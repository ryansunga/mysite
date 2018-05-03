class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://<ryansunga>:'
        '<database ryansunga1>'
        '@<username>.mysql.pythonanywhere-services.com/'
        '<username>$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False