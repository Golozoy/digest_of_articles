<a id='top'></a>
## Digest of articles / Сборник статей
### About / О приложении

---
Возможности приложения. Все записи разделены на две категории `is_public = True` и `is_public = False`. Просмотрeть список всех записей могут все пользователи. Записи выдаются по 10 штук на страницу. Не авторизованые пользователи могут получить полный доступ только к публичным статьям. Авторизованые пользователи могут получить доступ ко всем статьям. Добавлять и редоктировать статьи может только администратор. В приложении придусмотрена возможможность рагистрации и авторизации пользователей. Аутентификация осуществляется при помощи JWT.

---
Application capabilities. All entries are divided into two categories `is_public = True` and `is_public = False`. View a list of all system entries of all users. Entries are issued 10 per page. Unauthorized users can only get full access to public articles. Authorized users can access all articles. Only the administrator can add and edit an article. The application provides for the possible registration and authorization of users. Authentication is done using JWT.

---

### Список url / list url

---
`admin/` - панель администратора / admin panel\n
`api/articles/` - списов всех статей в кратком виде / list of all articles in short form\n
`api/articles/(заголовок статьи/title of article)` - просмотр опеределеной статьи / viewing a specific article\n
`api/auth/` - список url для работы с пользователями / url list for working with users [больше/more](https://djoser.readthedocs.io/en/latest/base_endpoints.html)\n
`api/token/` - список url для работы с JWT / url list for working with JWT [больше/more](https://djoser.readthedocs.io/en/latest/jwt_endpoints.html)\n

### Как запустить проект / How to use

---
Скопируйте файл `.env.temp` в файл `.env` и заполните поля.\n
Copy the `.env.temp` file to the `.env` file and fill in the fields.\n

Запустите сервис базы данных\n
Run servise data base\n
```
docker-compose up -d db
```

Выполните миграции\n
Make migrations\n
```
docker-compose run app python manage.py migrate
```

(Опцианально) Запонем базу данными данными для примера\n
(Optional) Populate the database with sample data\n
```
docker-compose run app python manage.py loaddata db.json
```

Создадим суперпользователя (администратора)\n
Create a cuperuser (admin)\n
```
docker-compose run app python manage.py createsuperuser
```

Запустить приложение в фоновом режиме\n
Run app in background\n
```
docker-compose up -d app
```

Остановить приложение\n
Stop app\n
```
docker-compose stop
```

[вверх](#top)
