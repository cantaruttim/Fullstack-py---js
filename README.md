# Step-by-Step

1. django-admin startproject name_of_your_project
2. cd name_of_your_project then
   2.1 django-admin startapp api
3. On views.py on our api app, create our endpoints
   3.1 cd api > make urls.py
   3.2 we will point our endpoint on urls.py inside our api directory
4. Make migrations with python .\manage.py makemigrations and then python .\manage.py migrate
5. Build your models on Models.py on api folder
   5.1 Apply serializers class on your api folder

# to run server

python .\manage.py runserver

# References

django
djangorestframework
