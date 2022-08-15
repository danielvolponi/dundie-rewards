import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

def get_logger(logfile="dundie.log"):
    """Return a configured logger."""
    # ch = logging.StreamHandler() # Console/terminal/stdeer
    # ch.setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        logfile, 
        maxBytes=10**6, # 10 **6 (1mb)
        backupCount= 10
    )
    fh.setLevel(LOG_LEVEL)
    # ch.setFormatter(fmt)
    # log.addHandler(ch)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log