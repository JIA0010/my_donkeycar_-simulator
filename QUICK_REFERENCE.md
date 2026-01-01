# よくあるエラーと解決方法 - クイックリファレンス

このドキュメントは、Donkey Carシミュレーター環境構築時によく発生するエラーの**即座の解決方法**をまとめたものです。

詳細な技術解説は `TECHNICAL_ISSUES.md` を参照してください。

---

## 🔥 緊急度: 高

### ❌ エラー: `ModuleNotFoundError: No module named 'pkg_resources'`

**解決方法**:
```bash
./env/bin/pip install setuptools
```

**原因**: Python 3.13でsetuptoolsがデフォルトで含まれていない

---

### ❌ エラー: `AttributeError: module 'collections' has no attribute 'MutableMapping'`

**解決方法**:
```bash
./env/bin/pip install --upgrade tornado
```

**原因**: 古いTornadoバージョンがPython 3.10+と非互換

---

### ❌ エラー: `gym.error.NameNotFound: Environment donkey-generated-track doesn't exist`

**解決方法**:
```bash
./env/bin/pip uninstall -y gym gym-donkeycar
./env/bin/pip install git+https://github.com/tawnkramer/gym-donkeycar
```

**原因**: PyPI版が古く、GitHubの最新版が必要

---

### ❌ エラー: `ModuleNotFoundError: No module named 'gym'`

**解決方法**:
```bash
./env/bin/pip install gym-donkeycar
```

**原因**: gym-donkeycarパッケージが未インストール

---

### ❌ エラー: `SyntaxError: unterminated string literal`

**解決方法**:
```bash
# myconfig.pyを削除して再作成
rm mycar/myconfig.py

# テンプレートをコピー（存在する場合）
cp myconfig.py.backup mycar/myconfig.py

# または手動で作成
nano mycar/myconfig.py
```

**確認**:
```bash
python3 -m py_compile mycar/myconfig.py
```

---

## ⚠️ 緊急度: 中

### ❌ エラー: `zsh: command not found: python`

**解決方法**:
```bash
# 仮想環境のPythonをフルパスで使用
/Users/yoshimurahiro/mysim/env/bin/python manage.py drive
```

**または**:
```bash
# スクリプトを使用
./start_drive.sh
```

**原因**: 仮想環境が有効化されていない

---

### ❌ エラー: `source: no such file or directory: env/bin/activate`

**解決方法**:
```bash
# カレントディレクトリを確認
pwd

# プロジェクトディレクトリに移動
cd /Users/yoshimurahiro/mysim

# 仮想環境を有効化
source env/bin/activate
```

**原因**: 間違ったディレクトリで実行している

---

### ⚠️ 警告: `Defaulting to user installation because normal site-packages is not writeable`

**これは問題です！システムが汚染されます**

**クリーンアップ**:
```bash
# システムPythonから削除
python3 -m pip uninstall -y donkeycar gym gym_donkeycar gym-notices gymnasium farama-notifications cloudpickle

# 今後は仮想環境のpipを使用
/Users/yoshimurahiro/mysim/env/bin/pip install <パッケージ名>
```

---

## ℹ️ 緊急度: 低（警告のみ）

### ⚠️ 警告: `Gym has been unmaintained since 2022...`

**対処**: 無視してOK（現時点では動作に問題なし）

**将来的な対応**:
```bash
# Gymnasiumへの移行（まだ必要ではない）
./env/bin/pip uninstall gym
./env/bin/pip install gymnasium
```

---

### ⚠️ 警告: `Box bound precision lowered by casting to float32`

**対処**: 無視してOK（NumPyの精度に関する警告）

---

## 🔍 トラブルシューティングフローチャート

```
起動できない？
    │
    ├─ YES → エラーメッセージは？
    │         │
    │         ├─ ModuleNotFoundError → 上記の解決方法を参照
    │         ├─ AttributeError → Tornadoアップグレード
    │         ├─ SyntaxError → myconfig.py再作成
    │         └─ その他 → ./check_system.sh を実行
    │
    └─ NO → シミュレーターに接続できない？
              │
              ├─ YES → シミュレーター起動確認
              │         ポート9091が開いているか確認
              │         lsof -i :9091
              │
              └─ NO → データ収集/学習/自動運転の問題？
                        GETTING_STARTED.md を参照
```

---

## 🛠️ 基本的な診断コマンド

### システム状態の確認
```bash
./check_system.sh
```

