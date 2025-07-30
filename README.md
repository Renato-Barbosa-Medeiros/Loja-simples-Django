No terminal: 
python -m venv venv 
.\venv\Scripts\Activate.ps1(PowerShell) ou venv\Scripts\activate.bat(CMD) 
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
