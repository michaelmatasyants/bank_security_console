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

4. Create an .env file and locate it in the same directory where your project is. Copy and append database settings in `.env` file like this:

   ```console
   DB_ENGINE=paste_here_engine
   DB_HOST=paste_here_host
   DB_PORT=paste_here_port
   DB_NAME=paste_here_host_name
   DB_USER=paste_here_host_user
   DB_PASSWORD=paste_here_host_password
   DB_SECRET_KEY=paste_here_secret_key
   DB_DEBUG=pass False before publishing or True to debug
   ```

5. Settings:

   The settings.py (located in `/project/settings.py`) contains all the project propeties. To start working with the database, firstly you must connect to it (you only need to do the step 4).
   Values of `DB_ENGINE`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_SECRET_KEY` and `DB_DEBUG` would be automatically passed from `.env` file to `/project/settings.py`.
   You can see for yourself by opening `settings.py`.

6. Remember to add `.env` to your `.gitignore` if you are going to put the project on GIT.


### How to run

Run in your console:

```Console
>>> python3 manage.py runserver 0.0.0.0:8000
```

Output:
    
```Console
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 30, 2023 - 20:57:07
Django version 3.2.18, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

To make sure the data is displayed on the website, follow the link from the output: [http://0.0.0.0:8000/](http://0.0.0.0:8000/)

### Project Goals
The code is written for educational purposes.
