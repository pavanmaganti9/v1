import logging

# NOTSET (Numeric Value =  0)
# DEBUG (Numeric Value = 10)  -- detailed info
# INFO  (Numeric Value = 20 )  -- confirmation that things according to plan
# WARNING (Numeric Value = 30 )  -- something unexpected
# ERROR  (Numeric Value =  40)  -- some function failed
# CRITICAL (Numeric Value =  50)  -- something failed application must close

logging.basicConfig(filename='logfile.log',level=logging.DEBUG)

def main():
    try:
        logging.debug('We are in try loop')
        if 1<2:
            logging.debug('entered first if stmt')
        else:
            logging.debug('entered second if stmt')
    except Exception as e:
        logging.critical(str(e))

main()
