import requests
import smtplib
from email.message import EmailMessage

# APIキーと複数都市リスト
API_KEY = 'あなたのAPIキー'
CITIES = ['Yokohama', 'Tokyo']

# iCloudメール設定
EMAIL_ADDRESS = "あなたの@icloud.com"
EMAIL_PASSWORD = "アプリ用パスワード"
TO_EMAIL = "送信先のメールアドレス"

# メール本文を組み立てる
weather_report = ""

for city in CITIES:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ja"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        weather_report += f"{city}：{weather}（{temp}℃）\n"
    else:
        weather_report += f"{city}：天気取得失敗\n"

# メールの件名・本文
subject = "今日の天気レポート（複数都市）"
body = f"以下は今日の天気です：\n\n{weather_report}"

msg = EmailMessage()
msg["Subject"] = subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL
msg.set_content(body)

# メール送信
with smtplib.SMTP_SSL("smtp.mail.me.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("送信完了")
