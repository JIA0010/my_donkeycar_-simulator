# 🏗️ Unity カスタムコース作成ガイド
## 赤い壁と黒い道のシンプルなコース

このディレクトリには、Donkey Carシミュレーターで**赤い壁と黒い道のカスタムコース**を作成するためのすべてのファイルが含まれています。

## 📁 ディレクトリ構成

```
unity_custom_course/
├── README.md                          # このファイル
├── setup_unity_project.md             # Unityプロジェクトセットアップ手順
├── scripts/                           # Unityスクリプト
│   ├── SimpleTrackGenerator.cs        # シンプルなトラック生成スクリプト
│   └── RedWallBlackRoadMaterials.cs   # マテリアル設定スクリプト
├── materials/                         # マテリアル定義
│   ├── BlackRoad.mat                  # 黒い道のマテリアル（JSON定義）
│   └── RedWall.mat                    # 赤い壁のマテリアル（JSON定義）
└── scenes/                            # シーン設定
    └── CustomTrackScene.json          # カスタムシーン設定
```

## 🚀 クイックスタート

### ステップ1: Unityのインストール

```bash
# Unity Hubをダウンロード
# https://unity.com/download

# Unity LTS をインストール
# 推奨: 2022 LTS, 6.0 LTS, または 6.3 LTS
# Unity Hub → Installs → Install Editor
```

### ステップ2: Donkey Simulatorのソースを取得

```bash
cd ~/Desktop
git clone https://github.com/tawnkramer/sdsandbox
cd sdsandbox
```

### ステップ3: Unityでプロジェクトを開く

1. Unity Hubを起動
2. 「Open」→ `sdsandbox/sdsim` を選択
3. Unity 2020.3 LTS で開く

### ステップ4: カスタムスクリプトをコピー

```bash
# このディレクトリから Unityプロジェクトにスクリプトをコピー
cp scripts/*.cs ~/Desktop/sdsandbox/sdsim/Assets/Scripts/
```

### ステップ5: カスタムシーンを作成

詳細は `setup_unity_project.md` を参照してください。

## 📝 必要な環境

- **Unity**: 2020.3 LTS 以降（**推奨**: 2022 LTS, 6.0 LTS, 6.3 LTS）
- **OS**: macOS, Windows, または Linux
- **ディスク空き容量**: 10GB以上（Unityとプロジェクト用）
- **メモリ**: 8GB以上推奨

## 🎯 このガイドで作成するもの

### コースの仕様

- **道路**: 幅4m、黒色（RGB: 0, 0, 0）
- **壁**: 高さ2m、厚さ0.2m、赤色（RGB: 255, 0, 0）
- **コースレイアウト**: シンプルな楕円形または直線＋カーブ
- **長さ**: 約50-100m（調整可能）

### 特徴

- ✅ シンプルな構造（赤い壁、黒い道）
- ✅ 実際のコース環境に近い
- ✅ AIトレーニングに最適
- ✅ カスタマイズ可能

## 📚 ドキュメント

1. **[setup_unity_project.md](setup_unity_project.md)** - Unityプロジェクトの詳細セットアップ
2. **[scripts/SimpleTrackGenerator.cs](scripts/SimpleTrackGenerator.cs)** - トラック生成スクリプト
3. **[materials/](materials/)** - マテリアル定義

## 🛠️ トラブルシューティング

### Unityが起動しない
- Unity Hubから正しいバージョン（2020.3 LTS）を選択
- macOSの場合、セキュリティ設定を確認

### プロジェクトが開けない
- Unity バージョンが古い可能性 → 2020.3 LTS以降を使用
- プロジェクトが壊れている可能性 → 再クローン

### ビルドエラー
- プラットフォーム設定を確認（File → Build Settings）
- 必要なモジュールがインストールされているか確認

## 💡 カスタマイズ

### 道路の色を変更

`scripts/RedWallBlackRoadMaterials.cs` を編集:

```csharp
// 黒から別の色に変更
roadMaterial.color = new Color(0.1f, 0.1f, 0.1f); // 濃いグレー
```

### 壁の高さを変更

`scripts/SimpleTrackGenerator.cs` を編集:

```csharp
wallHeight = 3.0f; // 2mから3mに変更
```

### コースの形状を変更

`SimpleTrackGenerator.cs` のパラメータを調整して、楕円から他の形状に変更可能。

## 🎓 次のステップ

1. Unityをインストール
2. `setup_unity_project.md` の手順に従う
3. カスタムシーンを作成
4. ビルドして実行
5. Donkey Carで使用

## 📞 サポート

問題が発生した場合:
- 📖 `setup_unity_project.md` の詳細手順を確認
- 📖 メインの `CUSTOM_COURSE_GUIDE.md` を参照
- 💬 Donkey Car Discord: https://discord.gg/donkeycar

---

**Happy Building! 🏗️**
