# celebi_rest_api
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

//isteğe bağlı
ngrok indirin(https://ngrok.com/)
.ngrok http 8000
