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
* `admin/` - панель администратора / admin panel
* `api/articles/` - списов всех статей в кратком виде / list of all articles in short form
* `api/articles/(заголовок статьи/title of article)` - просмотр опеределеной статьи / viewing a specific article
* `api/articles/entries/(часть заголовка/title part)` - список всех статей, где содержатся введеные символы / list of all articles containing the entered characters
* `api/auth/` - список url для работы с пользователями / url list for working with users [больше/more](https://djoser.readthedocs.io/en/latest/base_endpoints.html)
* `api/token/` - список url для работы с JWT / url list for working with JWT [больше/more](https://djoser.readthedocs.io/en/latest/jwt_endpoints.html)

### Как запустить проект / How to use

---
* Скопируйте файл `.env.temp` в файл `.env` и заполните поля.
* Copy the `.env.temp` file to the `.env` file and fill in the fields.

* Запустите сервис базы данных
* Run servise data base
```
docker-compose up -d db
```

* Выполните миграции
* Make migrations
```
docker-compose run app python manage.py migrate
```

* (Опцианально) Запонем базу данными данными для примера
* (Optional) Populate the database with sample data
```
docker-compose run app python manage.py loaddata db.json
```

* Создадим суперпользователя (администратора)
* Create a cuperuser (admin)
```
docker-compose run app python manage.py createsuperuser
```

* Запустить приложение в фоновом режиме
* Run app in background
```
docker-compose up -d app
```

* Остановить приложение
* Stop app
```
docker-compose stop
```

[вверх](#top)
