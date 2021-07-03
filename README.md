# online_shop

## Download

1. У вас должен быть установлен python3
2. Пишем в терминале: `git clone git@github.com:Akylbek005/online_shop.git`
3. Заходим в папку online_shop `cd online_shop`
4. Создаем виртуальное окружение `python3 -m venv venv`
5. Активируем виртуальное окржунение `source venv/vin/activate`
6. Скачиваем библиотеки `pip install -r requirements.txt`
7. Заходим в `config/settings` и изменим `DATABASE{...}` на`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}`
8. Сделаем миграции `python manage.py migrate`
9. Запустим проэкт `python magage.py runserver`
10. Заходим по [ссылке](127.0.0.1:8000)

