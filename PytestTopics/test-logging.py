import logging

LOGGER = logging.getLogger(__name__)


def test_mylogging():
    LOGGER.info("Info Logs")
    LOGGER.warning("Warning Logs")
    LOGGER.error("Error Logs")
    assert True
