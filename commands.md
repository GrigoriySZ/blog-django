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
git remote add {GIT_URL}
git push -u origin main
```