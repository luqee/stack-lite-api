import os

class BaseConfig(object):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class TestConfig(BaseConfig):
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
}