# 🚀 クイックスタート（5分で始める）

## ステップ1: シミュレーター起動

```bash
# シミュレーターアプリを起動
open /Applications/donkey_sim.app

# (またはダウンロードしたフォルダから直接起動)
```

**設定画面で**:
- Graphics: `Good` または `Fast`
- Resolution: `1920x1080`
- **Play!** をクリック

シーン選択で **Generated Track** を選択

## ステップ2: 手動運転開始

```bash
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
source env/bin/activate
cd mycar
python manage.py drive
```

**ブラウザを開く**: `http://localhost:8887`

## ステップ3: データ収集

1. **Start Recording** をクリック
2. コースを5～10周走行（滑らかに）
3. **Stop Recording** をクリック

→ データが `mycar/data/` に保存されます

## ステップ4: モデル学習

```bash
# 新しいターミナルで
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
source env/bin/activate
cd mycar
donkey train --tub ./data --model ./models/mypilot.h5
```

## ステップ5: 自動運転テスト

```bash
python manage.py drive --model ./models/mypilot.h5
```

**ブラウザで Mode を `Local Pilot` に切り替える**

---

## 🎮 キーボード操作

| キー | 動作 |
|------|------|
| ↑↓ | 前進・後退 |
| ←→ | 左旋回・右旋回 |
| I/K | スロットル +/- |
| J/L | 左/右旋回 |

## ⚠️ エラーが出た？

- **シミュレーター非接続**: シミュレーターアプリを起動したか確認
- **ModuleNotFoundError**: `source env/bin/activate` で環境を有効化
- **ポート8887使用中**: `lsof -i :8887` で確認後、別のターミナルで再実行

---

**詳細は [QUICK_REFERENCE.md](QUICK_REFERENCE.md) を参照**
