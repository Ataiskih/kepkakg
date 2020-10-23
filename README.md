# kepkakg
Route map - https://drive.google.com/file/d/178AKbjdQ9ugfvQaXLCLsC1-TtS1NAOYV/view?usp=sharing
DB Diagramm - https://dbdiagram.io/d/5f91dc9c3a78976d7b78cdc1
To Do List - https://trello.com/b/XpdC6n2u/todolist-kepkakg

1. git clone https://github.com/Ataiskih/kepkakg.git
2. cd kepkakg
3. Linux: sourse env/bin/activate 
   Windows: call env/bin/activate 
4. pip install -r requirements.txt
5. cd base/
6. python manage.py migrate
7. to runserver: python manage.py runserver_plus 8001 --cert-file /tmp/cert
8. In broweser URL paste: https://127.0.0.1:8001

COMMANDS
* git branch
* git checkout your_branch
    * git add .
    * git commit -m ""
    * git push -u origin your_branch
* git checkout master
* git pull
* git merge your_branch
