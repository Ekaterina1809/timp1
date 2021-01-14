import os
class Configuration():
    APPLICATION_DIR=os.path.dirname(os.path.realpath(__file__))
    DEBUG=True
    #SQLALCHEMY_DATABASE_URL='sqllite:///%s/cookie.db?check_some_thread=False' % APPLICATION_DIR
