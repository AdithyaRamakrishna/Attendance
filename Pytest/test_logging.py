import logging


def test_demoLogging():

    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('file.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    # logger.setLevel(logging.CRITICAL)    # this will execute from Critical
    logger.setLevel(level='INFO')  # this will execute from info
    logger.debug('this is debug message')
    logger.info('this is information')
    logger.warning('this is a warning')
    logger.error('An error happened')
    logger.critical('Its Critical')