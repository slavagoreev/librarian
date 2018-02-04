# LMS (Librarian)
Innopolis Library Management System

## Getting Started
Let`s deploy system on your local machine
First of all, you should download and unpack repository from here: https://github.com/slavagoreev/librarian/archive/master.zip

### Installing
1. Install Python 3.x: https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe
  (Make sure you`ve installed pip (including in the Python Installer))
  (Also make sure that python and pip were added in system variable 'Path')
2. Install Node.JS: https://nodejs.org/en/download/
3. Now let`s necessery libraries and frameworks - open console and type:
      ```
      pip install django
      pip install djangorestframework
      ```

### Migrations
Let`s make begining preparation for Data Base (make migrations)
1. Go to project_path/librarian-master/server
2. Open console here and type:
      ```
      python manage.py makemigrations lmsinno
      python manage.py migrate
      ```
      
### Admin
Let`s create local super user
1. Go to project_path/librarian-master/server
2. Open console here and type:
      ```
      python manage.py createsuperuser
      ```
 3. After that you should input username, email and password
      
### Running
Finally, let`s run our server on local machine:
1. Go to project_path/librarian-master/server
2. Open console here and type:
      '''
      python manage.py runserver localhost:80
      '''
3. Go to [localhost/admin](http://localhost/admin) and enter username and password from previous step
