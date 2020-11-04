How to start the Django server

```
python3 manage.py runserver
```

how to build a new app

```
python3 manage.py startapp __new__app__name___
```

How to app to store data and mapping the data to the database

In a app you can got to the models.py and create a model ie:

```
from django.db import models

class Product(models.Model):
  title = models.TextField()
  description = models.TextField()
  price = models.TextField()
```

Then go to the projcts main folder and add the App to the INSTALLED_APPS section

# Migrations
next migrate is migration work , any time you make a change to models.py we need to make a migration

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

How to create a super user and sign into the application admin pannels

```
 python3 manage.py createsuperuser

```

Using a model in the shell

```
python3 manage.py shell
```

# Example Creating a product in the Shell

```
from products.models import Product
```

```
Product.objects.create(title="Newer Products", price=129.66, summary="What is this awesome thing)
```
