# AirBnB Clone - MySQL

## Project Overview

This project is part of the **AirBnB clone** series, specifically focusing on the integration of **MySQL** and transitioning from file storage to a relational database storage system using **SQLAlchemy**.

The project was developed in collaboration between **David Tuyishime Rubagumya** and **Carine Ahishakiye YIBUKABAYO** as part of our software engineering journey.

## Features

- Unit testing for all major components.
- Environment variable management for better configuration flexibility.
- MySQL integration using SQLAlchemy for database operations.
- Two types of storage engines: FileStorage and DBStorage.
- Command interpreter integrated with MySQL storage.
- Python scripting, SQL queries, and database interaction.

## Concepts Covered

### Python

- Usage of `*args` and `**kwargs` to manage arguments in functions.
- Named arguments in Python functions.
- Python classes mapped to MySQL tables using SQLAlchemy ORM.
- Handling two different storage engines using the same codebase.
- Proper documentation for modules, classes, and functions.

### MySQL

- Creating and managing a MySQL database.
- User and privilege management in MySQL.
- Querying a MySQL database using SQLAlchemy.
- Working with environment variables for database configuration.

## Environment Variables

You will need to configure the following environment variables to run the project correctly:

- `HBNB_ENV`: Running environment (either “dev” or “test”).
- `HBNB_MYSQL_USER`: Username for MySQL.
- `HBNB_MYSQL_PWD`: Password for MySQL.
- `HBNB_MYSQL_HOST`: MySQL hostname.
- `HBNB_MYSQL_DB`: MySQL database name.
- `HBNB_TYPE_STORAGE`: Type of storage, either “file” or “db”.

## Requirements

- Python 3.8.5
- MySQL 8.0
- SQLAlchemy version 1.4.x
- Ubuntu 20.04 LTS

### Python Scripts

- Files must be executable and conform to **pycodestyle** (version 2.7.\*).
- Ensure proper documentation for each module, class, and function.
- Python scripts must start with `#!/usr/bin/python3`.

### SQL Scripts

- SQL files should start with comments explaining the task.
- All SQL keywords should be uppercase (e.g., SELECT, WHERE).
- Ensure SQL files are executable on MySQL 8.0.

## Testing

- We use the `unittest` module for testing the entire project.
- Tests are located in the `tests/` folder.
- To run all tests, use the command:

  ```bash
  python3 -m unittest discover tests
