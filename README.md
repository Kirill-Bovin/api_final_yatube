# **Проект «API для Yatube»**

### **Описание**
Через запросы API будут доступны посты, комментарии, подписчики и группы. Для аутентификации используються JWT-токены.

### **Как запустить проект:**
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://git@github.com:Kirill-Bovin/api_final_yatube.git
```
Перейти в репозиторий с проектом:
```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source env/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Перейти в репозиторий yatube:
```
cd yatube_api
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
К API есть документация по адресу http://localhost:8000/redoc/

### Примеры запросов:
+ Получение и создание публикаций
```
/api/v1/posts/      методы: GET, POST
```
+ Получение отдельной публикации, ее редактирование
```
/api/v1/posts/{id}/    методы: GET, PUT, PATCH, DEL
```
+ Получение и создание комментариев к публикации
```
/api/v1/posts/{post_id}/comments/    методы: GET, POST
```

### Автор:
Студент Яндекс.практикум: Бовин Кирилл Викторович.

### Технологии:
Django, Django REST, API.
