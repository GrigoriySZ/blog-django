1. Создать проект
```
django-admin startproject blog
```

2. Переход в папку 
```
cd blog
```

3. Добавляем приложения
```
python manage.py startapp post
python manage.py startapp userAcc
python manage.py startapp userProfile
```

4. Добавляем в GIT
```
git init
pip freeze > requirements.txt
git add .
git commit -m "chore: Initial project"
git branch -M main
git remote add origin {GIT_URL}
git push -u origin main
```

5. Создаем ветку develop и ветку разработки
```
git checkout -b develop
git push origin develop
git checkout -b feature/blog-basic
```

6. Создаем поля в модели Post и пушим в GIT

7. Создаем файл миграции для модели Post и сохраням в GIT
```
python manage.py makemigrations
git add . 
git commit -m "feat: create migrations Post model"
```

8. Настраиваем админку для Post

9. Проводим миграцию после создания админки
```
python manage.py migrate
```

10. Создаем суперпользователя
```
python manage.py createsuperuser
```

11. Запускаем сервер и останавливаем сервер после проверки
```
python manage.py runserver
Ctrl+C 
```

12. Сохраняем регистрацию модели Post в панели администратора
```
git add .
git commit -m "feat: register Post in admin panel"
```

