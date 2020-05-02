class Config(object):
    DEBUG = False
    TESTING = False
    TESSERACT_ROUTE = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    SUNAT_URL_IMG = 'https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image&magic=2'
    SUNAT_URL_INFO = 'http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias?accion=consPorRuc&nroRuc={0}&codigo={1}'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
