# NoSQL

This repository contains a set of Python scripts for interacting with MongoDB. Each script performs a specific task related to managing a MongoDB database called `my_db` with a collection named `school`.

## List of Scripts

### 0-list_databases
- **Description**: Lists all databases in MongoDB.
- **Usage**: `cat 0-list_databases | mongo`

### 1-use_or_create_database
- **Description**: Creates or uses the database `my_db`.
- **Usage**: `cat 1-use_or_create_database | mongo`

### 2-insert
- **Description**: Inserts a document into the `school` collection with the name "Holberton school."
- **Usage**: `cat 2-insert | mongo my_db`

### 3-all
- **Description**: Lists all documents in the `school` collection.
- **Usage**: `cat 3-all | mongo my_db`

### 4-match
- **Description**: Lists all documents with the name "Holberton school" in the `school` collection.
- **Usage**: `cat 4-match | mongo my_db`

### 5-count
- **Description**: Displays the number of documents in the `school` collection.
- **Usage**: `cat 5-count | mongo my_db`

### 6-update
- **Description**: Adds a new attribute "address" with the value "972 Mission street" to documents with the name "Holberton school" in the `school` collection.
- **Usage**: `cat 6-update | mongo my_db`

### 7-delete
- **Description**: Deletes all documents with the name "Holberton school" in the `school` collection.
- **Usage**: `cat 7-delete | mongo my_db`

### 8-all (Python)
- **Description**: Lists all documents in the `school` collection using a Python function.
- **Usage**: `./8-main.py`

### 9-insert_school (Python)
- **Description**: Inserts a new document into the `school` collection based on provided keyword arguments using a Python function.
- **Usage**: `./9-main.py`

### 10-update_topics (Python)
- **Description**: Changes all topics of a school document based on the name using a Python function.
- **Usage**: `./10-main.py`

### 11-schools_by_topic (Python)
- **Description**: Returns a list of schools with a specific topic using a Python function.
- **Usage**: `./11-main.py`

### 12-log_stats (Python)
- **Description**: Provides statistics about Nginx logs stored in MongoDB. Displays the number of logs, methods used, and status checks.
- **Usage**: `./12-log_stats.py`

## Usage
To use these scripts, simply follow the usage instructions provided for each script. Make sure you have MongoDB installed and running locally.

## Author
Christophe NGAN @Sirothpech
