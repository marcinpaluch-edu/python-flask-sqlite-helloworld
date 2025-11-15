# My Flask Application 🚀

A full‑blown Python application boilerplate using **Flask**, **SQLAlchemy**, and **Flask‑Migrate** with SQLite.  
This project demonstrates a clean structure with models, services, routes, and migrations.

  
## 📂 Project Structure
  ```
  my_app/  
  │  
  ├── app/  
  │    ├── models/              # Database models  
  │    │   └── user.py
  │    │
  │    ├── routes/              # Flask Blueprints  
  │    │   └── user_routes.py
  │    │
  │    ├─ services/            # Business logic  
  │    │   └── auth_service.py  
  │    │
  │    ├── config.py            # Config classes  
  │    └── __init__.py          # App factory  
  │  
  ├── instance/                # SQLite instance file  
  ├── migrations/              # Alembic/Flask-Migrate  
  ├── .gitignore  
  ├── .env
  ├── README.md                # This file                       
  └── run.py                   # Entry point  
  ```

## ⚙️ Setup Instructions

1. **Prepare your environment**  
You'll need:  
 a. Python3  
 b. Extra packages installation - see below - Flask, SQLAlchemy, Alembic  
 c. SQLite3 - SQLite CLI will be handy  

2. **The core files**  
The core files are:  
```powershell
app/__init__.py
app/config.py
app/models/user.py
app/services/auth_service.py
app/routes/user_routes.py
run.py
```

3. **Install Python packages**
```powershell
pip install flask flask_sqlalchemy flask_migrate
```

4. **Set environment variables**  
Create a .env file (optional)

   ```Env
   SECRET_KEY=dev_secret
   ```

5. **Initialize the database**
   ```powershell
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

   This creates the SQLite database (dev.db) and the user table.

6. **Check the database**  
   You may want to install sqlite CLI. Download it from [https://sqlite.org/download.html](https://sqlite.org/download.html).  
   This Readme shows example of Powershell and sqlite3.exe.  
   Go to the home directory of your project and run:
   ```powershell
   cd instance
   sqlite3.exe dev.db
   ```
   Then in the SQLite CLI get all tables names:
   ```sqlite
   SQLite version 3.51.0 2025-11-04 19:38:17
   Enter ".help" for usage hints.
   sqlite> .tables
   alembic_version  user
   ```

   Then check schema of the user table:
   ```sql
   sqlite> .schema user
   CREATE TABLE user (
        id INTEGER NOT NULL,
        username VARCHAR(80) NOT NULL,
        email VARCHAR(120) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (email),
        UNIQUE (username)
   );
   ```

   Exit from SQLite CLI:
   ```sqlite
   sqlite> .exit
   ```

7. **Run the app**
   ```powershell
   python run.py
   ```

   Flask will start at: [https://127.0.0.1:5000](https://127.0.0.1:5000)

 
8. **Run the curl for tests**
   ```powershell
   curl.exe -X GET http://127.0.0.1:5000/
   ```

   The following output will display
   
   ```powershell
   {   
    "endpoints": [  
    "/users/hello",  
    "/users/ (GET - list users, POST - create user)"  
    ],  
    "message": "Flask app is running \ud83d\ude80"  
   }
   ```

   Try /hello route:
   ```powershell
   curl.exe -X GET "http://127.0.0.1:5000/users/hello"
   ```
   You'll see:  
   ```powershell
   {
     "message": "Hello from Flask! Your app is running \ud83d\ude80"
   }
   ```
   
9. **Add new user for test (Powershell Invoke-WebRequest example)**
   ```powershell
   Invoke-WebRequest -Uri "http://127.0.0.1:5000/users/" `
   -Method POST `
   -Headers @{ "Content-Type" = "application/json" } `
   -Body '{"username":"marcin","email":"marcin@example.com"}'
   ```  
   
   You'll see:  

   ```powershell
   StatusCode        : 200
   StatusDescription : OK
   Content           : {
                         "email": "marcin@example.com",
                         "id": 1,
                         "username": "marcin"
                       }

   RawContent        : HTTP/1.1 200 OK
                       Connection: close
                       Content-Length: 71
                       Content-Type: application/json
                       Date: Sat, 15 Nov 2025 21:45:57 GMT
                       Server: Werkzeug/3.1.3 Python/3.14.0

                       {
                         "email": "marcin@example.com",
                       ...
   Forms             : {}
   Headers           : {[Connection, close], [Content-Length, 71], [Content-Type, application/json], [Date, Sat, 15 Nov
                    2025 21:45:57 GMT]...}
   Images            : {}
   InputFields       : {}
   Links             : {}
   ParsedHtml        : System.__ComObject
   RawContentLength  : 71
   ```

10. **Final test**  
    Check if user was created successfully
    ```sql
    sqlite> select * from user;
    1|marcin|marcin@example.com
    sqlite>
    ```

    And this is the end of the config.

11. **Make note**  
    This is a simple script and there are various limitations. For example name and email address columns in the database are unique and re-sending the same POST request used in this example again and again will throw an exception. Expand the code by adding exception handling if you would like to overcome that challenge. Thank you. 

