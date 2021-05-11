from bs4 import BeautifulSoup
import requests

url = "https://status.ecwid.com/"
page = requests.get(url)

# проверяем сайт на доступность
if page.status_code == 200:
    print("Сайт доступен!")

soup = BeautifulSoup(page.text, "html.parser")

# Дергаем все теги с подходящим описанием сервиса
allServices = soup.findAll('span', class_='name')
allStatus = soup.findAll('span', class_='component-status')

# Создаем 2 списка(массива) для очистки сырых данных полученых ранее
filteredServices = []
filteredStatus = []

# Чистим данные от пробелов и лишних символов и добавляем их в список(массив)
for data in allServices:
    filteredServices.append("".join(data.text.split()))


for data in allStatus:
    filteredStatus.append("".join(data.text.split()))


# testStatus = ["Operational", "Operational","Bad","Bad", "Operational", "Operational" ] #- тестовый набор

# Объединяем 2 списка в словарь
resultStatus = dict(zip(filteredServices, filteredStatus))


for key, value in resultStatus.items():
    if value == "Operational":
        print(f"status OK {key}")
    else:
        print(f"status FILED {key}")
