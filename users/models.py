from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

# py manage.py makemigrations <application>

#  1) Изменение моделей
#  2) Создание миграции
#  3) Применение миграции

# py manage.py migrate <application> <migration_name> - использование конкретной миграции в конкретном приложении
# py manage.py migrate - применение всех миграций во всех приложениях

# py manage.py makemigrations <application> - создание миграции в конкретном приложении
# py manage.py makemigrations - создание миграции во всех приложениях


#  CRUD - create, read, update, delete
