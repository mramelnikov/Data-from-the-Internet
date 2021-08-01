#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного
# пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json

url = 'https://api.github.com'
user = 'mramelnikov'
try:
    r = requests.get(f'{url}/users/{user}/repos')
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

repos = r.json()
report = []
for item_r in repos:
    report.append(item_r["name"])

print(f'Список репозиториев пользователя {user}')
print(report)
with open('repos.json', 'w') as f:
    json.dump(report, f)


# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию через curl, Postman, Python.
# Ответ сервера записать в файл (приложить скриншот для Postman и curl)

url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://developers.google.com"
token = 'AIzaSyCeynS8ILY1aoJp9ajabptGj_V_UboDTCk'
header = {
    'Content-Type': 'application/json',
    'Authorization': token
}

try:
    r = requests.get(f'{url}', headers = header)
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

repos = r.json()
report = []

with open('PageSpeed_Insights.json', 'w') as f:
    json.dump(repos, f)
