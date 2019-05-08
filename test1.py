# coding:utf-8

import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    for attr in dir(logger):
        print "{}: {}".format(attr, logger.__getattribute__(attr))
    logger.error('set a new file')
