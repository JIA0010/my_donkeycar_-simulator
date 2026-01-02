using UnityEngine;

/// <summary>
/// シンプルな赤い壁と黒い道のトラック生成スクリプト
/// 使い方: 空のGameObjectにこのスクリプトをアタッチして実行
/// </summary>
public class SimpleTrackGenerator : MonoBehaviour
{
    [Header("トラック設定")]
    [Tooltip("道路の幅（メートル）")]
    public float trackWidth = 4.0f;
    
    [Tooltip("直線部分の長さ（メートル）")]
    public float straightLength = 30.0f;
    
    [Tooltip("カーブの半径（メートル）")]
    public float curveRadius = 10.0f;
    
    [Header("壁設定")]
    [Tooltip("壁の高さ（メートル）")]
    public float wallHeight = 2.0f;
    
    [Tooltip("壁の厚さ（メートル）")]
    public float wallThickness = 0.2f;
    
    [Header("マテリアル設定")]
    [Tooltip("道路の色（黒）")]
    public Color roadColor = Color.black;
    
    [Tooltip("壁の色（赤）")]
    public Color wallColor = Color.red;
    
    [Header("トラックタイプ")]
    [Tooltip("true=楕円形, false=直線のみ")]
    public bool createOvalTrack = true;
    
    private Material roadMaterial;
    private Material wallMaterial;
    
    void Start()
    {
        // マテリアルを作成
        CreateMaterials();
        
        // トラックを生成
        if (createOvalTrack)
        {
            GenerateOvalTrack();
        }
        else
        {
            GenerateStraightTrack();
        }
    }
    
    /// <summary>
    /// マテリアルを作成
    /// </summary>
    void CreateMaterials()
    {
        // 黒い道のマテリアル
        roadMaterial = new Material(Shader.Find("Standard"));
        roadMaterial.color = roadColor;
        roadMaterial.SetFloat("_Metallic", 0f);
        roadMaterial.SetFloat("_Glossiness", 0.5f);
        
        // 赤い壁のマテリアル
        wallMaterial = new Material(Shader.Find("Standard"));
        wallMaterial.color = wallColor;
        wallMaterial.SetFloat("_Metallic", 0f);
        wallMaterial.SetFloat("_Glossiness", 0.3f);
    }
    
    /// <summary>
    /// 直線のトラックを生成
    /// </summary>
    void GenerateStraightTrack()
    {
        // 道路を作成
        GameObject road = CreateRoad(
            Vector3.zero,
            new Vector3(trackWidth, 0.1f, straightLength)
        );
        road.name = "Road_Straight";
        
        // 左の壁
        GameObject wallLeft = CreateWall(
            new Vector3(-trackWidth / 2, wallHeight / 2, 0),
            new Vector3(wallThickness, wallHeight, straightLength)
        );
        wallLeft.name = "Wall_Left";
        
        // 右の壁
        GameObject wallRight = CreateWall(
            new Vector3(trackWidth / 2, wallHeight / 2, 0),
            new Vector3(wallThickness, wallHeight, straightLength)
        );
        wallRight.name = "Wall_Right";
        
        // 前の壁
        GameObject wallFront = CreateWall(
            new Vector3(0, wallHeight / 2, straightLength / 2),
            new Vector3(trackWidth + wallThickness * 2, wallHeight, wallThickness)
        );
        wallFront.name = "Wall_Front";
        
        // 後ろの壁
        GameObject wallBack = CreateWall(
            new Vector3(0, wallHeight / 2, -straightLength / 2),
            new Vector3(trackWidth + wallThickness * 2, wallHeight, wallThickness)
        );
        wallBack.name = "Wall_Back";
    }
    
    /// <summary>
    /// 楕円形のトラックを生成
    /// </summary>
    void GenerateOvalTrack()
    {
        int segments = 32; // トラックのセグメント数
        float radiusX = straightLength / 2; // X方向の半径
        float radiusZ = curveRadius; // Z方向の半径
        
        GameObject trackParent = new GameObject("OvalTrack");
        trackParent.transform.position = Vector3.zero;
        
        // 楕円形のトラックをセグメントで作成
        for (int i = 0; i < segments; i++)
        {
            float angle1 = (float)i / segments * Mathf.PI * 2;
            float angle2 = (float)(i + 1) / segments * Mathf.PI * 2;
            
            Vector3 pos1 = new Vector3(
                Mathf.Cos(angle1) * radiusX,
                0,
                Mathf.Sin(angle1) * radiusZ
            );
            
            Vector3 pos2 = new Vector3(
                Mathf.Cos(angle2) * radiusX,
                0,
                Mathf.Sin(angle2) * radiusZ
            );
            
            Vector3 center = (pos1 + pos2) / 2;
            float segmentLength = Vector3.Distance(pos1, pos2);
            
            // 道路セグメント
            GameObject roadSegment = CreateRoad(
                new Vector3(center.x, 0, center.z),
                new Vector3(trackWidth, 0.1f, segmentLength)
            );
            roadSegment.name = $"Road_Segment_{i}";
            roadSegment.transform.parent = trackParent.transform;
            
            // 回転を計算
            Vector3 direction = (pos2 - pos1).normalized;
            float rotationAngle = Mathf.Atan2(direction.x, direction.z) * Mathf.Rad2Deg;
            roadSegment.transform.rotation = Quaternion.Euler(0, rotationAngle, 0);
            
            // 外側の壁
            CreateWallSegment(center, direction, segmentLength, trackWidth / 2 + wallThickness / 2, i, "Outer", trackParent.transform);
            
            // 内側の壁
            CreateWallSegment(center, direction, segmentLength, -(trackWidth / 2 + wallThickness / 2), i, "Inner", trackParent.transform);
        }
    }
    
    /// <summary>
    /// 壁のセグメントを作成
    /// </summary>
    void CreateWallSegment(Vector3 center, Vector3 direction, float length, float offset, int index, string side, Transform parent)
    {
        Vector3 perpendicular = new Vector3(-direction.z, 0, direction.x);
        Vector3 wallPosition = center + perpendicular * offset;
        wallPosition.y = wallHeight / 2;
        
        GameObject wall = CreateWall(
            wallPosition,
            new Vector3(wallThickness, wallHeight, length)
        );
        wall.name = $"Wall_{side}_{index}";
        wall.transform.parent = parent;
        
        float rotationAngle = Mathf.Atan2(direction.x, direction.z) * Mathf.Rad2Deg;
        wall.transform.rotation = Quaternion.Euler(0, rotationAngle, 0);
    }
    
    /// <summary>
    /// 道路オブジェクトを作成
    /// </summary>
    GameObject CreateRoad(Vector3 position, Vector3 scale)
    {
        GameObject road = GameObject.CreatePrimitive(PrimitiveType.Plane);
        road.transform.position = position;
        road.transform.localScale = new Vector3(scale.x / 10, 1, scale.z / 10); // Planeは10x10なので調整
        
        // マテリアルを適用
        Renderer renderer = road.GetComponent<Renderer>();
        renderer.material = roadMaterial;
        
        return road;
    }
    
    /// <summary>
    /// 壁オブジェクトを作成
    /// </summary>
    GameObject CreateWall(Vector3 position, Vector3 scale)
    {
        GameObject wall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        wall.transform.position = position;
        wall.transform.localScale = scale;
        
        // マテリアルを適用
        Renderer renderer = wall.GetComponent<Renderer>();
        renderer.material = wallMaterial;
        
        return wall;
    }
}
