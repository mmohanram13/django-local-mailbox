# django-local-mailbox
Local Mail Server implementation using Django

Steps to run the code: (in Windows)

1. pip install virtualenv
2. cd <location>
3. virtualenv <directory>
4. Scripts\activate.bat
5. clone repository as 'mailclient' in <directory>
6. cd mailclient
7. pip install -r requirements.txt
8. create database 'mailclient' in mysql
9. python manage.py migrate
10. python manage.py createsuperuser
	--> user: admin
	--> email: admin@example.com
	--> password: 123456
11. python manage.py runserver
12. go to http://127.0.0.1:8000/admin/
13. create users there. (create atleast 2 users)
	For example: user: a@example.com
		      password: 123456
14. logout from admin site
15. open 2 browser windows (one in normal and other in incognito)
16. log on to http://127.0.0.1:8000/ 
17. log in with 2 different accounts in 2 windows
18. Compose an email in one and click send
19. Refresh the other manually to see recieved messages.
20. Similarly do vice-versa. Also emails are visible on command prompt and are stored in db.
21. deactivate (in cmd) and exit

Important: configure your MySql db host, port and pass in mailClient/settings.py

For Linux and Mac machines only the virtualenv code will change
