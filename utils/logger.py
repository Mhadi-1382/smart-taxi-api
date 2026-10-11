
'''Provides logging configuration and utilities.'''

from loguru import logger

LOG_TYPE = {
    'ERROR': 'ERROR',
    'CRITICAL': 'CRITICAL',
    'WARNING': 'WARNING',
    'INFO': 'INFO',
    'SUCCESS': 'SUCCESS'
}

logger.add('log.log')

def generate_log(text: str = None, log_type: str = LOG_TYPE):
    logger.log(log_type, text)