### Pythonバージョン確認
```bash
python3 --version
./env/bin/python --version
```

### パッケージ確認
```bash
# 仮想環境内
./env/bin/pip list | grep -E "donkey|gym"

# システムPython（これは空であるべき）
python3 -m pip list --user | grep -E "donkey|gym"
```

### 設定ファイル確認
```bash
# 構文チェック
python3 -m py_compile mycar/myconfig.py

# シミュレーター設定確認
grep -E "DONKEY_GYM|SIM_HOST" mycar/myconfig.py
```

### ポート確認
```bash
# Webサーバー（8887）
lsof -i :8887

# シミュレーター（9091）
lsof -i :9091
```

---

## 🚑 緊急リセット手順

**すべてが壊れた場合の完全リセット**:

```bash
# 1. プロジェクトディレクトリに移動
cd /Users/yoshimurahiro/mysim

# 2. 仮想環境を削除
rm -rf env

# 3. システムPythonをクリーンアップ
python3 -m pip uninstall -y donkeycar gym gym_donkeycar gym-notices gymnasium

# 4. 仮想環境を再作成
python3 -m venv env

# 5. 依存関係を再インストール
./env/bin/pip install --upgrade pip
./env/bin/pip install setuptools
./env/bin/pip install donkeycar
./env/bin/pip install git+https://github.com/tawnkramer/gym-donkeycar

# 6. mycarが存在しない場合は作成
./env/bin/donkey createcar --path ./mycar

# 7. myconfig.pyを編集
nano mycar/myconfig.py
# DONKEY_GYM = True を設定

# 8. 動作確認
./env/bin/python mycar/manage.py drive
```

---

## 📋 環境確認チェックリスト

起動前に以下を確認：

- [ ] Python 3.9-3.11を使用している（3.13は非推奨）
- [ ] 仮想環境が存在する (`ls env/`)
- [ ] システムPythonがクリーンである
- [ ] myconfig.pyにシンタックスエラーがない
- [ ] シミュレーターがダウンロード済み
- [ ] シミュレーターアプリが起動している
- [ ] ポート9091と8887が空いている

---

## 🎯 よくある質問

### Q: どのPythonバージョンを使うべき？
**A**: Python 3.9、3.10、3.11のいずれかを推奨。3.13は避ける。

### Q: pip install時に"Defaulting to user installation"と表示される
**A**: 仮想環境が有効化されていません。`./env/bin/pip` を使用してください。

### Q: シミュレーターに接続できない
**A**: 
1. シミュレーターアプリが起動しているか確認
2. myconfig.pyで `DONKEY_GYM = True` になっているか確認
3. ポート9091が他のプロセスに使われていないか確認

### Q: "Play!"ボタンが見つからない
**A**: 新しいバージョンでは設定完了後に自動的に起動します。「Play!」ボタンは不要です。

### Q: データ収集はできるが学習でエラーになる
**A**: TensorFlowが必要です:
```bash
./env/bin/pip install tensorflow
```

---

## 🔗 関連ドキュメント

| ドキュメント | 用途 |
|------------|------|
| **TECHNICAL_ISSUES.md** | 詳細な技術解説と根本原因 |
| **CLEANUP_GUIDE.md** | システムクリーンアップ方法 |
| **README.md** | 全体的なセットアップガイド |
| **GETTING_STARTED.md** | クイックスタートガイド |
| **SIMULATOR_GUIDE.md** | シミュレーター起動方法 |

---

## 💡 プロからのヒント

### ヒント1: エラーメッセージを読む
最後の3-5行を注意深く読めば、ほとんどの問題は解決できます。

### ヒント2: フルパスを使う
```bash
# ❌ これは避ける
python manage.py drive

# ✅ これを使う
./env/bin/python manage.py drive
```

### ヒント3: バックアップを取る
```bash
cp mycar/myconfig.py mycar/myconfig.py.backup
```

### ヒント4: 段階的に進める
一度にすべてインストールせず、1つずつ確認しながら進める。

### ヒント5: ログを保存
```bash
./start_drive.sh 2>&1 | tee drive.log
```

---

**🆘 それでも解決しない場合**:

1. `./check_system.sh` を実行
2. エラーメッセージ全体をコピー
3. `TECHNICAL_ISSUES.md` で詳細を確認
4. Donkey Car公式フォーラムで質問

**最終更新**: 2026年1月1日
