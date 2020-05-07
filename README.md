# Team Project Mannheim - Cluj Master Service

## Installation
First, make sure you have at least Python 3.7 installed:
```
$ python -V
Python 3.7.1
```

Install the requirements:
```
$ pip install -r requirements.txt
```
### Running the server
You need to start the database first. You can use the already provided
[docker-compose](./development/docker-compose.yml) file for that:
```shell script
$ docker-compose -f ./development/docker-compose.yml up -d
```
Note: make sure that you're in the project root folder a.k.a where this README
file is.

Next up, run the migrations:
```shell script
$ ./manage.py migrate
```

After that is done, the database is ready and an admin user has already been created.
The user's name and password are both: admin

Use the BrowsableApi to check out the endpoints:
```
http://localhost:8000/api/
```
Keep in mind to always use trailing slashes! That means, always end an URL with a slash.

e.g. wrong: http://localhost:8000/api

e.g. correct: http://localhost:8000/api/


## Testing

Use this command to run the tests (make sure you are in the folder where your project is):
```
$ python ./manage.py test
```
Alternatively you can use directly the `pytest` command:
```shell script
$ pytest
```
In case that `pytest` doesn't work or throws any test unrelated errors and you're on Windows, the `manage.py`
has been configured to used the pytest runner under the hood. It should work on any OS and not throw any 
unexpected errors.


If you want to avoid running all tests, you can run specific tests by using the `-k` parameter.

e.g.: running all tests which contain the string "auth" in either the test name or test class:
`manage.py`:
```shell script
$ python ./manage.py test -- -k auth
```

`pytest`:
```shell script
$ pytest -k auth
```

You can find more on `pytest` [here](https://docs.pytest.org/en/latest/index.html).
