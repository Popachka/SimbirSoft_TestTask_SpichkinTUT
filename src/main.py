import requests
import re
import csv
import io

url = 'https://cloud.mail.ru/public/L1xB/nvgHGYJz5'


def get_direct_link_from_mail_cloud_url(link):
    response = requests.get(link)
    page_content = response.text

    re_pattern = r'dispatcher.*?weblink_get.*?url":"(.*?)"'
    match = re.search(re_pattern, page_content)

    if match:
        url = match.group(1)
        parts = link.split('/')[-2:]
        url = f'{url}/{parts[0]}/{parts[1]}'
        return url

    return None


direct_link = get_direct_link_from_mail_cloud_url(url)
print(f"Ссылка для скачивания: {direct_link}")


def fetch_and_save_csv(direct_link):
    if not direct_link:
        print("Недоступная ссылка")
        return

    try:
        response = requests.get(direct_link)
        response.raise_for_status()  # Проверка на успешный запрос (200 OK)

        # Преобразуем байты в строку
        content_str = response.content.decode('utf-8')

        # Используем StringIO для работы со строкой как с файлом
        csv_file = io.StringIO(content_str)

        # Читаем CSV данные
        csv_reader = csv.reader(csv_file, delimiter=';')

        with open('C:\MyFiles\Projects\SimbirSoft\src\output.csv', 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f, delimiter=',')  # Используем ',' для CSV
            for row in csv_reader:
                csv_writer.writerow(row)

        print("CSV файл успешно записан.")

    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except IOError as e:
        print(f"Ошибка при записи файла: {e}")


fetch_and_save_csv(direct_link)
