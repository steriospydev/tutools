import logging

def log_example() -> None:
  logging.basicConfig(
      level=logging.DEBUG,
      format="%(asctime)s %(levelname)s %(message)s",
      datefmt="%Y-%m-%d %H:%M:%S",
      filename="basic.log"
      )
  logging.debug("This is a debug message")
  logging.info("This is a info message")
  logging.warning("This is a warning message")
  logging.error("This is an error message")
  logging.critical("This is a critical message")

log_example()