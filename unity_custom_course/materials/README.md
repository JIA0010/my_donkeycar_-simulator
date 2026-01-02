# マテリアル定義ファイル

このディレクトリには、赤い壁と黒い道のマテリアル設定が含まれています。

## 使い方

### Unity エディタで手動作成する場合

#### 黒い道のマテリアル (BlackRoad.mat)

1. Unity Project パネルで右クリック → Create → Material
2. 名前を `BlackRoad` に変更
3. Inspector で以下を設定:

```
Shader: Standard
Rendering Mode: Opaque

Main Maps:
  - Albedo: RGB(0, 0, 0) - 完全な黒
  - Metallic: 0
  - Smoothness: 0.5
  - Normal Map: None
  - Height Map: None
  - Occlusion: None
  - Emission: None (黒)

Tiling: X=1, Y=1
Offset: X=0, Y=0
```

#### 赤い壁のマテリアル (RedWall.mat)

1. Unity Project パネルで右クリック → Create → Material
2. 名前を `RedWall` に変更
3. Inspector で以下を設定:

```
Shader: Standard
Rendering Mode: Opaque

Main Maps:
  - Albedo: RGB(255, 0, 0) - 鮮やかな赤
  - Metallic: 0
  - Smoothness: 0.3
  - Normal Map: None
  - Height Map: None
  - Occlusion: None
  - Emission: None (黒)

Tiling: X=1, Y=1
Offset: X=0, Y=0
```

## マテリアルのバリエーション

### より暗い赤（夕焼け風）
```
Albedo: RGB(180, 0, 0)
```

### 濃いグレーの道（より現実的）
```
Albedo: RGB(20, 20, 20)
```

### 光沢のある壁（プラスチック風）
```
Smoothness: 0.8
```

### マットな壁（コンクリート風）
```
Smoothness: 0.1
Metallic: 0
```

## スクリプトで生成する場合

`RedWallBlackRoadMaterials.cs` スクリプトを使用すると、自動的にマテリアルが生成されます。

### 使い方

1. 空の GameObject を作成
2. `RedWallBlackRoadMaterials.cs` をアタッチ
3. Inspector でパラメータを調整
4. Play ボタンを押すとマテリアルが生成される

### パラメータ調整例

```csharp
// より明るい赤
wallColor = new Color(1.0f, 0.3f, 0.3f);

// 濃いグレーの道
roadColor = new Color(0.1f, 0.1f, 0.1f);

// 滑らかな壁
wallSmoothness = 0.8f;
```

## テクスチャを追加する場合（オプション）

より現実的な見た目にしたい場合、テクスチャを追加できます。

### アスファルトテクスチャ（道路用）

無料のテクスチャサイト:
- https://www.textures.com/
- https://www.poliigon.com/
- https://freepbr.com/

1. アスファルトテクスチャをダウンロード
2. Unity にインポート
3. BlackRoad マテリアルの Albedo にドラッグ

### コンクリートテクスチャ（壁用）

1. 赤いコンクリートまたは塗装テクスチャをダウンロード
2. Unity にインポート
3. RedWall マテリアルの Albedo にドラッグ
4. Tint Color を赤 (255, 0, 0) に設定

## トラブルシューティング

### マテリアルが表示されない
- オブジェクトに Mesh Renderer コンポーネントがあるか確認
- マテリアルが正しく割り当てられているか確認

### 色が薄い・暗い
- Lighting 設定を確認
- Directional Light の Intensity を調整（推奨: 1.0）
- Environment Lighting の Intensity を確認

### 反射がおかしい
- Reflection Probes を追加
- Window → Rendering → Lighting → Generate Lighting

---

これらのマテリアルを使用して、シンプルで視覚的に明確なトラックを作成できます！
