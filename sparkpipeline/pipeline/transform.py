import logging
import logging.config


class Transform:

    logging.config.fileConfig("pipeline/resources/configs/logging.conf")

    def __init__(self,spark):
        self.spark=spark

    def transform_data(self,df):
        logger = logging.getLogger("Transform")
        logger.warning("Testing error message from Transform .. ")
        logger.error("Testing error message from Transform .. ")
        print("Transforming")
        # drop all the rows having null values
        df1 = df.na.drop()
        return df1