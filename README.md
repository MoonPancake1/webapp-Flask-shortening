# Устройство для укорочения ссылок

Устройство для укорочения ссылок, можете сделать свою ссылку короткой

## Описание
Устройство для укорочения ссылок созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro.

## Технологии
* Python
* Flask
* WTForms
* SQLAlchemy

## Как запустить

1. Склонируйте репозиторий

2. Создайте и активируйте виртаульное окружение
```commandline
python -m venv venv
source venv/Scripts/activate # for Windows
source venv/bin/activate # for Mac/Unix
```

3. Установите зависимости
```commandline
pip install -r requirements.txt
```

4. Создайте файл .env и укажите настройки подключения к БД и другие параметры.
```commandline
DATABASE_URL=sqlite:///urls.db
SECRET_KEY=YOUR_SECRET_KEY
```

5. Запустите flask приложение
```commandline
flask run
```

## Автор
Чернышев Владислав