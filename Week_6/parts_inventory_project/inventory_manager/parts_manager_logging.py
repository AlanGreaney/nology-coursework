import datetime
import logging
import csv
import io

class csvFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.output = io.StringIO()
        self.writer = csv.writer(self.output, quoting=csv.QUOTE_ALL)

    def format(self, record):
        self.writer.writerow([record.levelname, datetime.datetime.now(), record.msg])
        data = self.output.getvalue()
        self.output.truncate(0)
        self.output.seek(0)
        return data.strip()

def setup_logger(name, log_file, formatter = False, level=logging.INFO):
    handler = logging.FileHandler(log_file)        

    if formatter:
        handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def sqlLoggingWrapper(cursor, query, params):
    logger.info("NoSQL Query being made: " + query + " - with the parameters:")
    logger.info(params)
    cursor.execute(query, params)
