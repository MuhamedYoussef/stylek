from .base import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
ADMINS = (
    ('Mohamed Youssef', 'mu7med.youssef@gmail.com'),
)
ALLOWED_HOSTS = ['stylek.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd76mfks8rtte5d',
        'HOST': 'ec2-54-246-90-194.eu-west-1.compute.amazonaws.com',
        'USER': 'zulmecxfwnskpp',
        'PASSWORD': '3057bf8e4de4f957bd56f213474367f67143f41f965ba3afd5b029aea31fef38',
    }
}
