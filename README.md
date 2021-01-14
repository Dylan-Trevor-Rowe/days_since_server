# days_since_server

# Days-Since
Days-Since is a Full CRUD Full Stack application that I built as my final-capstone at Nashville Software School.  
The Application was built to aid Multiple-Sclerosis patients in tracking their disease progression over time.

A user can track their daily symptoms, view their all time average (sleep, emotional-well-being, pain and fatigue scales), journal about their day, set goals
and log them if completed, and also post and comment on helpful articles that correlate to the disease. 

![Days-Since](https://github.com/Dylan-Trevor-Rowe/days-since-client/blob/main/src/components/Days-Since%20read%20me%20picture.png)

## Technologies 
Technologies used include: React, React-Router-Dom,  Python, Django, and Material Ui.

## Running the server locally

Dependencies: Python 3.8

Clone the repo: git clone https://github.com/Dylan-Trevor-Rowe/days_since_server
Activate the virtual environment: pipenv shell
Install the dependencies for the virtual environment: pipenv install
Setup the database from the fixtures by running the seed file sh seed.sh
Run the server python manage.py runserver

##Deploying changes to the "production server"
If new packages have been installed in the pipenv, run pipenv lock -r > requirements.txt to save these dependencies to the virtual environment
Push your changes to github, create a pr, and after approval, it will be the new main branch
Log into pythonAnywhere, open the bash script for whoYou, and git pull origin main to get the changes
If changes have been made to the dependencies, run pip install -r requirements.txt , note that the server uses a different virtual environment(virtualenv instead of pipenv. This should already be running.)
Reload the web app: In pythonanywhere, navigate to the webapp, and click the big green button that says reload web app

### Client Side link
To view the client side repo head to https://github.com/Dylan-Trevor-Rowe/days-since-client


### `npm start`

If server is running open [http://localhost:3000](http://localhost:3000) to view it in the browser.


