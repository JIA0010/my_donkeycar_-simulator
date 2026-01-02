# カスタムコース作成ガイド

## 概要
赤い壁と黒い道のシンプルなコースを作成してDonkey Carの性能を向上させる方法

## 方法1: 既存シーンの変更（推奨）

### 利用可能なシーン
現在使用可能なビルトインシーンを試してみましょう:

1. **donkey-warehouse-v0** - 倉庫環境（シンプルな環境）
2. **donkey-generated-roads-v0** - 道路環境
3. **donkey-generated-track-v0** - 自動生成トラック（現在使用中）
4. **donkey-avc-sparkfun-v0** - SparkFun AVCコース

### シーン変更方法

`mycar/myconfig.py`を編集:

```python
# 倉庫環境を試す（シンプルでコントロールしやすい）
DONKEY_GYM_ENV_NAME = "donkey-warehouse-v0"
```

または

```python
# 道路環境を試す
DONKEY_GYM_ENV_NAME = "donkey-generated-roads-v0"
```

## 方法2: Unityで完全カスタムコース作成

### 必要なもの
- Unity Hub (最新版)
- Unity 2020.3 LTS以降
- Git
- Donkey Simulator のソースコード

### ステップ1: Donkey Simulatorのソースを取得

```bash
cd ~/Desktop
git clone https://github.com/tawnkramer/sdsandbox
cd sdsandbox
```

### ステップ2: Unityでプロジェクトを開く

1. Unity Hubを起動
2. 「Open」→ `sdsandbox/sdsim` フォルダを選択
3. プロジェクトが開くのを待つ

### ステップ3: カスタムシーンの作成

#### 新しいシーンを作成
1. `Assets/Scenes/` で右クリック → Create → Scene
2. 新しいシーンに名前をつける（例: `CustomRedWallTrack`）

#### 黒い道を作成
1. GameObject → 3D Object → Plane を作成
2. Materialを作成:
   - Project → Assets → 右クリック → Create → Material
   - 名前: `BlackRoad`
   - Albedo カラーを黒 (0, 0, 0) に設定
3. Planeにマテリアルを適用
4. Planeをスケール・配置して道路を形成

#### 赤い壁を作成
1. GameObject → 3D Object → Cube を作成
2. Materialを作成:
   - 名前: `RedWall`
   - Albedo カラーを赤 (255, 0, 0) に設定
3. Cubeをスケール (例: x=0.2, y=2, z=10) して壁を作成
4. 複製して道路の両側に配置

#### Donkey Car Prefabを追加
1. `Assets/Scripts/donkey/` から車のPrefabをシーンにドラッグ
2. スタート地点に配置

### ステップ4: ビルド

1. File → Build Settings
2. 「Add Open Scenes」をクリック
3. プラットフォームを選択（Mac → Mac、Windows → PC）
4. 「Build」をクリック
5. 保存先を選択（例: `~/Desktop/CustomSimulator`）

### ステップ5: カスタムシミュレーターを使用

`mycar/myconfig.py`を編集:

```python
DONKEY_GYM = True
DONKEY_SIM_PATH = "/Users/yoshimurahiro/Desktop/CustomSimulator/donkey_sim.app"  # Macの場合
# DONKEY_SIM_PATH = "/Users/yoshimurahiro/Desktop/CustomSimulator/donkey_sim.exe"  # Windowsの場合
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"  # カスタムシーンの場合も同じ
```

## 方法3: 既存コースのパラメータ調整（最も簡単）

シミュレーターのGYM_CONFで環境を調整:

```python
GYM_CONF = {
    "body_style": "donkey",
    "body_rgb": (128, 128, 128),
    "car_name": "mycar",
    "font_size": 100,
    # 追加のパラメータ
    "cam_resolution": (160, 120),
    "max_cte": 5.0,  # コースからの最大距離
}
```

## 性能向上のためのヒント

### 1. データ収集の改善
- 様々な走行パターンのデータを収集
- 滑らかで一貫した運転
- エッジケース（カーブ、コーナー）を多く収集

### 2. モデルの改善
```python
# mycar/myconfig.py
BATCH_SIZE = 128
MAX_EPOCHS = 150  # エポック数を増やす
LEARNING_RATE = 0.0001  # 学習率を調整
```

### 3. 画像処理の最適化
- コントラストを上げる
- 適切なクロッピング
- データ拡張（AUGMENTATIONS）を使用

### 4. より高度なモデルタイプ
```python
DEFAULT_MODEL_TYPE = 'linear'  # または 'categorical', 'rnn', 'imu', 'latent'
```

## トラブルシューティング

### シミュレーターが起動しない
- Unityビルド時にすべての依存関係が含まれているか確認
- パスが正しいか確認

### 接続エラー
```python
SIM_HOST = "127.0.0.1"  # ローカルで実行する場合
```

### 性能が悪い
1. より多くのデータを収集（最低1000-2000フレーム）
2. データの品質を確認
3. 異なるモデルアーキテクチャを試す

## 次のステップ

1. まず既存のシーンを試してみる
2. データを大量に収集
3. モデルをトレーニング
4. 性能を評価
5. 必要に応じてカスタムコース作成を検討

## 参考リンク

- [Donkey Simulator GitHub](https://github.com/tawnkramer/sdsandbox)
- [Donkey Car Documentation](https://docs.donkeycar.com/)
- [Unity 学習リソース](https://learn.unity.com/)
