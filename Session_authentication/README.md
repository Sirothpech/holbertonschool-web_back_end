# Session Authentication

## Tasks

### 0. Et moi et moi et moi!
Copy all your work from the `0x06. Basic authentication` project to this new folder.

In this version, you implemented Basic authentication to provide access to all User endpoints:

- `GET /api/v1/users`
- `POST /api/v1/users`
- `GET /api/v1/users/<user_id>`
- `PUT /api/v1/users/<user_id>`
- `DELETE /api/v1/users/<user_id>`

Now, add a new endpoint: `GET /users/me` to retrieve the authenticated User object.

Copy the folders `models` and `api` from the previous project `0x06. Basic authentication`. Make sure all mandatory tasks of this previous project are completed at 100% because this project (and the rest of this track) will be based on it.

Update `@app.before_request` in `api/v1/app.py`:
- Assign the result of `auth.current_user(request)` to `request.current_user`

Update the method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
- If `<user_id>` is equal to "me" and `request.current_user` is None: `abort(404)`
- If `<user_id>` is equal to "me" and `request.current_user` is not None: return the authenticated User in a JSON response (similar to a normal case of `GET /api/v1/users/<user_id>` where `<user_id>` is a valid User ID)
- Otherwise, keep the same behavior

In the first terminal:

```bash
$ cat main_0.py
#!/usr/bin/env python3
""" Main 0
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

# Create a user test
user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"

user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {}".format(user.id))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
```

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py
New user: 9375973a-68c7-46aa-b135-29f79e837495
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
```

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
[
  {
    "created_at": "2017-09-25 01:55:17",
    "email": "bob@hbtn.io",
    "first_name": null,
    "id": "9375973a-68c7-46aa-b135-29f79e837495",
    "last_name": null,
    "updated_at": "2017-09-25 01:55:17"
  }
]
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "created_at": "2017-09-25 01:55:17",
  "email": "bob@hbtn.io",
  "first_name": null,
  "id": "9375973a-68c7-46aa-b135-29f79e837495",
  "last_name": null,
  "updated_at": "2017-09-25 01:55:17"
}
```

### 1. Empty session
Create a class `SessionAuth` that inherits from `Auth`. For now, this class will be empty. This is the first step in creating a new authentication mechanism:

- Validate if everything inherits correctly without any overloading
- Validate the "switch" by using environment variables

Update `api/v1/app.py` to use a `SessionAuth` instance for the variable `auth` depending on the value of the environment variable `AUTH_TYPE`. If `AUTH_TYPE` is equal to `session_auth`:

```python
from api.v1.auth.session_auth import SessionAuth
auth = SessionAuth()
```

Otherwise, keep the previous mechanism.

In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0

.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

### 2. First User
Create a class method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` that returns `None` unless `self.user_id` is not `None` and `self.user_id` is in the dictionary `self.users`.

Update `api/v1/app.py` to use a `SessionAuth` instance for the variable `auth` depending on the value of the environment variable `AUTH_TYPE`. If `AUTH_TYPE` is equal to `session_auth`:

```python
from api.v1.auth.session_auth import SessionAuth
auth = SessionAuth()
```

Otherwise, keep the previous mechanism.

In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer HolbertonSchool98"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

### 3. Loggin
Create a class method `def create_session(self, email: str) -> str:` in `SessionAuth` that creates a `Session ID` for a user with email `email` by using the `user_id` of the user.

Create a class method `def user_id_for_session_id(self, session_id: str) -> str:` in `SessionAuth` that returns the `user_id` from the session ID.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` to use `user_id_for_session_id` to return a `User` instance based on a cookie value `session_id` if it exists.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` to check if `user_id` and `session_id` exist, and if they don't exist, create a new session for the user.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` to check if `user_id` and `session_id` exist, and if they don't exist, create a new session for the user.

In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.

0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "id": "ee2be3ca-bf7a-4f73-9872-5640f3d087a1",
  "email": "bob@hbtn.io",
  "created_at": "2022-03-11T15:48:51.918043",
  "updated_at": "2022-03-11T15:48:51.918043"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "id": "ee2be3ca-bf7a-4f73-9872-5640f3d087a1",
  "email: "bob@hbtn.io",
  "created_at": "2022-03-11T15:48:51.918043",
  "updated_at": "2022-03-11T15:48:51.918043"
}
```

### 4. Use Session ID for identifying a User
Update the class `User` to have the private attribute `session_id` and a property method `def session_id(self) -> str:` that returns the `session_id` for a `User` instance.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` to validate if the `session_id` is valid, and if not, return `None`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` to validate if the `session_id` is valid, and if not, return `None`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` to validate if the `session_id` is valid, and if not, return `None`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionAuth` to validate if the `session_id` is valid, and if not, return `None`.

In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "X-API-KEY: HolbertonSchool98"
{
  "error": "Forbidden"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "id": "ee2be3ca-bf7a-4f73-9872-5640f3d087a1",
  "email: "bob@hbtn.io",
  "created_at": "2022-03-11T15:48:51.918043",
  "updated_at": "2022-03-11T15:48:51.918043",
  "session_id": "`echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
}
```

### 5. Token generator
Create a class `SessionDBAuth` that inherits from `SessionAuth`. This class will override the class attribute `user_id_by_session_id` with a dictionary.

Create a class `SessionExpAuth` that inherits from `SessionDBAuth`. This class will override the class attribute `user_id_by_session_id` with a dictionary.

In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_exp_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "

OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "X-API-KEY: HolbertonSchool98"
{
  "error": "Forbidden"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "id": "ee2be3ca-bf7a-4f73-9872-5640f3d087a1",
  "email: "bob@hbtn.io",
  "created_at": "2022-03-11T15:48:51.918043",
  "updated_at": "2022-03-11T15:48:51.918043",
  "session_id": "`echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
}
```

### 6. Overload current_user - and update SessionExpAuth
Create a class method `def user_id_for_session_id(self, session_id: str) -> str:` in `SessionExpAuth` that returns the `user_id` from the session ID.

Create a class method `def create_session(self, email: str) -> str:` in `SessionExpAuth` that creates a `Session ID` for a user with email `email` by using the `user_id` of the user.

Create a class method `def create_session(self, email: str) -> str:` in `SessionExpAuth` that creates a `Session ID` for a user with email `email` by using the `user_id` of the user.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionExpAuth` to validate if the `session_id` is valid for a maximum duration of 5 minutes, and if not, return `None`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionExpAuth` to validate if the `session_id` is valid for a maximum duration of 5 minutes, and if not, return `None`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionExpAuth` to validate if the `session_id` is valid for a maximum duration of 5 minutes, and if not, return `None`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `SessionExpAuth` to validate if the `session_id` is valid for a maximum duration of 5 minutes, and if not, return `None`.

