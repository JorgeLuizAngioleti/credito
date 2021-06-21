# credito
Empréstimos genérico

#para  rodar o projeto no window
<p align="justify"> 
$ git clone https://github.com/JorgeLuizAngioleti/credito.git
cd credito
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
</p>
