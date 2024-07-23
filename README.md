

## Стэк технологий
- ⚡ [**Python3**](https://www.python.org/) Как основа для всего
    - 🧰 [SQLalchemy](https://docs.sqlalchemy.org/en/20/) для удобного подключения к бд и быстрой, эффективной работой с таблицами и записями через ORM.
    - 🔍 [Pydantic](https://docs.pydantic.dev) для управления настройками через `.env` файлы.
    - 💾 [PostgreSQL](https://www.postgresql.org) наша СУБД.
- 🐋 [Docker Compose](https://www.docker.com) Для развертывания приложения.
- 🐘 [PGAdmin]() UI-инструмент для работы с базой данных.


### Гайд по запуску.

- Сначала клонируйте репозиторий на свой локальный компьютер:

```bash
git clonehttps://github.com/Popachka/SimbirSoft_TestTask_SpichkinTUT.git
cd SimbirSoft_TestTask_SpichkinTUT
```

- Создайте виртуальное окружение в папке проекта:

```bash
python -m venv venv
```
- Активация виртуального окружения

```bash
cd venv\Scripts
activate
```
- На macOS и Linux

```bash
source venv/bin/activate
```

- Откройте и ознакомьтесь с начальными параметрами(пароли, юзеры и тд) в `.env`:

- Сборка контейнеров

Соберите Docker-контейнеры:

```bash
docker-compose build
```

- Запуск контейнеров

Запустите Docker-контейнеры:

```bash
docker-compose up
```

### Как работает все

- Когда вы запускаете Docker-контейнеры. Сначала запускается контейнер с базой данной, а затем отрабатывает скрипт.
Наш скрипт обращается по адресу `https://cloud.mail.ru/public/L1xB/nvgHGYJz5`, парсит страницу и ищет другую ссылку, уже в которой находится файл.
После того, как он его находит, все записи добавляются в уже запущенную базу данных. 

### Дополнительное:
- Логирование осуществляется через модуль `logging`.
- Ошибки обрабатываются с помощью `try`/`except`.
- Для доступа к `PGAdmin` используйте URL `http://localhost:5050/`. При создании подключения в поле "Host name/address" укажите db (имя контейнера базы данных).