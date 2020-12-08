# Install this Library
python -m pip install Django
pip install mysql-connector-python
pip install enum
pip install  xlrd

#to start a project open terminal where is located file "manage.py" and write in terminal
manage.py migrate
manage.py makemigrations
manage.py migrate
manage.py runserver
