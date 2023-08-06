from app_logger import logger
from connectors import postgresDB,keydb
from config import settings


def check_logging():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")


def get_records():
    print("Getting connection")
    with postgresDB.get_db_connection(server = "localhost",port = 5432,user="default",password = "default1",database = "default") as cursor:
        print("running query")
        cursor.execute("select * from employee")
        res = cursor.fetchone()
        print(res)


def get_keydb_key():
    kdb = keydb.KeyDB()
    x = kdb.get("mykey")
    print("Mykey is ", x)


if __name__ == "__main__":
    print(settings)
    get_records()
    check_logging()
    get_keydb_key()
    print("Process finsihed")
