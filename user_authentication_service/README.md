# User Authentication Service

## Tasks

### 0. User Model

In this task, create a SQLAlchemy model named `User` for a database table named `users`. The model should have the following attributes:

- `id`: integer primary key
- `email`: non-nullable string
- `hashed_password`: non-nullable string
- `session_id`: nullable string
- `reset_token`: nullable string

```python
# main.py
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
```

Output:
```python
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
```

### 1. Create User

Complete the `DB` class by implementing the `add_user` method. The method should take two required string arguments, `email` and `hashed_password`, and return a `User` object. The method should save the user to the database. No validations are required at this stage.

```python
# main.py
from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)
```

Output:
```python
1
2
```

### 2. Find User

Implement the `DB.find_user_by` method. This method takes arbitrary keyword arguments and returns the first row found in the `users` table filtered by the method’s input arguments. Use SQLAlchemy’s `NoResultFound` and `InvalidRequestError` to handle cases where no results are found or when wrong query arguments are passed.

```python
# main.py
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

try:
    find_user = my_db.find_user_by(email="test@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")
```

Output:
```python
1
1
Not found
Invalid
```

### 3. Update User

Implement the `DB.update_user` method. This method takes a required `user_id` integer and arbitrary keyword arguments and returns `None`. The method uses `find_user_by` to locate the user to update, then updates the user’s attributes as passed in the method’s arguments and commits changes to the database. If an argument that does not correspond to a user attribute is passed, raise a `ValueError`.

```python
# main.py
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated")
except ValueError:
    print("Error")
```

Output:
```python
1
Password updated
```

### 4. Hash Password

Define a `_hash_password` method in the `auth` module. This method takes in a password string argument and returns bytes. The returned bytes is a salted hash of the input password, hashed with `bcrypt.hashpw`.

```python
# main.py
from auth import _hash_password

print(_hash_password("Hello Holberton"))
```

Output:
```python
b'$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2'
```

### 5. Register User

Implement the `Auth.register_user` method in the `Auth` class. This method should take mandatory `email` and `password` string arguments and return a `User` object. If a user already exists with the passed email, raise a `ValueError` with the message `User <user's email> already exists`. If not, hash the password with `_hash_password`, save the user to the database using `self._db`, and return the `User` object.

```python
# main.py
from auth import Auth

email = 'me@

me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("Successfully created a new user!")
except ValueError as err:
    print("Could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("Successfully created a new user!")
except ValueError as err:
    print("Could not create a new user: {}".format(err))
```

Output:
```python
Successfully created a new user!
Could not create a new user: User me@me.com already exists
```

### 6. Basic Flask App

Create a basic Flask app with a single GET route ("/") that returns a JSON payload of the form: `{"message": "Bienvenue"}`.

```python
# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return jsonify(message="Bienvenue")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

### 7. Register User Endpoint

Implement the endpoint to register a user. Define a `users` function that implements the POST `/users` route. Import the `Auth` object and instantiate it at the root of the module.

```python
# app.py
from auth import Auth

AUTH = Auth()
```

The endpoint should expect two form data fields: "email" and "password". If the user does not exist, the endpoint should register it and respond with the following JSON payload:

```json
{"email": "<registered email>", "message": "user created"}
```

If the user is already registered, catch the exception and return a JSON payload of the form:

```json
{"message": "email already registered"}
```

and return a 400 status code.

### 8. Credentials Validation

Implement the `Auth.valid_login` method. It should expect `email` and `password` required arguments and return a boolean. Try locating the user by email. If it exists, check the password with `bcrypt.checkpw`. If it matches, return `True`. Otherwise, return `False`.

```python
# main.py
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "WrongPwd"))

print(auth.valid_login("unknown@email", password))
```

Output:
```python
True
False
False
```

### 9. Generate UUIDs

Implement a `_generate_uuid` function in the `auth` module. The function should return a string representation of a new UUID. Use the `uuid` module. Note that the method is private to the `auth` module and should NOT be used outside of it.

### 10. Get Session ID

Implement the `Auth.create_session` method. It takes an `email` string argument and returns the session ID as a string. The method should find the user corresponding to the email, generate a new UUID, store it in the database as the user’s `session_id`, and then return the session ID.

```python
# main.py
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))
```

Output:
```python
5a006849-343e-4a48-ba4e-bbd523fcca58
None
```

### 11. Log In

Implement a login function to respond to the POST `/sessions` route. The request is expected to contain form data with "email" and a "password" fields. If the login information is incorrect, use `flask.abort` to respond with a 401 HTTP status. Otherwise, create a new session for the user, store it as the session ID in a cookie with key "session_id" on the response, and return a JSON payload.

```bash
curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
```

Output:
```bash
{"email":"bob@bob.com","message":"logged in"}
```

```bash
curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=BlaBla' -v
```

Output:
```bash
401 Unauthorized
```

### 12. Find User by Session ID

Implement the `Auth.get_user_from_session_id` method. It takes a single `session_id` string argument and returns the corresponding `User` or `None`. If the session ID is `None` or no user is found, return `None`. Otherwise, return the corresponding user.

### 13. Destroy Session

Implement `Auth

.destroy_session`. The method takes a single `user_id` integer argument and returns `None`. The method updates the corresponding user’s session ID to `None`.

### 14. Log Out

Implement a logout function to respond to the DELETE `/sessions` route. The request is expected to contain the session ID as a cookie with key "session_id". Find the user with the requested session ID. If the user exists, destroy the session, redirect the user to GET `/`, and respond with a 200 HTTP status. If the user does not exist, respond with a 403 HTTP status.

### 15. User Profile

Implement a profile function to respond to the GET `/profile` route. The request is expected to contain a session_id cookie. Use it to find the user. If the user exists, respond with a 200 HTTP status and the following JSON payload:

```json
{"email": "<user email>"}
```

If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.

```bash
curl -XGET localhost:5000/profile -b "session_id=75c89af8-1729-44d9-a592-41b5e59de9a1"
```

Output:
```bash
{"email": "bob@bob.com"}
```

```bash
curl -XGET localhost:5000/profile -b "session_id=nope" -v
```

Output:
```bash
403 Forbidden
```

### 16. Generate Reset Password Token

Implement the `Auth.get_reset_password_token` method. It takes an `email` string argument and returns a string. Find the user corresponding to the email. If the user does not exist, raise a `ValueError` exception. If it exists, generate a UUID, update the user’s `reset_token` database field, and return the token.

### 17. Get Reset Password Token

Implement a `get_reset_password_token` function to respond to the POST `/reset_password` route. The request is expected to contain form data with the "email" field. If the email is not registered, respond with a 403 status code. Otherwise, generate a token and respond with a 200 HTTP status and the following JSON payload:

```json
{"email": "<user email>", "reset_token": "<reset token>"}
```

### 18. Update Password

Implement the `Auth.update_password` method. It takes a `reset_token` string argument and a `password` string argument and returns `None`. Use the reset_token to find the corresponding user. If it does not exist, raise a `ValueError` exception. Otherwise, hash the password and update the user’s `hashed_password` field with the new hashed password and the `reset_token` field to `None`.

### 19. Update Password End-Point

Implement the `update_password` function in the `app` module to respond to the PUT `/reset_password` route. The request is expected to contain form data with fields "email", "reset_token", and "new_password". Update the password. If the token is invalid, catch the exception and respond with a 403 HTTP code. If the token is valid, respond with a 200 HTTP code and the following JSON payload:

```json
{"email": "<user email>", "message": "Password updated"}
```