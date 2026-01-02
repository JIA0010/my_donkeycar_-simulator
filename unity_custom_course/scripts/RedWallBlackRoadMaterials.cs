using UnityEngine;

/// <summary>
/// 赤い壁と黒い道のマテリアルを作成・管理するスクリプト
/// 使い方: 空のGameObjectにアタッチして実行
/// </summary>
public class RedWallBlackRoadMaterials : MonoBehaviour
{
    [Header("マテリアル設定")]
    [Tooltip("道路のマテリアル名")]
    public string roadMaterialName = "BlackRoad";
    
    [Tooltip("壁のマテリアル名")]
    public string wallMaterialName = "RedWall";
    
    [Header("道路の設定")]
    [Tooltip("道路の色")]
    public Color roadColor = Color.black;
    
    [Tooltip("道路の金属度（0-1）")]
    [Range(0f, 1f)]
    public float roadMetallic = 0f;
    
    [Tooltip("道路の滑らかさ（0-1）")]
    [Range(0f, 1f)]
    public float roadSmoothness = 0.5f;
    
    [Header("壁の設定")]
    [Tooltip("壁の色")]
    public Color wallColor = Color.red;
    
    [Tooltip("壁の金属度（0-1）")]
    [Range(0f, 1f)]
    public float wallMetallic = 0f;
    
    [Tooltip("壁の滑らかさ（0-1）")]
    [Range(0f, 1f)]
    public float wallSmoothness = 0.3f;
    
    void Start()
    {
        CreateMaterials();
    }
    
    /// <summary>
    /// マテリアルを作成してAssets/Materialsに保存
    /// </summary>
    void CreateMaterials()
    {
        // 道路のマテリアルを作成
        Material roadMaterial = CreateMaterial(
            roadMaterialName,
            roadColor,
            roadMetallic,
            roadSmoothness
        );
        
        Debug.Log($"道路マテリアル '{roadMaterialName}' を作成しました。色: {roadColor}");
        
        // 壁のマテリアルを作成
        Material wallMaterial = CreateMaterial(
            wallMaterialName,
            wallColor,
            wallMetallic,
            wallSmoothness
        );
        
        Debug.Log($"壁マテリアル '{wallMaterialName}' を作成しました。色: {wallColor}");
    }
    
    /// <summary>
    /// マテリアルを作成
    /// </summary>
    Material CreateMaterial(string materialName, Color color, float metallic, float smoothness)
    {
        Material material = new Material(Shader.Find("Standard"));
        material.name = materialName;
        material.color = color;
        material.SetFloat("_Metallic", metallic);
        material.SetFloat("_Glossiness", smoothness);
        
        return material;
    }
    
    /// <summary>
    /// シーン内のすべての道路オブジェクトにマテリアルを適用
    /// </summary>
    public void ApplyRoadMaterialToAll()
    {
        GameObject[] roads = GameObject.FindGameObjectsWithTag("Road");
        Material roadMaterial = CreateMaterial(roadMaterialName, roadColor, roadMetallic, roadSmoothness);
        
        foreach (GameObject road in roads)
        {
            Renderer renderer = road.GetComponent<Renderer>();
            if (renderer != null)
            {
                renderer.material = roadMaterial;
            }
        }
        
        Debug.Log($"{roads.Length}個の道路オブジェクトにマテリアルを適用しました。");
    }
    
    /// <summary>
    /// シーン内のすべての壁オブジェクトにマテリアルを適用
    /// </summary>
    public void ApplyWallMaterialToAll()
    {
        GameObject[] walls = GameObject.FindGameObjectsWithTag("Wall");
        Material wallMaterial = CreateMaterial(wallMaterialName, wallColor, wallMetallic, wallSmoothness);
        
        foreach (GameObject wall in walls)
        {
            Renderer renderer = wall.GetComponent<Renderer>();
            if (renderer != null)
            {
                renderer.material = wallMaterial;
            }
        }
        
        Debug.Log($"{walls.Length}個の壁オブジェクトにマテリアルを適用しました。");
    }
}
