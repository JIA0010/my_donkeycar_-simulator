# システムクリーンアップガイド

## 🧹 実施済みクリーンアップ

システムのPythonに誤ってインストールされたパッケージをすべて削除しました。

### 削除したパッケージ

以下のパッケージをシステムPython（Python 3.12）から削除しました：

- ✅ `donkeycar 2.5.8`
- ✅ `gym 0.22.0`
- ✅ `gym_donkeycar 1.3.1`
- ✅ `gym-notices 0.1.0`
- ✅ `gymnasium 1.2.3`
- ✅ `farama-notifications 0.0.4`
- ✅ `cloudpickle 3.1.2`

## ✅ 現在の正しい状態

### 仮想環境内（推奨）

`/Users/yoshimurahiro/mysim/env/` に以下がインストールされています：

```bash
donkeycar          5.0.0
gym                0.22.0
gym_donkeycar      1.3.1
gym-notices        0.1.0
```

### システムPython

クリーン（Donkey Car関連のパッケージなし）

## 🛡️ 今後の注意事項

### ❌ やってはいけないこと

```bash
# システムのpipを使用（NG）
pip install donkeycar
pip3 install gym-donkeycar
python3.12 -m pip install ...

# sudo付きでのインストール（絶対NG）
sudo pip install ...
```

### ✅ 正しい方法

このプロジェクトでは、**必ず仮想環境のpipを使用**してください：

```bash
# 方法1: フルパスで仮想環境のpipを使用
/Users/yoshimurahiro/mysim/env/bin/pip install <パッケージ名>

# 方法2: 仮想環境を有効化してから使用
cd /Users/yoshimurahiro/mysim
source env/bin/activate
pip install <パッケージ名>
```

### スクリプトの使用（最も推奨）

提供されているスクリプトを使用すれば、常に正しい仮想環境が使われます：

```bash
# 手動運転
./start_drive.sh

# 学習
./train_model.sh

# 自動運転
./start_autopilot.sh
```

## 🔍 確認方法

### 仮想環境のパッケージを確認

```bash
/Users/yoshimurahiro/mysim/env/bin/pip list | grep -E "gym|donkey"
```

期待される出力：
```
donkeycar          5.0.0
gym                0.22.0
gym_donkeycar      1.3.1
gym-notices        0.1.0
```

### システムPythonが綺麗か確認

```bash
python3.12 -m pip list --user | grep -E "gym|donkey"
```

期待される出力：（何も表示されない、または関連パッケージがない）

## 🚨 もしシステムが汚れたら

将来的に誤ってシステムPythonにインストールしてしまった場合：

```bash
# システムPythonからDonkey Car関連パッケージを削除
python3.12 -m pip uninstall -y donkeycar gym gym_donkeycar gym-notices gymnasium farama-notifications cloudpickle

# または、Python 3.13を使っている場合
python3.13 -m pip uninstall -y donkeycar gym gym_donkeycar gym-notices gymnasium farama-notifications cloudpickle
```

## 📝 なぜ仮想環境を使うのか

1. **システムの汚染を防ぐ** - システム全体に影響を与えない
2. **バージョン管理** - プロジェクトごとに異なるバージョンを使える
3. **再現性** - 他の環境でも同じ構成を再現できる
4. **安全性** - システムのPythonパッケージを壊さない
5. **削除が簡単** - 不要になったらenvフォルダを削除するだけ

## 💡 ベストプラクティス

### 常にスクリプトを使用

```bash
# ✅ 良い例
./start_drive.sh

# ❌ 悪い例
python manage.py drive  # どのPythonが使われるか不明確
```

### 新しいパッケージをインストールする時

```bash
# プロジェクトディレクトリに移動
cd /Users/yoshimurahiro/mysim

# 仮想環境のpipを使用
./env/bin/pip install <新しいパッケージ>
```

### 依存関係の記録（推奨）

```bash
# 現在インストールされているパッケージを記録
./env/bin/pip freeze > requirements.txt

# 後で同じ環境を再現
./env/bin/pip install -r requirements.txt
```

---

**✨ システムがクリーンになりました！**

今後は仮想環境を正しく使用して、システムを綺麗に保ちましょう。
