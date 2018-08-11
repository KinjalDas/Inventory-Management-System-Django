# Inventory-Management-System-Django
This is an inventory management system written in Python 3.6.5 and Django 2.0.7 and datatables is a Jquery plugin. 
The local installation of python 32/64bit is provided with the project as "python-3.7.0.exe/python-3.7.0-amd64.exe". 
Also the local installation of DJango is provided as "django-master" which can be run as "python setup.py install". 
The project is run through "python manage.py runserver".I have provided way to extract the transaction info in a csv format as "data-extract.py". The main page lists all the items. 
Clicking the name of any of the itmes will take you to the transaction page (Transfer/Return) page. 
Here clicking on Transfer/Return will take you to confirmation page providing you with the transaction number. The date of transcation is auto-added by the system as the present date.Also by going to the django admin page ("homepage/admin") will let you Create, Read, Update and Delete Items, Clients (supposed to receive or return items), Categories and Transactions. 
Dont forward, back or reload pages as that may lead to redundant data. Also,search can be based on any of the components - Name,
Category,No. of items, Item No. and it will work seamlessly.Transact by using buttons on the page only. 
