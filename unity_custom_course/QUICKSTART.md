# 🚀 クイックスタートガイド
## 赤い壁と黒い道のカスタムコースを今すぐ作る

このガイドに従えば、**30分で**カスタムコースを作成できます！

---

## ⏱️ 所要時間: 30分

- Unity インストール: 15分
- プロジェクトセットアップ: 5分
- トラック作成: 5分
- ビルド: 5分

---

## 📋 準備するもの

- ✅ macOS, Windows, または Linux PC
- ✅ 10GB 以上の空き容量
- ✅ インターネット接続

---

## ステップ1️⃣: Unityをインストール（15分）

### macOS

```bash
# Homebrew でインストール
brew install --cask unity-hub

# Unity Hub を起動
open -a "Unity Hub"
```

### Windows

1. https://unity.com/download からUnity Hubをダウンロード
2. インストーラーを実行
3. Unity Hubを起動

### Unity LTS をインストール

1. Unity Hub → **Installs** タブ
2. **Install Editor** をクリック
3. **利用可能なLTSバージョンを選択**:
   - **推奨**: 2022 LTS（最新）
   - **代替**: 6.0 LTS または 6.3 LTS
   - **注**: 2020.3 LTSが表示されない場合、より新しいバージョンで問題ありません
4. モジュール:
   - ✅ Mac Build Support (macOS)
   - ✅ Windows Build Support (Windows)
5. **Install** をクリック
6. 完了まで待つ（10-15分）

---

## ステップ2️⃣: Donkey Simulatorを取得（5分）

```bash
# デスクトップに移動
cd ~/Desktop

# Donkey Simulator をクローン
git clone https://github.com/tawnkramer/sdsandbox
cd sdsandbox

# 確認
ls sdsim
# Assets/ ProjectSettings/ などが表示されればOK
```

---

## ステップ3️⃣: Unityプロジェクトを開く（5分）

1. Unity Hub を開く
2. **Projects** タブ → **Open** をクリック
3. `~/Desktop/sdsandbox/sdsim` を選択
4. Unity バージョンを選択（インストールしたLTSバージョンを選択）
5. プロジェクトが開くまで待つ（初回は3-5分）

**注**: バージョンアップグレードの警告が出た場合、**Upgrade** を選択してください。これは正常です。

---

## ステップ4️⃣: カスタムスクリプトをコピー（1分）

```bash
# Donkey Car プロジェクトに戻る
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator

# スクリプトをコピー
cp unity_custom_course/scripts/SimpleTrackGenerator.cs \
   ~/Desktop/sdsandbox/sdsim/Assets/Scripts/

cp unity_custom_course/scripts/RedWallBlackRoadMaterials.cs \
   ~/Desktop/sdsandbox/sdsim/Assets/Scripts/
```

---

## ステップ5️⃣: カスタムシーンを作成（5分）

### 5-1: 新しいシーンを作成

Unity エディタで:

1. **File** → **New Scene** → **3D** を選択
2. **File** → **Save As...**
3. 保存先: `Assets/Scenes/CustomRedWallTrack.unity`

### 5-2: トラック生成オブジェクトを追加

1. **Hierarchy** で右クリック → **Create Empty**
2. 名前: `TrackGenerator`
3. **Inspector** で **Add Component** → `Simple Track Generator`
4. パラメータ設定:
   - Track Width: `4.0`
   - Straight Length: `30.0`
   - Wall Height: `2.0`
   - Wall Thickness: `0.2`
   - Road Color: 黒 (R=0, G=0, B=0)
   - Wall Color: 赤 (R=255, G=0, B=0)
   - Create Oval Track: ✅ チェック

### 5-3: トラックを生成

1. Unity エディタの上部にある **▶ Play** ボタンをクリック
2. トラックが自動生成される（赤い壁と黒い道）
3. **■ Stop** ボタンをクリック
4. **File** → **Save** (Cmd+S / Ctrl+S)

✅ これで赤い壁と黒い道のトラックが完成！

---

## ステップ6️⃣: Donkey Car Prefabを追加（2分）

### 6-1: 車を配置

1. **Project** パネル → `Assets/Prefabs/` を開く
2. `DonkeyCar` Prefabを探す
3. **Hierarchy** にドラッグ＆ドロップ
4. **Inspector** で Position: `X=0, Y=0.5, Z=-10`

