# 🏁 Donkey Car シミュレーター - カスタムコース作成ガイド

## 概要

Donkey Carシミュレーターでは、複数の方法でカスタムコースを作成・使用できます。

---

## 方法1: Built-in Scenes（組み込みシーン）

### 利用可能なシーン

すぐに使えるプリセットシーン：

| シーン名 | 特徴 | 難易度 | 推奨用途 |
|---------|------|--------|---------|
| `Generated Track` | ランダム生成壁付きトラック | ⭐ 易しい | 初心者の練習 |
| `Generated Road` | 開けた道路 | ⭐⭐ 中級 | 自由走行の学習 |
| `Warehouse` | 倉庫内コース | ⭐⭐ 中級 | 屋内環境の学習 |
| `Sparkfun AVC` | 実際の競技会場を再現 | ⭐⭐⭐ 上級 | 大会準備 |
| `Mountain Track` | 山道コース | ⭐⭐⭐ 上級 | 複雑な環境 |

### 使い方

`myconfig.py` で環境名を変更：

```python
# Generated Track（推奨）
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"

# Generated Road
DONKEY_GYM_ENV_NAME = "donkey-generated-roads-v0"

# Warehouse
DONKEY_GYM_ENV_NAME = "donkey-warehouse-v0"

# Sparkfun AVC
DONKEY_GYM_ENV_NAME = "donkey-avc-sparkfun-v0"

# Mountain Track
DONKEY_GYM_ENV_NAME = "donkey-mountain-track-v0"
```

---

## 方法2: Unity Track Editor（完全カスタム）

### 必要なもの

- **Unity 2019.4 LTS 以降**（無料版でOK）
- **sdsandbox**（シミュレーターのソースコード）
- 基本的な3D編集スキル

### セットアップ手順

#### 1. sdsandboxをクローン

```bash
cd ~/projects
git clone https://github.com/tawnkramer/sdsandbox.git
cd sdsandbox
```

#### 2. Unityで開く

1. Unity Hubを起動
2. "Add" → sdsandboxフォルダを選択
3. プロジェクトを開く

#### 3. Scene Builderを使う

1. `Assets/Scenes/` フォルダを開く
2. 既存のシーンを複製
3. トラックを編集：
   - 道路セグメントの配置
   - 壁の追加/削除
   - テクスチャの変更
   - ライティングの調整

#### 4. カスタムシーンをビルド

1. File → Build Settings
2. シーンをビルドリストに追加
3. Build（Mac/Windows/Linux用）

#### 5. Donkey Carで使用

```python
# myconfig.py
DONKEY_SIM_PATH = "/path/to/your/custom_build"
DONKEY_GYM_ENV_NAME = "donkey-your-custom-scene-v0"
```

---

## 方法3: Procedural Generation（手続き的生成）

### Generated Trackの仕組み

`Generated Track`は起動時に**ランダムに**コースを生成します。

#### パラメータ調整（高度）

シミュレーター内部のスクリプトを編集することで、生成ルールを変更可能：

- トラックの長さ
- カーブの頻度
- 壁の高さ
- 道幅

**注意**: これにはUnityプロジェクトの編集が必要です。

---

## 方法4: 既存コミュニティのトラック

### Donkey Carコミュニティ

他のユーザーが作成したトラックをダウンロード：

- [Donkey Car Discord](https://discord.com/invite/PN6kFgY)
- [GitHub Discussions](https://github.com/autorope/donkeycar/discussions)
- [r/donkeycar](https://www.reddit.com/r/donkeycar/)

### インストール方法

1. `.unitypackage` または ビルド済みファイルをダウンロード
2. Unityプロジェクトにインポート
3. ビルド
4. `DONKEY_SIM_PATH` で指定

---

## 推奨ワークフロー

### 初心者向け

```
1. Generated Track で基本を学ぶ
   ↓
2. 他のBuilt-in Scenesを試す
   ↓
3. コミュニティのトラックを試す
   ↓
4. Unity Editor でカスタマイズ
```

### 上級者向け

```
1. Unity で完全オリジナルトラックを作成
   ↓
2. 複数の環境でテスト
   ↓
3. コミュニティで共有
```

---

## トラック作成のベストプラクティス

### 1. シンプルから始める

❌ 最初から複雑なコース  
✅ シンプルなループから開始

### 2. 段階的な難易度

- 最初：広い直線 + ゆるいカーブ
- 中級：狭い道 + 急カーブ
- 上級：障害物 + 複雑な交差点

### 3. テクスチャのバリエーション

- 路面のテクスチャを変化させる
- 環境の多様性（昼/夜、天候など）
- リアルな環境に近づける

### 4. パフォーマンス考慮

- ポリゴン数を抑える
- ライティングを最適化
- 不要なオブジェクトを削除

---

## トラブルシューティング

### Q: カスタムシーンが認識されない

```bash
# 環境名を確認
python -c "import gym; import gym_donkeycar; print(gym_donkeycar.envs.ENVS)"

# シミュレーターのログを確認
# シミュレーター起動時のコンソール出力をチェック
```

### Q: Unityプロジェクトが開けない

- Unity 2019.4 LTS 以降を使用
- 必要なパッケージをインストール
- プロジェクトの互換性を確認

### Q: ビルドに失敗する

- ターゲットプラットフォームを確認
- エラーログを読む
- 不要なアセットを削除

---

## 参考リンク

- [Donkey Car 公式ドキュメント](https://docs.donkeycar.com/)
- [sdsandbox GitHub](https://github.com/tawnkramer/sdsandbox)
- [Unity Learn](https://learn.unity.com/)
- [Donkey Car Discord](https://discord.com/invite/PN6kFgY)

---

## まとめ

| 方法 | 難易度 | カスタマイズ性 | 時間 |
|-----|-------|-------------|-----|
| Built-in Scenes | ⭐ | 低 | 0分 |
| Unity Editor | ⭐⭐⭐ | 高 | 数時間〜数日 |
| Procedural | ⭐⭐⭐⭐ | 中 | 数日 |
| コミュニティ | ⭐ | 中 | 数分 |

**推奨**: まずはBuilt-in Scenesで練習し、必要に応じてUnity Editorでカスタマイズ！

---

**Happy Track Building! 🏁**
