from django.test import TestCase
import requests

a = requests.get(url="http://45.142.36.22:4812/ut3/hs/radius_bot/", auth=("django_admin", "DJango_96547456"), params={"list": 'a52'})

print(a.json().values())
