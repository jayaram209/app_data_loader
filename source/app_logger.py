import logging
from pathlib import Path

file_name = str(Path(r'C:\Users\email\Downloads').parent) + "/app_logs.log"
logging.basicConfig(
    format="%(asctime)s %(message)s",
    filename=file_name,
    encoding="utf-8",
    filemode="a",
    level=logging.DEBUG,
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
logger = logging.getLogger(__name__)
