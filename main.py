import os
import sys
from flask import Flask, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

@app.route('/')
def home():
    """根路径欢迎页面"""
    return {
        "status": "online",
        "message": "OpenClaw Sales Bot is Running!",
        "project": "Sabaki Green Estate Management",
        "region": "Kenya/Nairobi"
    }

@app.route('/health')
def health_check():
    """健康检查接口"""
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # 获取 Hugging Face 分配的端口，默认为 7860
    try:
        port = int(os.environ.get("PORT", 7860))
        print(f"--- Starting Sales Bot on port {port} ---")
        # 允许外部访问
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"Critical Error during startup: {e}")
        sys.exit(1)
