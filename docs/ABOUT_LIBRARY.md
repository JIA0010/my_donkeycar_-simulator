# 📚 Donkey Car ライブラリ

**←  [ドキュメント一覧に戻る](INDEX.md)**

## 📍 場所

```
env/lib/python3.11/site-packages/donkeycar/
```

**確認コマンド**:
```bash
source env/bin/activate
python -c "import donkeycar; print(donkeycar.__file__)"
```

---

## 📦 バージョン・基本情報

| 項目 | 値 |
|------|-----|
| **バージョン** | 5.0.0 |
| **Python** | 3.11 |
| **TensorFlow** | 2.15 |
| **Gym** | 0.22 + gym-donkeycar 1.3.1 |

---

## 🗂️ 主要モジュール

```
donkeycar/
├── 🚗 vehicle.py          ← メイン：Vehicle クラス（パーツ組み合わせ）
├── 🔧 parts/              ← 60+ パーツ（カメラ、コントローラー、アクチュエーター等）
├── 📊 pipeline/           ← 学習・推論処理
├── 🎮 gym/                ← シミュレーター環境
├── 🛠️ utilities/          ← ユーティリティ関数
└── ...
```

---

## 🚀 このプロジェクトでの使われ方

### manage.py（ドライブモード）

```python
import donkeycar as dk
from donkeycar.vehicle import Vehicle

cfg = dk.load_config(myconfig=args['--myconfig'])
V = Vehicle()
V.add(camera, outputs=['cam/image_array'])
V.add(pilot, inputs=['cam/image_array'], outputs=['angle', 'throttle'])
V.start(rate_hz=20)
```

### train.py（学習）

```python
from donkeycar.pipeline.training import train

train(cfg, tubs=['data/tub_1'], model='models/mypilot.h5')
```

---

## 🔧 主要クラス

| クラス | 役割 |
|--------|------|
| **Vehicle** | パーツを登録・実行するフレームワーク |
| **LocalWebController** | ブラウザUI（このプロジェクト使用）|
| **train** | モデル学習関数 |
| **DonkeyGymEnv** | シミュレーター環境 |

---

## 🔗 参照リンク

- 🎯 **[プロジェクト概要](ABOUT_PROJECT.md)** ← プロジェクトの目的と流れ
- 🚀 **[クイックスタート](QUICKSTART.md)** ← 5分で実行開始
- 🆘 **[トラブル解決](QUICK_REFERENCE.md)** ← エラー対応
- 📖 **[公式ドキュメント](https://docs.donkeycar.com)** ← 詳細情報

**モジュール設計。必要なパーツだけを組み合わせてカスタマイズ可能です。** 🏗️
