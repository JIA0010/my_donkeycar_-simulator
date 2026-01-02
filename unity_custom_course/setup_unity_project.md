# Unity プロジェクト セットアップ詳細ガイド
## 赤い壁と黒い道のカスタムコース作成

## 📋 目次

1. [前提条件](#前提条件)
2. [Unityのインストール](#unityのインストール)
3. [Donkey Simulatorのセットアップ](#donkey-simulatorのセットアップ)
4. [カスタムシーンの作成](#カスタムシーンの作成)
5. [マテリアルの設定](#マテリアルの設定)
6. [トラックの構築](#トラックの構築)
7. [ビルドと実行](#ビルドと実行)
8. [Donkey Carとの統合](#donkey-carとの統合)

---

## 1️⃣ 前提条件

### 必要なソフトウェア

- **Unity Hub**: https://unity.com/download
- **Unity LTS**: Unity Hub経由でインストール
  - **推奨**: 2022 LTS（最新の長期サポート版）
  - **代替**: 6.0 LTS, 6.3 LTS, Unity 6 LTS
  - **互換性**: 2020.3 LTS以降のすべてのバージョン
- **Git**: https://git-scm.com/downloads
- **テキストエディタ**: Visual Studio Code推奨

### システム要件

- **OS**: macOS 10.13+, Windows 10+, Ubuntu 18.04+
- **CPU**: Intel Core i5以上
- **RAM**: 8GB以上（16GB推奨）
- **GPU**: DirectX 11/12対応GPU
- **ディスク**: 10GB以上の空き容量

---

## 2️⃣ Unityのインストール

### ステップ1: Unity Hubのインストール

```bash
# macOS (Homebrewを使用)
brew install --cask unity-hub

# または公式サイトからダウンロード
# https://unity.com/download
```

### ステップ2: Unity LTS のインストール

1. Unity Hubを起動
2. 左メニューから「Installs」を選択
3. 「Install Editor」をクリック
4. **利用可能なLTSバージョンを選択**:
   - **推奨**: 2022 LTS（最新の長期サポート版）
   - **代替**: 6.0 LTS, 6.3 LTS, または Unity 6 LTS
   - **互換性**: 2020.3 LTS以降のすべてのLTSバージョンで動作します
5. モジュールを選択:
   - ✅ Mac Build Support (macOS)
   - ✅ Windows Build Support (Windows)
   - ✅ Linux Build Support (Linux)
   - ✅ Documentation
6. 「Install」をクリック

**インストール時間**: 約15-30分

**注**: 2020.3 LTSが表示されない場合、より新しいLTSバージョン（2022 LTS推奨）を使用してください。Donkey Simulatorは新しいUnityバージョンとも互換性があります。

---

## 3️⃣ Donkey Simulatorのセットアップ

### ステップ1: ソースコードの取得

```bash
# デスクトップに移動
cd ~/Desktop

# Donkey Simulator のソースをクローン
git clone https://github.com/tawnkramer/sdsandbox
cd sdsandbox

# 確認
ls sdsim
# Assets, ProjectSettings などが表示されればOK
```

### ステップ2: Unityでプロジェクトを開く

1. Unity Hubを起動
2. 「Projects」タブを選択
3. 「Open」ボタンをクリック
4. `~/Desktop/sdsandbox/sdsim` フォルダを選択
5. Unity バージョンを選択（インストールしたLTSバージョン）
6. Unity エディターが開くまで待つ（初回は数分かかる）

**注意**: 
- 最初の起動時、Unityが自動的にプロジェクトを新しいバージョンにアップグレードする場合があります。これは正常です。
- 「Upgrade project to Unity [バージョン]」と表示された場合、**Proceed** または **Upgrade** をクリックしてください。
- アップグレード後、いくつかの警告が出る可能性がありますが、通常は無視して問題ありません。

---

## 4️⃣ カスタムシーンの作成

### ステップ1: 新しいシーンを作成

1. Unity エディタで、`File` → `New Scene` を選択
2. テンプレート: `3D` を選択
3. `File` → `Save As...` を選択
4. 保存先: `Assets/Scenes/CustomRedWallTrack.unity`
5. シーン名: `CustomRedWallTrack`

### ステップ2: 基本的な照明を設定

シーンには自動的に Directional Light が含まれています。

1. Hierarchy で `Directional Light` を選択
2. Inspector で以下を設定:
   - **Rotation**: X=50, Y=-30, Z=0
   - **Intensity**: 1.0
   - **Color**: 白 (255, 255, 255)

### ステップ3: 環境設定

1. `Window` → `Rendering` → `Lighting` を開く
2. Environment タブで:
   - **Sky Material**: Default-Skybox
   - **Sun Source**: Directional Light
   - **Environment Lighting**: Skybox
   - **Ambient Intensity**: 1.0

---

## 5️⃣ マテリアルの設定

### ステップ1: 黒い道のマテリアル作成

1. Project パネルで右クリック → `Create` → `Material`
2. 名前: `BlackRoad`
3. Inspector で設定:
   - **Shader**: Standard
   - **Albedo Color**: RGB(0, 0, 0) - 完全な黒
   - **Metallic**: 0
   - **Smoothness**: 0.5

### ステップ2: 赤い壁のマテリアル作成

1. Project パネルで右クリック → `Create` → `Material`
2. 名前: `RedWall`
3. Inspector で設定:
   - **Shader**: Standard
   - **Albedo Color**: RGB(255, 0, 0) - 鮮やかな赤
   - **Metallic**: 0
   - **Smoothness**: 0.3

### ステップ3: マテリアルを整理

1. Project パネルで `Materials` フォルダを作成
2. `BlackRoad` と `RedWall` を `Materials` フォルダに移動

---

## 6️⃣ トラックの構築

### 方法A: 手動でトラックを作成（シンプル）

#### 道路の作成

1. Hierarchy で右クリック → `3D Object` → `Plane`
2. 名前: `Road`
3. Inspector で設定:
   - **Position**: X=0, Y=0, Z=0
   - **Rotation**: X=0, Y=0, Z=0
   - **Scale**: X=10, Y=1, Z=50（幅10m、長さ50m）
4. `BlackRoad` マテリアルをドラッグ＆ドロップ

#### 左の壁を作成

1. Hierarchy で右クリック → `3D Object` → `Cube`
2. 名前: `WallLeft`
3. Inspector で設定:
   - **Position**: X=-5, Y=1, Z=0（道路の左端）
   - **Rotation**: X=0, Y=0, Z=0
   - **Scale**: X=0.2, Y=2, Z=50（厚さ0.2m、高さ2m、長さ50m）
4. `RedWall` マテリアルをドラッグ＆ドロップ

#### 右の壁を作成

1. Hierarchy で右クリック → `3D Object` → `Cube`
2. 名前: `WallRight`
3. Inspector で設定:
   - **Position**: X=5, Y=1, Z=0（道路の右端）
   - **Rotation**: X=0, Y=0, Z=0
   - **Scale**: X=0.2, Y=2, Z=50
4. `RedWall` マテリアルをドラッグ＆ドロップ

#### カーブを追加（オプション）

カーブを追加する場合は、追加のPlaneとCubeを回転させて配置します。

### 方法B: スクリプトで自動生成（高度）

提供されている `SimpleTrackGenerator.cs` スクリプトを使用します。

#### ステップ1: スクリプトの配置

```bash
# スクリプトをUnityプロジェクトにコピー
cp unity_custom_course/scripts/SimpleTrackGenerator.cs \
   ~/Desktop/sdsandbox/sdsim/Assets/Scripts/
```

#### ステップ2: 空のGameObjectを作成

1. Hierarchy で右クリック → `Create Empty`
2. 名前: `TrackGenerator`
3. Position: X=0, Y=0, Z=0

#### ステップ3: スクリプトをアタッチ

1. `TrackGenerator` を選択
2. Inspector で `Add Component` → `Simple Track Generator`
3. パラメータを設定:
   - **Track Width**: 4.0
   - **Track Length**: 50.0
   - **Wall Height**: 2.0
   - **Wall Thickness**: 0.2

#### ステップ4: 生成

1. Unity エディタで `Play` ボタンをクリック
2. トラックが自動生成される
3. `Stop` を押して編集モードに戻る
4. 生成されたオブジェクトは保持される

---

## 7️⃣ Donkey Car Prefab の追加

### ステップ1: 車のPrefabを配置

1. Project パネルで `Assets/Prefabs/` を開く
2. `DonkeyCar` または `Car` という名前のPrefabを探す
3. Prefabをシーンにドラッグ＆ドロップ
4. Position: X=0, Y=0.5, Z=-20（スタート地点）

### ステップ2: カメラの設定

車にはカメラが含まれているはずですが、確認:

1. Hierarchy で `DonkeyCar` → `Camera` を選択
2. Position と Rotation が適切か確認

### ステップ3: シーンを保存

`File` → `Save` または `Ctrl+S` (Mac: `Cmd+S`)

---

## 8️⃣ ビルドと実行

### ステップ1: ビルド設定

1. `File` → `Build Settings` を開く
2. `Scenes In Build` に `CustomRedWallTrack` が含まれていることを確認
3. 含まれていない場合、`Add Open Scenes` をクリック
4. プラットフォームを選択:
   - macOS: `Mac OSX`
   - Windows: `PC, Mac & Linux Standalone` → `Windows`
   - Linux: `PC, Mac & Linux Standalone` → `Linux`
5. `Switch Platform` をクリック（必要な場合）

### ステップ2: Player Settings

1. `Player Settings` ボタンをクリック
2. Inspector で設定:
   - **Company Name**: あなたの名前
   - **Product Name**: DonkeySimCustom
   - **Resolution and Presentation**:
     - `Fullscreen Mode`: Windowed
     - `Default Screen Width`: 1280
     - `Default Screen Height`: 720

### ステップ3: ビルド

1. `Build Settings` で `Build` をクリック
2. 保存先を選択（例: `~/Desktop/DonkeySimCustom`）
3. ビルドが完了するまで待つ（5-15分）

### ステップ4: 実行テスト

```bash
# macOS
open ~/Desktop/DonkeySimCustom/DonkeySimCustom.app

# Windows
~/Desktop/DonkeySimCustom/DonkeySimCustom.exe

# Linux
chmod +x ~/Desktop/DonkeySimCustom/DonkeySimCustom.x86_64
~/Desktop/DonkeySimCustom/DonkeySimCustom.x86_64
```

シミュレーターが起動し、赤い壁と黒い道のコースが表示されればOK！

---

## 9️⃣ Donkey Carとの統合

### ステップ1: myconfig.py を更新

```bash
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
```

`mycar/myconfig.py` を編集:

```python
DONKEY_GYM = True
DONKEY_SIM_PATH = "/Users/yoshimurahiro/Desktop/DonkeySimCustom/DonkeySimCustom.app"  # macOS
# DONKEY_SIM_PATH = "C:/Users/YourName/Desktop/DonkeySimCustom/DonkeySimCustom.exe"  # Windows
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"  # カスタムの場合も同じ
```

### ステップ2: シミュレーターを起動

```bash
# カスタムシミュレーターを手動で起動
open ~/Desktop/DonkeySimCustom/DonkeySimCustom.app
```

### ステップ3: Donkey Carを接続

```bash
cd mycar
python manage.py drive
```

ブラウザで `http://localhost:8887` を開き、車を操作できることを確認。

---

## 🎉 完了！

これで赤い壁と黒い道のカスタムコースが完成しました！

### 次のステップ

1. **データ収集**: カスタムコースで運転してデータを収集
2. **トレーニング**: `python train.py --tub ./data --model ./models/custom_pilot.h5`
3. **オートパイロット**: `python manage.py drive --model ./models/custom_pilot.h5`

### カスタマイズ

- コースの長さや形状を変更
- 壁の色や高さを調整
- 障害物を追加
- 複数のトラックバリエーションを作成

---

## 🛠️ トラブルシューティング

### ビルドエラー: "No valid Unity license"
- Unity Hub → Settings → License Management → Activate new license
- Personal (free) を選択

### カメラが表示されない
- DonkeyCar Prefab にカメラが含まれているか確認
- Main Camera タグが設定されているか確認

### 接続エラー
- シミュレーターが起動しているか確認
- ポート9091が使用可能か確認: `lsof -i :9091`
- ファイアウォール設定を確認

### パフォーマンスが悪い
- Graphics Quality を `Fast` または `Fastest` に変更
- 解像度を下げる（Build Settings → Player Settings）

---

**Happy Building! 🏗️💨**
