import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')


    @staticmethod
    def getUserEmail():
        return config.get('common info', 'useremail')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')
