#!/bin/bash

# システム状態確認スクリプト
# 使い方: ./check_system.sh

echo "🔍 Donkey Car環境 - システム状態確認"
echo "=============================================="
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 1. 仮想環境の存在確認
echo "📁 1. 仮想環境の確認..."
if [ -d "${SCRIPT_DIR}/env" ]; then
    echo "   ✅ 仮想環境が存在します: ${SCRIPT_DIR}/env"
else
    echo "   ❌ 仮想環境が見つかりません"
    echo "      以下のコマンドで作成してください:"
    echo "      python3 -m venv env"
    echo "      ./env/bin/pip install -r requirements.txt"
    exit 1
fi

echo ""

# 2. 仮想環境内のパッケージ確認
echo "📦 2. 仮想環境内のDonkey Car関連パッケージ..."
VENV_PACKAGES=$("${SCRIPT_DIR}/env/bin/pip" list | grep -E "donkeycar|gym")
if [ -n "$VENV_PACKAGES" ]; then
    echo "$VENV_PACKAGES" | sed 's/^/   ✅ /'
else
    echo "   ❌ 必要なパッケージがインストールされていません"
    echo "      以下のコマンドでインストールしてください:"
    echo "      ./env/bin/pip install -r requirements.txt"
    exit 1
fi

echo ""

# 3. システムPythonの確認
echo "🧹 3. システムPython（グローバル環境）の確認..."
SYSTEM_PACKAGES=$(python3 -m pip list --user 2>/dev/null | grep -E "donkeycar|gym" || echo "")
if [ -z "$SYSTEM_PACKAGES" ]; then
    echo "   ✅ システムPythonはクリーンです（Donkey Car関連パッケージなし）"
else
    echo "   ⚠️  システムPythonに以下のパッケージが見つかりました:"
    echo "$SYSTEM_PACKAGES" | sed 's/^/      /'
    echo ""
    echo "   クリーンアップするには:"
    echo "   python3 -m pip uninstall -y donkeycar gym gym_donkeycar gym-notices gymnasium"
fi

echo ""

# 4. mycarディレクトリの確認
echo "🚗 4. mycarディレクトリの確認..."
if [ -d "${SCRIPT_DIR}/mycar" ]; then
    echo "   ✅ mycarディレクトリが存在します"
    
    # config.pyの確認
    if [ -f "${SCRIPT_DIR}/mycar/myconfig.py" ]; then
        echo "   ✅ myconfig.py が存在します"
    else
        echo "   ❌ myconfig.py が見つかりません"
    fi
    
    # dataディレクトリの確認
    if [ -d "${SCRIPT_DIR}/mycar/data" ]; then
        DATA_COUNT=$(find "${SCRIPT_DIR}/mycar/data" -type d -name "tub_*" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$DATA_COUNT" -gt 0 ]; then
            echo "   ✅ データフォルダ: ${DATA_COUNT}個のtubが存在します"
        else
            echo "   ℹ️  データフォルダは空です（まだデータ収集していません）"
        fi
    fi
    
    # modelsディレクトリの確認
    if [ -d "${SCRIPT_DIR}/mycar/models" ]; then
        MODEL_COUNT=$(find "${SCRIPT_DIR}/mycar/models" -name "*.h5" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$MODEL_COUNT" -gt 0 ]; then
            echo "   ✅ モデルフォルダ: ${MODEL_COUNT}個のモデルが存在します"
        else
            echo "   ℹ️  モデルフォルダは空です（まだ学習していません）"
        fi
    fi
else
    echo "   ❌ mycarディレクトリが見つかりません"
    echo "      以下のコマンドで作成してください:"
    echo "      ./env/bin/donkey createcar --path ./mycar"
    exit 1
fi

echo ""

# 5. スクリプトの実行権限確認
echo "🔧 5. 実行スクリプトの確認..."
SCRIPTS=("start_drive.sh" "train_model.sh" "start_autopilot.sh")
ALL_EXECUTABLE=true

for script in "${SCRIPTS[@]}"; do
    if [ -f "${SCRIPT_DIR}/${script}" ]; then
        if [ -x "${SCRIPT_DIR}/${script}" ]; then
            echo "   ✅ ${script} (実行可能)"
        else
            echo "   ⚠️  ${script} (実行権限なし)"
            ALL_EXECUTABLE=false
        fi
    else
        echo "   ❌ ${script} が見つかりません"
        ALL_EXECUTABLE=false
    fi
done

if [ "$ALL_EXECUTABLE" = false ]; then
    echo ""
    echo "   実行権限を付与するには:"
    echo "   chmod +x *.sh"
fi

echo ""
echo "=============================================="
echo "✨ システム状態確認が完了しました"
echo ""

# 6. 推奨事項
echo "💡 次のステップ:"
echo ""
if [ "$DATA_COUNT" -eq 0 ]; then
    echo "   1. シミュレーターをダウンロード"
    echo "      https://github.com/tawnkramer/gym-donkeycar/releases"
    echo "   2. 手動運転でデータを収集"
    echo "      ./start_drive.sh"
elif [ "$MODEL_COUNT" -eq 0 ]; then
    echo "   1. AIモデルを学習"
    echo "      ./train_model.sh"
else
    echo "   1. 自動運転を試す"
    echo "      ./start_autopilot.sh"
fi

echo ""
echo "📖 詳細なガイド:"
echo "   - README.md: セットアップと使い方"
echo "   - SIMULATOR_GUIDE.md: シミュレーター起動方法"
echo "   - CLEANUP_GUIDE.md: システムクリーンアップ"
echo "   - GETTING_STARTED.md: クイックスタート"
