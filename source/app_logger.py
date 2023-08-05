import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    filename="/home/jayaram/app_data_loader/example.log",
    encoding="utf-8",
    filemode="w",
    level=logging.DEBUG,
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
logger = logging.getLogger(__name__)
