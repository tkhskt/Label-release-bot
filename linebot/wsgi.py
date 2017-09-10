"""
WSGI config for linebot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import threading
import requests
import time

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "linebot.settings")

application = get_wsgi_application()

def awake():
    while True:
        try:
            print("Awaking Start!")
            requests.get("http://releasenotification.herokuapp.com/calendar/")
            print("End!")
        except:
            print("awaking error")
            pass
        time.sleep(300)

t = threading.Thread(target=awake)
t.start()