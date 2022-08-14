<h2 align="center">MovieCatalog</h2>


### Описание проекта:
Небльшой каталог фильмов

### Инструменты разработки

**Стек:**
- Python = 3.9
- Django = 4.0.6
- sqlite3

## Запуск проекта

##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение
    
    venv/Scripts/activate

##### 4) Устанавливить зависимости:

    pip install -r requirements.txt

##### 5) Перейти в папку с проектом

    cd .\MovieCatalog\
    
##### 6) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 7) Создать суперпользователя

    python manage.py createsuperuser
    
##### 8) Запустить сервер

    python manage.py runserver