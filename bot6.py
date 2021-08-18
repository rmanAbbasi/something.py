import time
import schedule
import cv2
import random
from pyrogram import Client
from pyrogram.raw import functions
from datetime import datetime

app = Client(
	'myapp',
	api_id=7918017,
	api_hash='f3804f0880757bb29d9c5a510f57131d'
)


def job():
    now_h = datetime.now().strftime('%H')
    now_m = datetime.now().strftime('%M')
    image = cv2.imread('download.png')
    cv2.putText(image, f'{now_h}:{now_m}', (150, 280),
    cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 5)
    n = random.randint(0, 100000000000000000)
    cv2.imwrite(f"pic/picfile_{n}.png", image)
    with app:
        app.send(
            functions.account.UpdateProfile(
                about=f"{now_h}:{now_m}"
            )
        )
        app.set_profile_photo(photo=f'pic/picfile_{n}.png')
        print('Changed !')


schedule.every().minute.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
