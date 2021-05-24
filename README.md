# uuid-timestamp-task

This simple task is to showcase a uuid generated at a particular timestamp when a user  
visits our application homepage.

### How to set up and run

* Install python version 3 from [here]('https://www.python.org/downloads/)
* Clone this repo to your local computer
* Change directory into the base project directory `cd uuid-timestamp-task`
* Set up your `venv` as this is recommended, so you do not pollute your e python installation

  #### Venv setup
    * `python3 -m venv venv` this will create the venv directory if it doesn't exist, and also create directories inside
      it containing a copy of the Python interpreter, the standard library, and various supporting files 
    * Activate the virtual environment:
      * `venv\Scripts\activate.bat` - windows
      * `sourc venv/bin/activate` - Unix or MacOS
* Once your `venv` is activated, just install your projects requirements found in the `requirements.txt` file with `pip install -r requirements.txt`
* Change directory into the `uuid_timestamp` directory which houses our main django project `cd uuid_timestamp`
* Run the project migrations, since this is a small task, using databases like postgres will be an overkill, so we will leverage the sqlite database which is very light.  
  To run the migrations, run this command `python manage.py migrate`, make sure you are in the `uuid_timestamp` directory
* Run the application with `python manage.py runserver`
