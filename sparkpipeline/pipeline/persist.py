
import logging
import logging.config
import sys

class Persist:

    logging.config.fileConfig("pipeline/resources/configs/logging.conf")

    def __init__(self,spark):
        self.spark=spark

    def persist_data(self,df):
        logger = logging.getLogger("Transform")
        logger.info("starting the pipeline")
        try:
            df.coalesce(1).write.option("header", "true").csv("transformed_retailstore")
        except Exception as ex:
            # logger.error("An error occured while persisting data "+ str(ex))
            raise Exception
            sys.exit(1)