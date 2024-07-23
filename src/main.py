import requests
import re
import csv
import io
from db import MarketData, SessionLocal
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
                    handlers=[
                        logging.FileHandler('app.log'),  # Запись логов в файл
                        logging.StreamHandler()  # Вывод логов на консоль
                    ])

url = 'https://cloud.mail.ru/public/L1xB/nvgHGYJz5'


def get_direct_link_from_mail_cloud_url(link):
    try:
        response = requests.get(link)
        response.raise_for_status()  # Проверка на успешный запрос (200 OK)
        page_content = response.text

        re_pattern = r'dispatcher.*?weblink_get.*?url":"(.*?)"'
        match = re.search(re_pattern, page_content)

        if match:
            url = match.group(1)
            parts = link.split('/')[-2:]
            url = f'{url}/{parts[0]}/{parts[1]}'
            return url
    except requests.RequestException as e:
        logging.error(f"Ошибка при запросе ссылки: {e}")

    return None


def import_csv_to_db(direct_link):
    if not direct_link:
        logging.error("Недоступная ссылка")
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

        session = SessionLocal()
        flag = True
        for row in csv_reader:
            if flag:
                flag = False
                continue
            try:
                data = MarketData(
                    ticker=row[0],
                    period=row[1],
                    date=row[2],
                    time=row[3],
                    open=float(row[4]),
                    high=float(row[5]),
                    low=float(row[6]),
                    close=float(row[7]),
                    volume=int(row[8])
                )
                session.add(data)
                session.commit()
            except Exception as e:
                logging.error(f"Ошибка при обработке строки: {e}")
                session.rollback()
                continue
        logging.info("CSV файл успешно записан.")

    except requests.RequestException as e:
        logging.error(f"Ошибка при запросе CSV файла: {e}")
    except IOError as e:
        logging.error(f"Ошибка при обработке CSV файла: {e}")
    finally:
        if session:
            session.close()


direct_link = get_direct_link_from_mail_cloud_url(url)
logging.info(f"Ссылка для скачивания: {direct_link}")

import_csv_to_db(direct_link)