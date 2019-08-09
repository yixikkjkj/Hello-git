# coding: utf-8

import logging

from unittest.mock import Mock, patch

logger = logging.getLogger(__name__)


def tobetest(need, *args, **kwargs):
    logger.info(need)
    logger.info(args)
    logger.info(kwargs)
    return 10


def use_tobetest():
    return tobetest('this is nedddd', 1, 2, cb=3, real=4)


def side_effect_func(*args, **kwargs):
    return 100


@patch('mocktest.tobetest', side_effect=side_effect_func)
def test_tobe_test(mock_patched):
    logger.info(mock_patched)
    assert use_tobetest() == 100
    assert mock_patched.called == True
