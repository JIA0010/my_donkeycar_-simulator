# Donkey Carシミュレーター 起動ガイド

このガイドでは、Donkey Carシミュレーターの起動方法を詳しく説明します。

## 🎮 シミュレーターのダウンロード

### macOS の場合

1. [Donkey Gym Releases](https://github.com/tawnkramer/gym-donkeycar/releases) にアクセス
2. 最新リリースから **`DonkeySimMac.zip`** をダウンロード
3. ダウンロードしたファイルを解凍
4. `donkey_sim.app` を**アプリケーションフォルダ**または任意の場所に配置

### 初回起動時の注意（macOS）

macOSでは、初回起動時にセキュリティ警告が表示される場合があります：

1. `donkey_sim.app` をダブルクリック
2. 「開発元を確認できないため開けません」と表示された場合：
   - **システム設定** → **プライバシーとセキュリティ** を開く
   - 下部に「"donkey_sim.app"は開発元を確認できないため、使用がブロックされました」と表示されているので、**「このまま開く」** をクリック
3. または、以下のコマンドで起動：
   ```bash
   xattr -cr /Applications/donkey_sim.app
   ```

## 🚀 シミュレーターの起動手順

### 1. シミュレーターアプリを起動

`donkey_sim.app`（またはOS別の実行ファイル）をダブルクリックします。

### 2. 設定画面が表示される

シミュレーターが起動すると、**Unity起動設定画面**が表示されます：

```
┌─────────────────────────────────────┐
│  DonkeySimMac                       │
│                                     │
│  Graphics                           │
│  ○ Fastest                          │
│  ○ Fast                             │
│  ◉ Good         ← これを選択       │
│  ○ Beautiful                        │
│  ○ Fantastic                        │
│                                     │
│  Screen Resolution                  │
│  [1920 x 1080  ▼]                  │
│                                     │
│  [ ] Windowed                       │
│                                     │
│  [      Cancel      ] [ Play! ]    │
└─────────────────────────────────────┘
```

#### 推奨設定：

- **Graphics Quality**: `Good` または `Fast`
  - PCの性能が高い場合: `Beautiful`
  - PCの性能が低い場合: `Fast` または `Fastest`
  
- **Screen Resolution**: お好みで（`1920x1080`推奨）

- **Windowed**: ウィンドウモードで起動したい場合はチェック

### 3. 「Play!」ボタンをクリック

設定が完了したら、右下の **「Play!」** ボタンをクリックします。

### 4. シミュレーターが起動

数秒後、3Dシミュレーター画面が表示されます。

#### 新しいバージョンの場合

新しいバージョンのシミュレーターでは、起動後にさらに選択画面が表示されます：

1. **Scene Selection（シーン選択）**
   ```
   Select a Scene:
   - Generated Track (recommended for beginners)
   - Generated Road
   - Warehouse
   - Sparkfun AVC
   ```
   → `Generated Track` を選択してください

2. 選択後、自動的にシミュレーターが開始されます

### 5. 起動成功の確認

以下が表示されていればOKです：

- ✅ 3D道路/トラックが表示されている
- ✅ 画面上部に「Waiting for car...」または「Connected」と表示
- ✅ 画面がフリーズしていない

## 🔧 トラブルシューティング

### シミュレーターが起動しない（macOS）

```bash
# 権限を修正
xattr -cr /path/to/donkey_sim.app

# または、ターミナルから起動
open /path/to/donkey_sim.app
```

### 「Play!」ボタンが見当たらない

- **ケース1**: 既に起動している
  - 設定画面をスキップして直接3D画面が表示される場合があります
  
- **ケース2**: 古いバージョン
  - シミュレーター内で右クリック → 設定からシーンを選択

### 画面が真っ黒

- グラフィック設定を下げて再起動してください
- `Graphics Quality` を `Fast` または `Fastest` に変更

### 接続できない（Waiting for car...のまま）

1. シミュレーターのポート番号を確認（デフォルト: 9091）
2. `myconfig.py`の設定を確認：
   ```python
   DONKEY_GYM = True
   SIM_HOST = "127.0.0.1"
   ```
3. ファイアウォールの設定を確認

## 📝 次のステップ

シミュレーターが正常に起動したら：

```bash
# メインディレクトリに戻る
cd /Users/yoshimurahiro/mysim

# 手動走行モードを起動
./start_drive.sh
```

ブラウザで `http://localhost:8887` を開いて操作します！

---

**参考**: [公式ドキュメント - Simulator](https://docs.donkeycar.com/guide/simulator/)
