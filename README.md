# kepkakg
1. git clone https://github.com/Ataiskih/kepkakg.git
2. cd kepkakg
3. Linux: sourse env/bin/activate 
   Windows: call env/bin/activate 
4. pip install -r requirements.txt
5. cd base/
6. python manage.py migrate
7. to runserver: python manage.py runserver_plus 8001 --cert-file /tmp/cert
8. In broweser URL paste: https://127.0.0.1:8001
