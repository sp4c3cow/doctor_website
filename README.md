###Python driven landing page###

To setup correctly, you need to install requirements.txt
`pip3 install -r requirements.txt`

Then run migrations and start django local server and browser localhost:8000 in your browser
`python3 manage.py migrate
python3 manage.py runserver`

Also you need to create a speruser account to be able to test all website functionality
`python3 manage.py createsuperuser`
To access admin menu�, type this link in your browser and provide superuser credentials
`http://localhost:8000/admin`