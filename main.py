import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# 配置信息
WHATSAPP_TARGET = "+254796963059"

@app.route('/wix-lead', methods=['POST'])
def handle_wix_lead():
    """1. Wix 访客留言自动推送"""
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    message = data.get('message')
    
    # 逻辑：调用 WhatsApp 发送接口
    log_msg = f"新客户通知: {name}, 电话: {phone}, 留言: {message}"
    print(f"发送推送至 {WHATSAPP_TARGET}: {log_msg}")
    
    # 这里集成您的 WhatsApp API 发送代码
    return jsonify({"status": "success", "sent_to": WHATSAPP_TARGET}), 200

@app.route('/payment-reminder', methods=['POST'])
def payment_reminder():
    """2. 付款计划提醒逻辑 (由 Google Sheets 触发)"""
    # 对应文档: 1Iy4Uo4RvMGWVhAhMM-CB7Bvlnslv4GHsNCTLiBDToX8
    data = request.json
    buyer = data.get('buyer')
    days_left = data.get('days_left')
    
    # 提醒规则：14, 10, 7, 5, 3, 2, 0 天
    if days_left in [14, 10, 7, 5, 3, 2, 0]:
        msg = f"付款提醒: 买家 {buyer} 还有 {days_left} 天到期，请及时跟进。"
        # 发送逻辑...
    elif days_left < 0:
        msg = f"逾期警告: 买家 {buyer} 已逾期 {abs(days_left)} 天！"
        
    return jsonify({"status": "processed"}), 200

@app.route('/daily-report-trigger', methods=['POST'])
def daily_report():
    """3. 日报汇总提醒 (由系统定时器触发)"""
    # 对应文档: 1LrlGfTHlcOGAJP8bfOy3BxQJ-BBqTrdoV7xgNzNJueo
    current_hour = datetime.now().hour
    
    if current_hour in [17, 19]:
        return jsonify({"action": "remind_sales", "msg": "请及时提交日报"}), 200
    elif current_hour == 21:
        return jsonify({"action": "auto_summarize", "msg": "开始汇总接访/收款/成交分析"}), 200
    
    return jsonify({"status": "idle"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)