### 6-2: シーンを保存

**File** → **Save** (Cmd+S / Ctrl+S)

---

## ステップ7️⃣: ビルド（5分）

### 7-1: ビルド設定

1. **File** → **Build Settings**
2. **Scenes In Build** に `CustomRedWallTrack` があることを確認
3. なければ **Add Open Scenes** をクリック
4. Platform を選択:
   - **macOS**: Mac OSX
   - **Windows**: PC, Mac & Linux Standalone → Windows
5. **Build** をクリック

### 7-2: 保存先を選択

```
保存先: ~/Desktop/DonkeySimCustom
```

### 7-3: ビルド完了を待つ（5分）

コーヒーブレイク ☕

---

## ステップ8️⃣: テスト実行（1分）

```bash
# macOS
open ~/Desktop/DonkeySimCustom/DonkeySimCustom.app

# Windows
~/Desktop/DonkeySimCustom/DonkeySimCustom.exe
```

✅ 赤い壁と黒い道が表示されればOK！

---

## ステップ9️⃣: Donkey Carと接続（2分）

### 9-1: 設定ファイルを更新

```bash
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
```

`mycar/myconfig.py` を編集:

```python
DONKEY_GYM = True
DONKEY_SIM_PATH = "/Users/yoshimurahiro/Desktop/DonkeySimCustom/DonkeySimCustom.app"  # macOS
# DONKEY_SIM_PATH = "C:/Users/YourName/Desktop/DonkeySimCustom/DonkeySimCustom.exe"  # Windows
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"
```

### 9-2: シミュレーターを起動

```bash
# カスタムシミュレーターを起動
open ~/Desktop/DonkeySimCustom/DonkeySimCustom.app
```

### 9-3: Donkey Carを接続

```bash
cd mycar
python manage.py drive
```

ブラウザで `http://localhost:8887` を開いて運転！

---

## 🎉 完了！

おめでとうございます！赤い壁と黒い道のカスタムコースが完成しました！

---

## 🎯 次のステップ

### 1. データ収集
```bash
# ブラウザで http://localhost:8887
# Start Recording → 運転 → Stop Recording
```

### 2. トレーニング
```bash
cd mycar
python train.py --tub ./data --model ./models/custom_pilot.h5
```

### 3. オートパイロット
```bash
python manage.py drive --model ./models/custom_pilot.h5
# ブラウザで "Local Pilot" に切り替え
```

---

## 💡 カスタマイズのヒント

### トラックを長くする
Unity エディタで `TrackGenerator` を選択 → Inspector:
```
Straight Length: 50.0  (30.0から変更)
```

### 壁を高くする
```
Wall Height: 3.0  (2.0から変更)
```

### 直線のみにする
```
Create Oval Track: ❌ チェックを外す
```

### 色を変える
```
Road Color: RGB(20, 20, 20)  # 濃いグレー
Wall Color: RGB(255, 100, 100)  # 明るい赤
```

---

## 🛠️ トラブルシューティング

### Unity が開けない
→ Unity LTS（2022 LTS推奨）がインストールされているか確認

### 2020.3 LTS が見つからない
→ **問題ありません！** 2022 LTS, 6.0 LTS, または 6.3 LTS を使用してください
→ 詳細: [UNITY_VERSION_NOTES.md](UNITY_VERSION_NOTES.md)

### プロジェクトアップグレード警告が出る
→ **「Proceed」または「Upgrade」をクリック** - これは正常です

### スクリプトが見つからない
→ `Assets/Scripts/` にコピーされているか確認

### ビルドエラー
→ `File → Build Settings` でシーンが追加されているか確認

### 接続できない
→ シミュレーターが起動しているか、ポート9091が空いているか確認

---

## 📚 詳細ドキュメント

もっと詳しく知りたい場合:

- 📖 [setup_unity_project.md](setup_unity_project.md) - 詳細なUnityセットアップ
- 📖 [README.md](README.md) - プロジェクト全体の説明
- 📖 [materials/README.md](materials/README.md) - マテリアルのカスタマイズ

---

**Happy Racing! 🏎️💨**

30分でカスタムコースが完成しました！
