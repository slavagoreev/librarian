# LMS (Librarian)
Innopolis Library Management System

## Web-page


## Getting Started
Let`s deploy system on your local machine
First of all, you should download and unpack repository from here: https://github.com/slavagoreev/librarian/archive/master.zip

### Installing
1. Install Python 3.x: https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe
  (Make sure you`ve installed pip (including in the Python Installer))
  (Make sure that python and pip were added in system variable 'Path')
2. Install Node.JS: https://nodejs.org/en/download/ (Make sure that node was added in system variable 'Path')
3. Now let`s necessery libraries and frameworks - open console and type:
      ```
      pip install django djangorestframework django-rest-auth django-allauth django-cors-headers djangorestframework-jwt
      ```
4. You need to be sure about where is your .sock of MySQL.

### Migrations
Let's make begining preparation for Data Base (make migrations)
1. Go to ```librarian/server/```
2. Open console here and type:
      ```
      python manage.py makemigrations lmsinno
      python manage.py migrate
      ```
3. Now we need to go to to ```../librarian/client/```, and do following in console:
      ```
      npm install -g @angular/cli
      npm install
      ```

### Admin
Let's create local super user
1. Go to ```project_path/librarian-master/server```
2. Open console here and type:
      ```
      python manage.py createsuperuser
      ```
3. After that you should input username, email and password
      
### Running
Finally, let`s run our server on local machine:
1. Go to ```project_path/librarian-master/server```
2. Open console here and type:
      ```
      python manage.py runserver localhost:80
      ```
3. Go to [localhost/admin](http://localhost/admin) and enter username and password from previous step

### Test DataSet
Moreover you can upload test dataset (about 500 books) (You server should have been runned)
1. Go to ```project_path/librarian-master/shared```
2. Open console here and type:
      ```
      node dataset_loader.js
      ```
3. It will take about 5 minutes

## Using of the service

### 1. Client
If you wish to see available books or checkout new book, you may enter the main page:
      ```
      http://trainno.ru/
      ```
Also you can manage your profile.
### 2. Server
#### Orders
To check orders and their statuses you may log in by librarian first, then type:
      ```
      http://trainno.ru:41000/api/orders/
      ```
### Sample Python script:
```python
import requests as rq

admin = "JWT " + rq.post("https://trainno.ru/api/users/login/", data={"username": "librarian", "password": "librarian"}).json()['token']
student = "JWT " + rq.post("https://trainno.ru/api/users/login/", data={"username": "john.doe", "password": "FXM-HC3-JKc-WXa"}).json()['token']
faculty = "JWT " + rq.post("https://trainno.ru/api/users/login/", data={"username": "joseph.brown", "password": "joseph.brown"}).json()['token']
      
request = rq.get("https://trainno.ru/api/documents/", headers={"BEARER": admin}).json()
data = request['data']
status = request['status']
print(data, status)
```
      
