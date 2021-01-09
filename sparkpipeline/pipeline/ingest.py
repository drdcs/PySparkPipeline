import logging
import logging.config
import configparser


class Ingest:

    logging.config.fileConfig("pipeline/resources/configs/logging.conf")


    def __init__(self,spark):
        self.spark=spark

    def ingest_data(self):
        logger = logging.getLogger("Ingest")
        logger.info("Info message from ingestion..")
        logger.warning("Warning message from ingestion..")
        logger.error("Error message from ingestion..")

    def ingest_from_mysql(self):

        try:

            logger = logging.getLogger("Ingest")
            logger.info("started reading from config file..")

            config = configparser.ConfigParser()
            config.read('pipeline/resources/pipeline.ini')
            target_url = config.get('DB_CONFIGS', 'SOURCE_MYSQL_URL')
            target_table = config.get('DB_CONFIGS', 'SOURCE_MYSQL_TABLE')
            target_username = config.get('DB_CONFIGS', 'SOURCE_MYSQL_USERNAME')
            target_password = config.get('DB_CONFIGS', 'SOURCE_MYSQL_PASSWORD')

            print(target_url)

            jdbcdf = self.spark.read.format("jdbc")\
                .option("url",target_url)\
                .option("dbtable", target_table)\
                .option("user", target_username) \
                .option("password", target_password)\
                .load()
            return jdbcdf

        except Exception as ex:

            logger.error("An error occured " + str(ex))
            raise Exception("Connection Failure.")
