##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
