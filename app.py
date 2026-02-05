from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import requests

app = Flask(__name__)

# ================= EMAIL CONFIG =================
EMAIL_ADDRESS = "manojnehra556@gmail.com"      # your email
EMAIL_PASSWORD = "YOUR_APP_PASSWORD_HERE"     # Gmail App Password

# ================= WHATSAPP CONFIG =================
WHATSAPP_PHONE = "919772237618"  # your number with country code

def send_email(name, phone, message):
    msg = EmailMessage()
    msg['Subject'] = "🔥 New Website Inquiry"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    msg.set_content(f"""
New Inquiry Received

Name: {name}
Phone: {phone}
Message: {message}
""")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def send_whatsapp(name, phone, message):
    text = f"New Inquiry%0AName: {name}%0APhone: {phone}%0AMessage: {message}"
    url = f"https://wa.me/{WHATSAPP_PHONE}?text={text}"
    requests.get(url)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        message = request.form.get("message")

        send_email(name, phone, message)
        send_whatsapp(name, phone, message)

    return render_template("index.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        message = request.form.get("message")

        send_email(name, phone, message)
        send_whatsapp(name, phone, message)

    return render_template("contact.html")

if __name__ == "__main__":
    app.run()