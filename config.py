# DB Config
db = {
    'user': 'bowl',
    'password': 'bowling!@#',
    'host': '121.66.185.30',
    'port': 5432,
    'database': 'bowlingdb'
}

DB_URL = f"postgresql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"


class Config:
    DEBUG = False
    from swagger import swagger_config
    SWAGGER = swagger_config

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'

    @classmethod
    def init_app(cls, app):
        print('[Dev Config]THIS APP IS IN DEBUG MODE.')


config = {
    'dev': DevConfig,
    'default': DevConfig
}
