import logging, structlog, os

def setup_logging(level: str = "INFO"):
    logging.basicConfig(level=level, format="%(message)s")
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(getattr(logging, level.upper(), logging.INFO)),
        processors=[structlog.processors.JSONRenderer()]
    )

setup_logging(os.getenv("LOG_LEVEL","INFO"))