Update the class `User` to use a `session_id` with a maximum duration of 5 minutes.

In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_exp_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0

:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "X-API-KEY: HolbertonSchool98"
{
  "error": "Forbidden"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer HolbertonSchool98"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "X-API-KEY: HolbertonSchool98"
{
  "error": "Forbidden"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Forbidden"
}
```

```bash
$ sleep 6 ; curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Forbidden"
}
```

### 7. New view for Session Authentication
Update the class `User` to have the public method `def to_dict(self) -> Dict[str, Any]:` that returns a dictionary representation of a `User` instance for using in a `Session ID`.

Create a class `AuthSessionExp` that inherits from `SessionExpAuth`.

Create a class `AuthSessionExp` that inherits from `SessionExpAuth`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `AuthSessionExp` to return a `User` instance based on the `user_id` and `session_id`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `AuthSessionExp` to return a `User` instance based on the `user_id` and `session_id`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `AuthSessionExp` to return a `User` instance based on the `user_id` and `session_id`.

Update the method `def current_user(self, request=None) -> TypeVar('User'):` in `AuthSessionExp` to return a `User` instance based on the `user_id` and `session_id`.

In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth_session_exp python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "error": "Unauthorized"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -c /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "X-API-KEY: HolbertonSchool98"
{
  "error": "Forbidden"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Forbidden

"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer HolbertonSchool98"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Bearer `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "error": "Unauthorized"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "X-API-KEY: HolbertonSchool98"
{
  "error": "Forbidden"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Forbidden"
}
```

```bash
$ sleep 4 ; curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Forbidden"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me" -H "X-SESSION-ID: `echo -n 9375973a-68c7-46aa-b135-29f79e837495 | sha256sum | awk '{print $1}'`"
{
  "id": "ee2be3ca-bf7a-4f73-9872-5640f3d087a1",
  "email": "bob@hbtn.io",
  "created_at": "2022-03-11T15:48:51.918043",
  "updated_at": "2022-03-11T15:48:51.918043"
}
```

```bash
$ sleep 4 ; curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Forbidden"
}
```

```bash
$ sleep 2 ; curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "id": "ee2be3ca-bf7a-4f73-9872-5640f3d087a1",
  "email": "bob@hbtn.io",
  "created_at": "2022-03-11T15:48:51.918043",
  "updated_at": "2022-03-11T15:48:51.918043"
}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/logout" -X DELETE
{}
```

```bash
$ curl -b /tmp/1 "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Forbidden"
}
```

## 8. Logout

### Description
Update the class `SessionAuth` by adding a new method `def destroy_session(self, request=None):` that deletes the user session / logout:

- If the request is equal to None, return False
- If the request doesn’t contain the Session ID cookie, return False - you must use `self.session_cookie(request)`
- If the Session ID of the request is not linked to any User ID, return False - you must use `self.user_id_for_session_id(...)`
- Otherwise, delete in `self.user_id_by_session_id` the Session ID (as key of this dictionary) and return True

Update the file `api/v1/views/session_auth.py`, by adding a new route `DELETE /api/v1/auth_session/logout`:

- Slash tolerant
- You must use `from api.v1.app import auth`
- You must use `auth.destroy_session(request)` for deleting the Session ID contains in the request as a cookie:
  - If `destroy_session` returns False, `abort(404)`
  - Otherwise, return an empty JSON dictionary with the status code 200

### Example

#### In the first terminal:

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

#### In a second terminal:

```bash
$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
# Output truncated for brevity
{
  "created_at": "2017-10-16 04:23:04",
  "email": "bobsession@hbtn.io",
  "first_name": null,
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992",
  "last_name": null,
  "updated_at": "2017-10-16 04:23:04"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "created_at": "2017-10-16 04:23:04",
  "email": "bobsession@hbtn.io",
  "first_name": null,
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992",
  "last_name": null,
  "updated_at": "2017-10-16 04:23:04"
}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
# Output truncated for brevity
{}
```

```bash
$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "error": "Forbidden"
}
```
