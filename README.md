# INSTRUCTIONS

This is a short and simple Django project created according to SOME of the  guidelines explained in "Python Crash Course - Eric Matthes". Follow the instructions to get the project running on a local server in your PC.

- Clone this repository to a local folder
- Run the following commands for creating a virtual environment, working inside it and installing requirements needed for the project to run: 
``` 
virtualenv --python python3 venv
source venv/bin/activate
pip install -r requirements.txt
``` 
- Run the following commands to create and set a local sqlite database 
``` 
python manage.py makemigrations blogs
python manage.py migrate
``` 
- Finally, run your local server with the following command 
``` 
python manage.py runserver
``` 
- Access to your localhost IP through any web browser to use the app
