class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://ryansunga:'
        'databasepw'
        '@ryansunga.mysql.pythonanywhere-services.com/'
        'ryansunga$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False