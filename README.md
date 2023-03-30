# Bank security console

This tutorial project shows how to connect to a database, make queries without SQL using Django ORM, and display data from the database on a website.

### How to install

1. Firstly, you have to install python and pip (package-management system) if they haven't been already installed.

2. Create a virtual environment with its own independent set of packages using [virtualenv/venv](https://docs.python.org/3/library/venv.html). It'll help you to isolate the project from the packages located in the base environment.

3. Install all the packages used in this project, in your virtual environment which you've created on the step 2. Use the `requirements.txt` file to install dependencies.
   
   Run in your console:
    ```console
    >>> pip install -r requirements.txt
    ```
4. Settings:

   The settings.py (located in `/project/settings.py`) contains all the project propeties. To start working with the database, firstly you must connect to it by passing `ENGINE`, `HOST`, `PORT`, `NAME`, `USER` and `PASSWORD`. All of the above is already done, you can see for yourself by opening `settings.py`.


### How to run

Run in your console:

```Console
>>> python3 main.py
```

Output:
    
```Console
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 30, 2023 - 20:57:07
Django version 3.2.18, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

To make sure the data is displayed on the website, follow the link from the output: ` http://127.0.0.1:8000/`.

### Project Goals
The code is written for educational purposes.
