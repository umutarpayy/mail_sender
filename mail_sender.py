import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# E-posta gönderme işlevi
def send_email(subject, body, to_email):
    from_email = "umutozturkarpay99@gmail.com"
    password = "xbhy bjaj qumv tzgc"

    # E-posta oluştur
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # E-posta gönder
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"E-posta gönderimi başarısız oldu: {e}")

# Eşik değerler ve bayraklar
thresholds = [50000, 100000, 200000, 250000, 300000]
flags = {threshold: False for threshold in thresholds}

# Txt dosyasını kontrol eden işlev
def check_counter(file_path):
    try:
        with open(file_path, 'r') as file:
            counter = int(file.read().strip())
            return counter
    except Exception as e:
        print(f"Dosya okunurken hata oluştu: {e}")
        return None

# Sürekli kontrol döngüsü
def monitor_counter(file_path, to_email):
    while True:
        counter = check_counter(gifile_path)
        if counter is not None:
            for threshold in thresholds:
                if counter >= threshold and not flags[threshold]:
                    subject = f"EŞİK AŞILDI: {threshold}"
                    body = f"İstek sayısı {threshold} sayısını aştı. Şu anki istek sayısı: {counter}."
                    send_email(subject, body, to_email)
                    flags[threshold] = True  # Mail atıldı, bir daha atılmaması için bayrak işaretlendi
        time.sleep(3600)  # 1 saat bekle

if __name__ == "__main__":
    file_path = sys.argv[1]  # İstek sayısını tuttuğunuz txt dosyası
    to_email = "imparkmailadresi@gmail.com"  # Mail gönderilecek adres
    monitor_counter(file_path, to_email)
