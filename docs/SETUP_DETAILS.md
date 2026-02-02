# ✅ セットアップ確認（5分）

## 1. 仮想環境を有効化

```bash
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
source env/bin/activate
```

**確認**: プロンプトが `(env) $` になればOK

## 2. Donkey Car v5.0.0 確認

```bash
python -c "import donkeycar; print('Version:', donkeycar.__version__)"
```

**出力**: `Version: 5.0.0` ✅

## 3. 設定ファイル確認

```bash
cd mycar
cat myconfig.py | grep -E "^(DONKEY_GYM|IMAGE_W|IMAGE_H|LEARNING_RATE)"
```

**重要設定**: `DONKEY_GYM = True` (シミュレーターモード)

## 4. データディレクトリ確認

```bash
ls -la mycar/data/
```

## 5. モデルディレクトリ確認

```bash
ls -la mycar/models/
```

---

👉 [QUICKSTART.md](QUICKSTART.md) で実際に走らせてみましょう！
