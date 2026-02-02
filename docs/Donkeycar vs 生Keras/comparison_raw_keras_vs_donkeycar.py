"""
Donkeycar vs 生Keras: コード量と複雑度の比較

このファイルでは、Donkeycarを使った場合と、
TensorFlow/Kerasを直接使った場合の比較を示します。
"""

# =============================================================================
# 【1】Donkeycarを使った場合（あなたが今やっていること）
# =============================================================================

# ■ データ収集 → ブラウザで手動運転するだけ（コード0行）

# ■ 学習 → たった1コマンド
# $ donkey train --tub ./data --model ./models/mypilot.h5

# ■ 自動運転 → 1コマンド
# $ python manage.py drive --model ./models/mypilot.h5

# 合計: 実質 0行のコード！


# =============================================================================
# 【2】生のTensorFlow/Kerasで同じことをする場合
# =============================================================================

"""
最低限必要なコード: 約200-300行
"""

import os
import glob
import json
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, Input
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split

# --------------------------------------------------------
# ステップ1: データの読み込み（約50行）
# --------------------------------------------------------
def load_data_from_tub(tub_path):
    """
    Donkeycarのtubデータを読み込む
    この関数だけで50行以上のコードが必要
    """
    images = []
    steering_angles = []
    throttles = []
    
    # manifest.jsonを読み込む
    manifest_path = os.path.join(tub_path, 'manifest.json')
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")
    
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    # カタログファイルを読み込む
    for catalog_file in sorted(glob.glob(os.path.join(tub_path, 'catalog_*.catalog'))):
        with open(catalog_file, 'r') as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    
                    # 画像パスを取得
                    if 'cam/image_array' in record:
                        img_filename = record['cam/image_array']
                        img_path = os.path.join(tub_path, 'images', img_filename)
                        
                        # 画像を読み込む
                        if os.path.exists(img_path):
                            img = Image.open(img_path)
                            img_array = np.array(img)
                            images.append(img_array)
                            
                            # ステアリングとスロットルを取得
                            steering = record.get('user/angle', 0.0)
                            throttle = record.get('user/throttle', 0.0)
                            steering_angles.append(steering)
                            throttles.append(throttle)
    
    return np.array(images), np.array(steering_angles), np.array(throttles)


# --------------------------------------------------------
# ステップ2: データの前処理（約30行）
# --------------------------------------------------------
def preprocess_data(images, steering_angles, throttles, target_size=(120, 160)):
    """
    画像のリサイズと正規化
    """
    processed_images = []
    
    for img in images:
        # リサイズ
        img_pil = Image.fromarray(img)
        img_resized = img_pil.resize((target_size[1], target_size[0]))
        img_array = np.array(img_resized)
        
        # 正規化 (0-255 → 0.0-1.0)
        img_normalized = img_array.astype(np.float32) / 255.0
        processed_images.append(img_normalized)
    
    X = np.array(processed_images)
    y_steering = np.array(steering_angles).reshape(-1, 1)
    y_throttle = np.array(throttles).reshape(-1, 1)
    
    return X, y_steering, y_throttle


# --------------------------------------------------------
# ステップ3: モデルの構築（約40行）
# --------------------------------------------------------
def build_model(input_shape=(120, 160, 3)):
    """
    CNNモデルの構築
    Donkeycarと同じアーキテクチャ
    """
    drop = 0.2
    
    # 入力層
    img_in = Input(shape=input_shape, name='img_in')
    
    # CNN層（畳み込み層）
    x = Conv2D(24, (5, 5), strides=(2, 2), activation='relu', name='conv2d_1')(img_in)
    x = Dropout(drop)(x)
    x = Conv2D(32, (5, 5), strides=(2, 2), activation='relu', name='conv2d_2')(x)
    x = Dropout(drop)(x)
    x = Conv2D(64, (5, 5), strides=(2, 2), activation='relu', name='conv2d_3')(x)
    x = Dropout(drop)(x)
    x = Conv2D(64, (3, 3), strides=(1, 1), activation='relu', name='conv2d_4')(x)
    x = Dropout(drop)(x)
    x = Conv2D(64, (3, 3), strides=(1, 1), activation='relu', name='conv2d_5')(x)
    x = Dropout(drop)(x)
    
    # 平坦化
    x = Flatten(name='flattened')(x)
    
    # 全結合層
    x = Dense(100, activation='relu', name='dense_1')(x)
    x = Dropout(drop)(x)
    x = Dense(50, activation='relu', name='dense_2')(x)
    x = Dropout(drop)(x)
    
    # 出力層（ステアリングとスロットル）
    steering_out = Dense(1, activation='linear', name='steering')(x)
    throttle_out = Dense(1, activation='linear', name='throttle')(x)
    
    # モデルの作成
    model = Model(
        inputs=[img_in],
        outputs=[steering_out, throttle_out],
        name='autopilot_model'
    )
    
    return model


