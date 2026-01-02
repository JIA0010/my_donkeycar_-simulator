"""
My CAR CONFIG

This file is read by your car application's manage.py script to change the car
performance. This configuration is set up for simulator mode.
"""

import os

#PATHS
CAR_PATH = PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(CAR_PATH, 'data')
MODELS_PATH = os.path.join(CAR_PATH, 'models')

#VEHICLE
DRIVE_LOOP_HZ = 20
MAX_LOOPS = None

#CAMERA
IMAGE_W = 160
IMAGE_H = 120
IMAGE_DEPTH = 3

# SIMULATOR SETTINGS
DONKEY_GYM = True
# カスタムビルド（CustomRedWallTrack）を使う場合はパスを指定
DONKEY_SIM_PATH = "/Users/yoshimurahiro/Desktop/DonkeySimCustom/DonkeySimCustom.app"
# DONKEY_SIM_PATH = "remote"  # リモートシミュレーターの場合
# シンプルな環境を試す: warehouse, generated-roads, generated-track, avc-sparkfun
# - donkey-warehouse-v0: 倉庫環境（シンプル、制御しやすい）
# - donkey-generated-roads-v0: 道路環境
# - donkey-generated-track-v0: 自動生成トラック（デフォルト）
# - donkey-avc-sparkfun-v0: SparkFun AVCコース
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"  # 組み込み環境名（カスタムビルドでは無視される）

GYM_CONF = {
    "body_style": "donkey",
    "body_rgb": (128, 128, 128),
    "car_name": "mycar",
    "font_size": 100
}
GYM_CONF["racer_name"] = "Your Name"
GYM_CONF["country"] = "Japan"
GYM_CONF["bio"] = "Learning autonomous driving!"

SIM_HOST = "127.0.0.1"
SIM_ARTIFICIAL_LATENCY = 0

# Save info from Simulator
SIM_RECORD_LOCATION = False
SIM_RECORD_GYROACCEL = False
SIM_RECORD_VELOCITY = False
SIM_RECORD_LIDAR = False

# JOYSTICK
USE_JOYSTICK_AS_DEFAULT = False
JOYSTICK_MAX_THROTTLE = 1.0
JOYSTICK_STEERING_SCALE = 1.0
JOYSTICK_DEADZONE = 0.01

# TRAINING - 性能向上のための最適化
BATCH_SIZE = 128
TRAIN_TEST_SPLIT = 0.8
MAX_EPOCHS = 150  # エポック数を増やして学習を深める
SHOW_PLOT = True
VERBOSE_TRAIN = True
USE_EARLY_STOP = True
EARLY_STOP_PATIENCE = 10  # より多くのエポックを待つ
MIN_DELTA = 0.0005
PRINT_MODEL_SUMMARY = True

# MODEL
DEFAULT_MODEL_TYPE = 'linear'
OPTIMIZER = "adam"
LEARNING_RATE = 0.001
LEARNING_RATE_DECAY = 0.0

# AUGMENTATION
AUGMENTATIONS = []

# WEB CONTROL
WEB_CONTROL_PORT = 8887
WEB_INIT_MODE = "user"

# TELEMETRY
HAVE_CONSOLE_PRINTING = True
TELEMETRY_DONKEY_NAME = "mycar"
