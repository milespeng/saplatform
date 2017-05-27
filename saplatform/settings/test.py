DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autoops',
        'USER': 'miles',
        'PASSWORD': '4rfv5TGB',
        'HOST': 'rm-bp1ro67zwm41qb2ye.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    }
}

SALT_MASTER = '10.10.0.10'

SALTAPI_URL = 'https://127.0.0.1:8000'

SALTAPI_USER = 'salttest'

SALTAPI_PASSWORD = 'salttest'

BROKER_URL = 'redis://localhost:6379'

CELERY_RESULT_BACKEND = 'redis://localhost:6379'

CELERY_ACCEPT_CONTENT = ['application/json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Asia/Shanghai'