# --------------------------------------------------------
# ステップ4: 学習の実行（約40行）
# --------------------------------------------------------
def train_model(model, X_train, y_steering_train, y_throttle_train,
                X_val, y_steering_val, y_throttle_val,
                model_path='./models/my_model.h5',
                epochs=100, batch_size=32):
    """
    モデルの学習
    """
    # コンパイル
    model.compile(
        optimizer='adam',
        loss={
            'steering': 'mse',
            'throttle': 'mse'
        },
        metrics={
            'steering': ['mae'],
            'throttle': ['mae']
        }
    )
    
    # コールバックの設定
    callbacks = [
        EarlyStopping(
            monitor='val_loss',
            patience=5,
            min_delta=0.0005,
            verbose=1
        ),
        ModelCheckpoint(
            filepath=model_path,
            monitor='val_loss',
            save_best_only=True,
            verbose=1
        )
    ]
    
    # 学習の実行
    history = model.fit(
        X_train,
        {'steering': y_steering_train, 'throttle': y_throttle_train},
        validation_data=(
            X_val,
            {'steering': y_steering_val, 'throttle': y_throttle_val}
        ),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=1
    )
    
    return history


# --------------------------------------------------------
# ステップ5: 推論（予測）（約20行）
# --------------------------------------------------------
def predict(model, image_path):
    """
    単一画像から予測
    """
    # 画像の読み込み
    img = Image.open(image_path)
    img_resized = img.resize((160, 120))
    img_array = np.array(img_resized).astype(np.float32) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)  # バッチ次元を追加
    
    # 予測
    steering, throttle = model.predict(img_batch)
    
    return steering[0][0], throttle[0][0]


# --------------------------------------------------------
# メイン処理（約30行）
# --------------------------------------------------------
def main():
    """
    すべてを統合するメイン関数
    """
    # 1. データの読み込み
    print("Loading data from tub...")
    images, steering_angles, throttles = load_data_from_tub('./data')
    
    # 2. データの前処理
    print("Preprocessing data...")
    X, y_steering, y_throttle = preprocess_data(images, steering_angles, throttles)
    
    # 3. 訓練データと検証データに分割
    print("Splitting data...")
    indices = np.arange(len(X))
    train_idx, val_idx = train_test_split(indices, test_size=0.2, random_state=42)
    
    X_train, X_val = X[train_idx], X[val_idx]
    y_steering_train, y_steering_val = y_steering[train_idx], y_steering[val_idx]
    y_throttle_train, y_throttle_val = y_throttle[train_idx], y_throttle[val_idx]
    
    print(f"Training samples: {len(X_train)}")
    print(f"Validation samples: {len(X_val)}")
    
    # 4. モデルの構築
    print("Building model...")
    model = build_model()
    model.summary()
    
    # 5. 学習の実行
    print("Training model...")
    history = train_model(
        model,
        X_train, y_steering_train, y_throttle_train,
        X_val, y_steering_val, y_throttle_val,
        model_path='./models/my_custom_model.h5',
        epochs=100,
        batch_size=32
    )
    
    print("Training completed!")
    print(f"Model saved to ./models/my_custom_model.h5")
    
    # 6. 予測の例
    # steering, throttle = predict(model, './data/images/0_cam_image_array_.jpg')
    # print(f"Predicted - Steering: {steering:.3f}, Throttle: {throttle:.3f}")


if __name__ == '__main__':
    main()


# =============================================================================
# 【3】コード量の比較まとめ
# =============================================================================

