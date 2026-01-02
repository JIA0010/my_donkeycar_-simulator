#!/bin/bash

# シミュレーター環境切り替えスクリプト

echo "======================================"
echo "Donkey Car シミュレーター環境切り替え"
echo "======================================"
echo ""
echo "利用可能な環境:"
echo "1. donkey-warehouse-v0 (倉庫 - シンプル)"
echo "2. donkey-generated-roads-v0 (道路環境)"
echo "3. donkey-generated-track-v0 (自動生成トラック)"
echo "4. donkey-avc-sparkfun-v0 (SparkFun AVCコース)"
echo ""
read -p "環境を選択してください (1-4): " choice

case $choice in
    1)
        ENV_NAME="donkey-warehouse-v0"
        ENV_DESC="倉庫環境（シンプル）"
        ;;
    2)
        ENV_NAME="donkey-generated-roads-v0"
        ENV_DESC="道路環境"
        ;;
    3)
        ENV_NAME="donkey-generated-track-v0"
        ENV_DESC="自動生成トラック"
        ;;
    4)
        ENV_NAME="donkey-avc-sparkfun-v0"
        ENV_DESC="SparkFun AVCコース"
        ;;
    *)
        echo "無効な選択です"
        exit 1
        ;;
esac

echo ""
echo "環境を ${ENV_DESC} (${ENV_NAME}) に変更します..."

# myconfig.pyのバックアップ
cp mycar/myconfig.py mycar/myconfig.py.backup

# 環境名を置換
sed -i '' "s/DONKEY_GYM_ENV_NAME = \".*\"/DONKEY_GYM_ENV_NAME = \"${ENV_NAME}\"/" mycar/myconfig.py

echo "✅ 環境が ${ENV_DESC} に変更されました！"
echo ""
echo "シミュレーターを起動するには:"
echo "  ./start_drive.sh"
echo ""
echo "または手動で:"
echo "  source env/bin/activate"
echo "  python mycar/manage.py drive"
