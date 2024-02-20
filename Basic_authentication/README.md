# Basic Authentication

This project involves implementing basic authentication for a simple API with Flask. The API has a User model, and user information is stored through serialization/deserialization in files.

## Setup and Start Server

1. Install required packages:

    ```bash
    bob@dylan:~$ pip3 install -r requirements.txt
    ```

2. Start the server:

    ```bash
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    ```

## Task 1: Unauthorized Error Handler

HTTP status code for an unauthorized request is 401. Implement an error handler for this status code that returns a JSON response: `{"error": "Unauthorized"}`. For testing, add a new endpoint:

- Route: GET /api/v1/unauthorized
- This endpoint should raise a 401 error using `abort(401)`.

Example:

```bash
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized"
{
  "error": "Unauthorized"
}
```

## Task 2: Forbidden Error Handler

HTTP status code for a request where the user is authenticated but not allowed to access a resource is 403. Implement an error handler for this status code that returns a JSON response: `{"error": "Forbidden"}`. For testing, add a new endpoint:

- Route: GET /api/v1/forbidden
- This endpoint should raise a 403 error using `abort(403)`.

Example:

```bash
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden"
{
  "error": "Forbidden"
}
```

## Task 3: Auth Class

Create an `Auth` class in the `api/v1/auth` folder with the following methods:

- `require_auth(self, path: str, excluded_paths: List[str]) -> bool`
- `authorization_header(self, request=None) -> str`
- `current_user(self, request=None) -> TypeVar('User')`

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
False
None
None
```

## Task 4: Define Routes Excluded from Authentication

Update the `require_auth` method in the `Auth` class to return `True` if the path is not in the list of excluded paths.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_1.py
True
True
True
False
False
True
True
```

## Task 5: Request Validation

Validate all requests to secure the API. Add request validation by checking if the path requires authentication, if the path is in the exclusion list, and if the user is authenticated.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

## Task 6: Basic Auth

Create a `BasicAuth` class that inherits from `Auth`. Update the app to use `BasicAuth` based on the environment variable `AUTH_TYPE`.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

## Task 7: Basic - Base64 Part

Add methods to extract and decode the Base64 part of the Authorization header in the `BasicAuth` class.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_2.py
None
None
None
Holberton
SG9sYmVydG9u
SG9sYmVydG9uIFNjaG9vbA==
None
```

## Task 8: Basic - Base64 Decode

Add a method to decode the Base64 Authorization header in the `BasicAuth` class.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_3.py
None
None
None
Holberton
Holberton School
Holberton School
```

## Task 9: Basic - User Credentials

Add a method to extract user credentials from the decoded Base64 Authorization header in the `BasicAuth` class.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_4.py
(None, None)
(None, None)
(None, None)
('Holberton', 'School')
('bob@gmail.com', 'toto1234')
```

## Task 10: Basic - User Object

Add a method to retrieve a `User` instance based on email and password in the `BasicAuth` class.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_5.py 
New user: Bob Dylan
None
None
None
None
Bob Dylan
```

## Task 11: Overload Current User

Overload the `current_user` method in the `BasicAuth` class to retrieve a `User` instance for a request.

Example:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
