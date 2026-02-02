#!/bin/bash

# Donkey Car シミュレーター 学習スクリプト
# 使い方: ./train_model.sh

echo "🎓 Donkey Car - AIモデル学習"
echo "=============================================="
echo ""

# スクリプトのディレクトリを取得
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${SCRIPT_DIR}/mycar"

# データディレクトリの確認
if [ ! -d "data" ] || [ -z "$(ls -A data)" ]; then
    echo "❌ エラー: データが見つかりません"
    echo "   先に手動走行でデータを収集してください"
    echo "   ./start_drive.sh を実行してデータを収集してください"
    exit 1
fi

echo "📊 収集済みデータ:"
ls -lh data/

echo ""
echo "🚀 学習を開始します..."
echo "   モデルは ./models/mypilot.h5 に保存されます"
echo "   学習には数分から数十分かかる場合があります"
echo ""

# 仮想環境のPythonを直接使用して学習を実行
"${SCRIPT_DIR}/env/bin/donkey" train --tub ./data --model ./models/mypilot.h5

echo ""
echo "✅ 学習が完了しました！"
echo "   自動運転を試すには: ./start_autopilot.sh"
