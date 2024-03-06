# i18n

## Tasks

### 0. Basic Flask app
**File:** [0-app.py](0-app.py)

- Setup a basic Flask app with a single `/` route.
- Create an `index.html` template with the page title `<title>` as "Welcome to Holberton" and header `<h1>` as "Hello world".

### 1. Basic Babel setup
**File:** [1-app.py](1-app.py)

- Install Flask Babel extension using `$ pip3 install flask_babel`.
- Instantiate Babel object in the app, store it in a module-level variable named `babel`.
- Create a `Config` class with a `LANGUAGES` class attribute equal to `["en", "fr"]`.
- Set Babel's default locale ("en") and timezone ("UTC") using `Config` as the app's config.

### 2. Get locale from request
**File:** [2-app.py](2-app.py)

- Create a `get_locale` function with the `babel.localeselector` decorator.
- Use `request.accept_languages` to determine the best match with supported languages.

### 3. Parametrize templates
**Files:** [3-app.py](3-app.py), [babel.cfg](babel.cfg)

- Use `_` or `gettext` function to parametrize templates with message IDs `home_title` and `home_header`.
- Create a `babel.cfg` file.
- Initialize translations using `$ pybabel extract -F babel.cfg -o messages.pot .`.
- Create dictionaries using `$ pybabel init -i messages.pot -d translations -l en` and `$ pybabel init -i messages.pot -d translations -l fr`.
- Edit files `translations/[en|fr]/LC_MESSAGES/messages.po` with translations.
- Compile dictionaries using `$ pybabel compile -d translations`.

### 4. Force locale with URL parameter
**File:** [4-app.py](4-app.py)

- Implement a way to force a particular locale by passing `locale=fr` parameter to app's URLs.
- In `get_locale` function, detect if the incoming request contains the `locale` argument.
- Return the value if it's a supported locale; otherwise, resort to the default behavior.

### 5. Mock logging in
**File:** [5-app.py](5-app.py)

- Create a user table as a mock database.
- Define a `get_user` function to return a user dictionary or `None`.
- Use `app.before_request` to execute `before_request` function before all other functions.
- Display welcome messages in HTML template based on user login status.

### 6. Use user locale
**File:** [6-app.py](6-app.py)

- Change `get_locale` function to use a user's preferred locale if supported.
- Priority order: Locale from URL parameters > Locale from user settings > Locale from request header > Default locale.

### 7. Infer appropriate time zone
**File:** [7-app.py](7-app.py)

- Define a `get_timezone` function and use the `babel.timezoneselector` decorator.
- Priority order: Timezone from URL parameters > Timezone from user settings > Default to UTC.
- Validate that the provided or user time zone is a valid time zone using `pytz.timezone` and catch `pytz.exceptions.UnknownTimeZoneError`.