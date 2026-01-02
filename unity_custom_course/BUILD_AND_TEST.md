# 🏗️ ビルドとテストガイド
## カスタムシミュレーターのビルドと検証

このガイドでは、カスタムシミュレーターを正しくビルドし、テストする方法を説明します。

---

## 📋 目次

1. [ビルド前の確認](#ビルド前の確認)
2. [ビルド設定](#ビルド設定)
3. [ビルド実行](#ビルド実行)
4. [テスト手順](#テスト手順)
5. [Donkey Carとの統合テスト](#donkey-carとの統合テスト)
6. [トラブルシューティング](#トラブルシューティング)

---

## 1️⃣ ビルド前の確認

### シーンの確認

Unity エディタで以下を確認:

```
✅ CustomRedWallTrack.unity が作成されている
✅ 道路（黒）と壁（赤）が表示されている
✅ Donkey Car Prefab が配置されている
✅ カメラが車に追従している
✅ Directional Light がある
```

### Play モードでテスト

1. Unity エディタで **▶ Play** をクリック
2. 確認事項:
   - 道路が黒く表示される
   - 壁が赤く表示される
   - 車が正しい位置にある
   - カメラが機能している
3. **■ Stop** をクリック

### スクリプトエラーの確認

Unity Console (Window → General → Console) を開いて:

```
✅ エラーがないこと
⚠️ 警告は無視してOK（一部のDonkey関連の警告は正常）
```

---

## 2️⃣ ビルド設定

### Build Settings を開く

Unity エディタで: **File → Build Settings**

### シーンの追加

```
✅ Scenes In Build リストに CustomRedWallTrack が含まれている
❌ 含まれていない場合: Add Open Scenes をクリック
```

### プラットフォーム選択

#### macOS の場合

1. **Platform** → **Mac OSX** を選択
2. **Switch Platform** をクリック（まだ選択されていない場合）
3. 待つ（数分かかる場合がある）

#### Windows の場合

1. **Platform** → **PC, Mac & Linux Standalone** を選択
2. **Target Platform** → **Windows** を選択
3. **Architecture** → **x86_64** を選択
4. **Switch Platform** をクリック

#### Linux の場合

1. **Platform** → **PC, Mac & Linux Standalone** を選択
2. **Target Platform** → **Linux** を選択
3. **Architecture** → **x86_64** を選択
4. **Switch Platform** をクリック

### Player Settings

**Player Settings** ボタンをクリックして設定:

```
Company Name: YourName
Product Name: DonkeySimCustom

Resolution and Presentation:
  ✅ Fullscreen Mode: Windowed
  ✅ Default Screen Width: 1280
  ✅ Default Screen Height: 720
  ✅ Resizable Window: チェック
  ❌ Run In Background: チェックを外す

Other Settings:
  ✅ Color Space: Gamma（または Linear）
  ✅ Auto Graphics API: チェック
```

---

## 3️⃣ ビルド実行

### ステップ1: ビルドボタンをクリック

**Build Settings** ウィンドウで **Build** をクリック

### ステップ2: 保存先を選択

```bash
# macOS/Linux
~/Desktop/DonkeySimCustom

# Windows
C:\Users\YourName\Desktop\DonkeySimCustom
```

### ステップ3: ビルド開始

- 進捗バーが表示される
- **所要時間**: 5-15分（PCの性能による）
- ビルド中は他の作業をしてOK

### ステップ4: ビルド完了の確認

```bash
# macOS
ls ~/Desktop/DonkeySimCustom/
# DonkeySimCustom.app が表示されればOK

# Windows
dir C:\Users\YourName\Desktop\DonkeySimCustom\
# DonkeySimCustom.exe が表示されればOK

# Linux
ls ~/Desktop/DonkeySimCustom/
# DonkeySimCustom.x86_64 が表示されればOK
```

---

## 4️⃣ テスト手順

### テスト1: 単体起動テスト

#### macOS

```bash
open ~/Desktop/DonkeySimCustom/DonkeySimCustom.app
```

#### Windows

```bash
~/Desktop/DonkeySimCustom/DonkeySimCustom.exe
```

#### Linux

```bash
chmod +x ~/Desktop/DonkeySimCustom/DonkeySimCustom.x86_64
~/Desktop/DonkeySimCustom/DonkeySimCustom.x86_64
```

### 確認事項

起動後、以下を確認:

```
✅ 設定画面が表示される
✅ Scene: CustomRedWallTrack が選択されている
✅ Graphics Quality が選択できる
✅ Port: 9091 が表示されている
```

設定画面を閉じるか、そのまま待つ:

```
✅ 3D環境が表示される
✅ 道路が黒く表示される
✅ 壁が赤く表示される
✅ 車が配置されている
✅ FPS が表示される（左上）
```

### テスト2: ネットワーク接続テスト

シミュレーターが起動している状態で、別のターミナルで:

```bash
# ポート9091が開いているか確認
lsof -i :9091

# macOS/Linux
# COMMAND   PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
# DonkeySim 1234 user   15u  IPv4 ...     0t0  TCP *:9091 (LISTEN)
```

✅ 上記のように表示されればOK

---

## 5️⃣ Donkey Carとの統合テスト

### ステップ1: シミュレーターを起動

```bash
# シミュレーターを起動（前のセクション参照）
open ~/Desktop/DonkeySimCustom/DonkeySimCustom.app
```

### ステップ2: myconfig.py を設定

```bash
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
```

`mycar/myconfig.py` を確認・編集:

```python
DONKEY_GYM = True
DONKEY_SIM_PATH = "/Users/yoshimurahiro/Desktop/DonkeySimCustom/DonkeySimCustom.app"
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"

SIM_HOST = "127.0.0.1"
```

### ステップ3: Donkey Carを起動

```bash
cd mycar
source ../env/bin/activate
python manage.py drive
```

### 期待される出力

```
loading config file: .../myconfig.py
Setting default: start_delay 5.0
Setting default: max_cte 8.0
connecting to 127.0.0.1:9091
loading scene CustomRedWallTrack  ← これが表示されればOK
sim started!
Starting vehicle at 20 Hz
You can now go to http://localhost:8887 to drive your car.
```

### ステップ4: ブラウザで操作

1. ブラウザで `http://localhost:8887` を開く
2. 車が表示されることを確認
3. キーボードで操作:
   - **↑**: 前進
   - **↓**: 後退
   - **←**: 左旋回
   - **→**: 右旋回

### 確認事項

```
✅ ブラウザに車のカメラ映像が表示される
✅ 黒い道と赤い壁が映っている
✅ キーボード操作で車が動く
✅ シミュレーター側で車の動きが確認できる
```

---

## 6️⃣ パフォーマンステスト

### FPS（フレームレート）の確認

シミュレーター左上に表示されるFPSを確認:

```
✅ 30 FPS以上: 優秀
⚠️ 20-30 FPS: 許容範囲
❌ 20 FPS以下: グラフィック設定を下げる必要あり
```

### グラフィック設定の調整

FPSが低い場合:

1. シミュレーターを再起動
2. 設定画面で **Graphics Quality** を変更:
   - **Fast** または **Fastest** を選択
3. 解像度を下げる（1280x720 → 1024x768）

### レイテンシ（遅延）の確認

```bash
# Donkey Car のログを確認
# 「DonkeyGymEnv」のタイミングを見る
```

```
✅ 0.02-0.05ms: 優秀
⚠️ 0.05-0.10ms: 許容範囲
❌ 0.10ms以上: ネットワークまたはPC性能の問題
```

---

## 7️⃣ データ収集テスト

### テスト手順

1. ブラウザ (`http://localhost:8887`) で **Start Recording** をクリック
2. 車を運転（1周程度）
3. **Stop Recording** をクリック
4. データが保存されたか確認

### データの確認

```bash
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator/mycar

# データ数を確認
ls data/images/ | wc -l

# 最低でも50-100枚あればOK
```

### 画像の確認

```bash
# 最初の画像を開いて確認
open data/images/0_cam_image_array_.jpg
```

確認事項:

```
✅ 黒い道が写っている
✅ 赤い壁が写っている
✅ 画像が鮮明
✅ 暗すぎない、明るすぎない
```

---

## 8️⃣ トレーニングテスト

十分なデータ（500枚以上推奨）を収集したら:

```bash
cd mycar
python train.py --tub ./data --model ./models/custom_pilot.h5
```

### 期待される結果

```
Loading data...
Found 500 samples
Training...
Epoch 1/150
Train on 400 samples, validate on 100 samples
loss: 50.234 - val_loss: 48.123  ← 徐々に減少すればOK
...
```

### 成功の指標

```
✅ Training loss が 30以下に下がる
✅ Validation loss が 35以下に下がる
✅ エポックごとに損失が減少している
```

---

## 9️⃣ オートパイロットテスト

トレーニング完了後:

```bash
python manage.py drive --model ./models/custom_pilot.h5
```

ブラウザで:

1. **Mode** → **Local Pilot** に切り替え
2. 車が自動で走ることを確認

### 確認事項

```
✅ 車が道路の中央を走る
✅ 壁にぶつからない
✅ カーブで外れない
✅ 最低1周完走できる
```

---

## 🛠️ トラブルシューティング

### ビルドエラー: "No valid Unity license"

**解決策:**
```
Unity Hub → Settings → License Management
→ Activate New License → Personal (free)
```

### シミュレーターが起動しない（macOS）

**解決策:**
```bash
# セキュリティ設定を確認
System Preferences → Security & Privacy
→ "Allow apps downloaded from: App Store and identified developers"

# または、アプリを右クリック → Open
```

### 接続エラー: "connection refused"

**解決策:**
```
1. シミュレーターが起動しているか確認
2. ポート9091が使用可能か確認: lsof -i :9091
3. ファイアウォール設定を確認
4. myconfig.py の SIM_HOST が "127.0.0.1" になっているか確認
```

### カメラ映像が表示されない

**解決策:**
```
1. Unity エディタでカメラが車にアタッチされているか確認
2. カメラのタグが "MainCamera" になっているか確認
3. シーンを再ビルド
```

### FPSが低い

**解決策:**
```
1. Graphics Quality を "Fast" に変更
2. 解像度を下げる
3. 他のアプリケーションを閉じる
4. Unity Build Settings → Player Settings で最適化オプションを確認
```

### データが保存されない

**解決策:**
```
1. mycar/data/ ディレクトリの権限を確認
2. ディスク容量を確認
3. Start Recording ボタンがクリックされているか確認
```

---

## ✅ チェックリスト

ビルドとテストが完了したら、以下を確認:

- [x] シミュレーターが単体で起動する
- [x] 赤い壁と黒い道が表示される
- [x] Donkey Carから接続できる
- [x] ブラウザで車を操作できる
- [x] データ収集ができる
- [x] 画像が正しく保存される
- [x] FPSが30以上
- [x] トレーニングが実行できる
- [x] オートパイロットが動作する

すべてチェックできたら、カスタムコースの完成です！🎉

---

## 📚 次のステップ

1. **データ収集**: カスタムコースで大量のデータを収集
2. **モデル改善**: 異なるモデルアーキテクチャを試す
3. **コースのカスタマイズ**: 障害物や複雑なカーブを追加
4. **複数のコース**: バリエーションを作成

---

**Happy Testing! 🧪💨**