"""
┌─────────────────────────────────────────────────────────────────┐
│                    コード量と難易度の比較                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  【Donkeycar使用】                                               │
│    - コード量: 0行（コマンド2つだけ）                             │
│    - 難易度: ★☆☆☆☆ (初心者でも可能)                            │
│    - 開発時間: 5分                                               │
│    - 必要な知識:                                                 │
│      ✓ コマンドラインの基本                                      │
│      ✓ ブラウザでの操作                                         │
│                                                                 │
│  【生Keras使用】                                                │
│    - コード量: 約250-300行                                       │
│    - 難易度: ★★★★☆ (中級～上級者向け)                         │
│    - 開発時間: 2-3日                                            │
│    - 必要な知識:                                                 │
│      ✓ Python プログラミング                                    │
│      ✓ NumPy, TensorFlow/Keras                                 │
│      ✓ データ処理（JSON, 画像）                                 │
│      ✓ CNNの基礎知識                                            │
│      ✓ 機械学習のワークフロー                                    │
│      ✓ デバッグとトラブルシューティング                           │
│                                                                 │
│  【さらに実用的にする場合（+100-200行）】                         │
│    ✓ データ拡張（Data Augmentation）                            │
│    ✓ リアルタイム推論システム                                    │
│    ✓ ログとモニタリング                                         │
│    ✓ ハイパーパラメータのチューニング                             │
│    ✓ エラーハンドリング                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
"""


# =============================================================================
# 【4】一般的な画像認識タスクの場合
# =============================================================================

"""
例: 犬と猫を分類するモデル（シンプルな例）

【最小限のコード】約50-80行

from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds

# データセット読み込み（TensorFlow Datasetsを使用）
(train_ds, val_ds), info = tfds.load(
    'cats_vs_dogs',
    split=['train[:80%]', 'train[80%:]'],
    with_info=True,
    as_supervised=True
)

# データ前処理
def preprocess(image, label):
    image = tf.image.resize(image, (160, 160))
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

train_ds = train_ds.map(preprocess).batch(32).prefetch(1)
val_ds = val_ds.map(preprocess).batch(32).prefetch(1)

# モデル構築
model = keras.Sequential([
    layers.Conv2D(32, 3, activation='relu', input_shape=(160, 160, 3)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(128, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='softmax')  # 犬 or 猫
])

# コンパイル
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 学習
model.fit(train_ds, validation_data=val_ds, epochs=10)

# 保存
model.save('cat_dog_classifier.h5')
"""

"""
【実用的なコード】約200-500行

上記に加えて:
- カスタムデータローダー（自分の画像を使う場合）
- データ拡張（回転、反転、明るさ調整など）
- 転移学習（VGG16, ResNet等の事前学習済みモデル使用）
- 学習の可視化（グラフ作成）
- ハイパーパラメータチューニング
- 推論用のAPIまたはWebアプリ
"""


# =============================================================================
# 【5】結論: Donkeycarの価値
# =============================================================================

"""
Donkeycarが素晴らしい理由:

1. 【抽象化レベルが高い】
   - データ収集、学習、推論のパイプラインが完全に統合
   - 細かい実装を気にせず、「自動運転」という目的に集中できる

2. 【ベストプラクティスが組み込み済み】
   - モデルアーキテクチャが最適化済み
   - データ拡張、Early Stopping、モデル保存などが自動

3. 【実機との連携が簡単】
   - Raspberry Pi、カメラ、モーター制御が統合
   - シミュレーターと実機で同じコードが動く

4. 【教育価値が高い】
   - 機械学習の全体像を体験できる
   - 段階的に深く学べる（まず使う→中身を理解→カスタマイズ）


生Kerasで書く場合:
✓ 完全な制御が可能
✓ 細かいカスタマイズができる
✓ 深い理解が得られる
✗ 時間がかかる（2-3日 vs 5分）
✗ バグが入りやすい
✗ 実機連携を自分で実装する必要がある


結論: 
Donkeycarは「機械学習の民主化」の素晴らしい例です。
まずDonkeycarで体験→興味が湧いたら中身を理解→さらに深く学ぶ
という流れが最も効果的な学習方法です！
"""
