#change format of log message
import logging
logging.basicConfig(filename='app.log',
                    level=logging.DEBUG,
                    filemode='w',
                    format="%(name)s:%(levelname)s:%(message)s")    #changing the level #10#a

logging.debug("this is debug message")
logging.info('the info message is displaying')
logging.warning('the warning message is displaying')
logging.error('the error message is displaying')
logging.critical('the critical meassge is displaying')