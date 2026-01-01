# Donkey Car シミュレーター環境

PC上でDonkey Carのシミュレーターを使用して自動運転を体験できる環境です。実機（Raspberry Pi）がなくても、**手動走行でデータ収集** → **学習（AIモデル作成）** → **自動運転** の一連の流れを体験できます。

> 📚 **すべてのドキュメント一覧は [INDEX.md](INDEX.md) を参照してください**  
> 🚨 **エラーが出た場合は [QUICK_REFERENCE.md](QUICK_REFERENCE.md) を参照してください**

## 📋 目次

- [環境構築済み](#環境構築済み)
- [シミュレーターのダウンロード](#シミュレーターのダウンロード)
- [使い方](#使い方)
- [トラブルシューティング](#トラブルシューティング)

## ✅ 環境構築済み

このプロジェクトでは以下がセットアップ済みです：

- ✅ Python仮想環境 (`env/`)
- ✅ Donkey Car v5.0.0 インストール済み
- ✅ シミュレーター用の設定ファイル (`mycar/myconfig.py`)
- ✅ データ保存ディレクトリ (`mycar/data/`)
- ✅ モデル保存ディレクトリ (`mycar/models/`)

## 🎮 シミュレーターのダウンロード

Unityベースのシミュレーターをダウンロードします。

### macOS の場合

1. [Donkey Gym Releases](https://github.com/tawnkramer/gym-donkeycar/releases) にアクセス
2. 最新リリースから **`DonkeySimMac.zip`** または **`DonkeySimMacGL.zip`** をダウンロード
3. ダウンロードしたファイルを解凍
4. 解凍したアプリ（`donkey_sim.app`）を任意の場所に配置

### Windows の場合

1. [Donkey Gym Releases](https://github.com/tawnkramer/gym-donkeycar/releases) にアクセス
2. 最新リリースから **`DonkeySimWin.zip`** をダウンロード
3. ダウンロードしたファイルを解凍
4. 解凍したフォルダを任意の場所に配置

### Linux の場合

1. [Donkey Gym Releases](https://github.com/tawnkramer/gym-donkeycar/releases) にアクセス
2. 最新リリースから **`DonkeySimLinux.zip`** をダウンロード
3. ダウンロードしたファイルを解凍
4. 実行権限を付与: `chmod +x donkey_sim.x86_64`

## 🚗 使い方

### 1. 仮想環境の有効化

```bash
# プロジェクトディレクトリに移動
cd /Users/yoshimurahiro/mysim

# 仮想環境を有効化
source env/bin/activate  # macOS/Linux
# または
# .\env\Scripts\activate  # Windows
```

### 2. シミュレーターの起動

ダウンロードしたシミュレーターアプリを起動します。

- **macOS**: `donkey_sim.app` をダブルクリック
- **Windows**: `donkey_sim.exe` をダブルクリック
- **Linux**: `./donkey_sim.x86_64`

#### シミュレーター起動画面の操作：

シミュレーターが起動すると設定画面が表示されます：

1. **Scene（シーン選択）**
   - `Generated Track` を選択（壁付きトラック、初心者向け）
   - または `Generated Road`（開けた道路）
   - 他にも `Warehouse`, `Sparkfun AVC` などがあります

2. **Graphics Quality（グラフィック品質）**
   - `Fantastic`, `Beautiful`, `Good`, `Fast`, `Fastest` から選択
   - PCの性能に合わせて選択してください（`Good`または`Fast`を推奨）

3. **Port（ポート番号）**
   - デフォルトの `9091` のままでOK

4. **起動**
   - 設定が完了したら、ウィンドウを閉じるか、そのまま待つとシミュレーターが起動します
   - **「Play!」ボタンはありません** - 設定が完了すると自動的にシミュレーターが開始されます
   - 3Dの道路が表示されればOKです

### 3. 手動走行とデータ収集

#### Python側から接続

```bash
cd mycar
python manage.py drive
```

正常に起動すると以下のメッセージが表示されます：
```
loading config file: /path/to/mycar/myconfig.py
Opening http://localhost:8887
```

#### Webブラウザでコントロール

1. ブラウザで `http://localhost:8887` を開く
2. 画面に表示される操作パネルまたはキーボードで車を操作
   - **矢印キー**: ステアリング（左右）とスロットル（上下）
   - **i**: スロットル増加
   - **k**: スロットル減少
   - **j**: 左旋回
   - **l**: 右旋回
3. 上手く走れるようになったら、**Start Recording** ボタンをクリック
4. コースを数周走行してデータを収集
5. **Stop Recording** ボタンでデータ収集を停止

データは `mycar/data/` ディレクトリ内の `tub_XX_YY-MM-DD` フォルダに保存されます。

### 4. AIモデルの学習（Training）

十分なデータ（最低でも1000枚以上の画像を推奨）を収集したら、学習を行います。

```bash
# ドライブモードを終了 (Ctrl+C)

# 学習を実行
donkey train --tub ./data --model ./models/mypilot.h5
```
<!-- 引数の解析: --tub（データの場所）、--model（保存する名前）、--config（設定ファイル）などのオプションを解析します。 -->

学習には数分から数十分かかります（データ量とPCの性能による）。

### 5. 自動運転（Autopilot）

学習したモデルを使用して自動運転を試します。

```bash
# シミュレーターが起動していることを確認

# モデルを指定してドライブモードを起動
python manage.py drive --model ./models/mypilot.h5
```

ブラウザ（`http://localhost:8887`）で以下の操作：
1. **Mode** を `Local Pilot` または `Autopilot` に切り替え
2. 車が自動で走り出します！

うまく走らない場合は、より多くのデータを収集して再学習してください。

## 🛠️ トラブルシューティング

### シミュレーターに接続できない

- シミュレーターが起動していることを確認
- `myconfig.py` で `DONKEY_GYM = True` になっていることを確認
- ファイアウォールでポート通信がブロックされていないか確認

### 学習時にエラーが出る

```bash
# TensorFlowを追加インストール
pip install tensorflow
```

### データが保存されない

- Webインターフェースで「Start Recording」ボタンを押していることを確認
- `mycar/data/` ディレクトリの権限を確認

### Python 3.13で動かない場合

**重要**: Python 3.13は現在TensorFlow 2.20しかサポートしておらず、Donkeycar 5.0.0とは互換性がありません。**Python 3.9-3.11を使用してください**。

```bash
# Python 3.11で新しい仮想環境を作成
python3.11 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### エラー例
```
AttributeError: 'Functional' object has no attribute 'input_names'
```
このエラーが出た場合、Python 3.13を使用している可能性があります。上記の手順でPython 3.11の環境を作り直してください。

## 📚 参考リンク

- [Donkey Car 公式ドキュメント](https://docs.donkeycar.com/)
- [Donkey Gym GitHub](https://github.com/tawnkramer/gym-donkeycar)
- [Donkey Car フォーラム](https://discord.gg/donkeycar)

## ⚠️ 重要: 仮想環境の使用

このプロジェクトでは**必ず仮想環境**を使用してください。

### ✅ 正しい使い方

```bash
# スクリプトを使用（推奨）
./start_drive.sh
./train_model.sh
./start_autopilot.sh

# または、仮想環境のPythonを直接使用
/Users/yoshimurahiro/mysim/env/bin/python manage.py drive
```

### ❌ やってはいけないこと

```bash
# システムのpipを使用しない
pip install donkeycar
pip3 install gym-donkeycar
sudo pip install ...  # 絶対にNG
```

詳細は `CLEANUP_GUIDE.md` を参照してください。

## 🔄 環境の再構築

もし環境を作り直す必要がある場合：

```bash
# 古い仮想環境を削除
rm -rf env

# 新しい仮想環境を作成
python3 -m venv env

# 依存関係をインストール
./env/bin/pip install -r requirements.txt

# gym-donkeycarを再インストール
./env/bin/pip install git+https://github.com/tawnkramer/gym-donkeycar
```

## 📝 設定ファイル

主要な設定は `mycar/myconfig.py` に記載されています：

- `DONKEY_GYM = True`: シミュレーターモードを有効化
- `DONKEY_GYM_ENV_NAME`: コース選択
  - `"donkey-generated-track-v0"`: 壁付きトラック（推奨）
  - `"donkey-generated-roads-v0"`: 開けた道路
  - `"donkey-warehouse-v0"`: 倉庫内コース
  - `"donkey-avc-sparkfun-v0"`: SparkFun AVCコース

設定を変更した場合は、`manage.py drive` を再起動してください。

## 🎯 次のステップ

1. より多くのデータを収集して学習精度を向上
2. 異なるコースで学習と走行を試す
3. モデルのパラメータ調整（`myconfig.py`）
4. 実機（Raspberry Pi + Donkey Car）での実装に挑戦！

Happy Racing! 🏁
