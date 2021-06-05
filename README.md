# Libray Django

Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

## Tech

- [Django] - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design;
- [Pillow] - Pillow is the friendly Python Imaging Library;
- [Sqlparse] - sqlparse is a non-validating SQL parser.

## Installation

#### _Create venv_
```sh
python3 -m venv .
```

#### _Activate venv_
```sh
source bin/activate
```

#### _Install libs_
```sh
pip install -r requirements.txt
```

#### _Create database_
```sh
python3 manage.py migrate
```

#### _Run application_
```sh
python3 manage.py runserver
```

## License

MIT