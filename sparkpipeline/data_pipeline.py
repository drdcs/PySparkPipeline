
from pyspark.sql import SparkSession
from pipeline import ingest
import logging
import logging.config


class Pipeline:

    logging.config.fileConfig("pipeline/resources/configs/logging.conf")

    def run_pipeline(self):
        try:
            logging.info("starting the pipeline")
            print("Running Pipeline")
            ingest_process = ingest.Ingest(self.spark)
            df1= ingest_process.ingest_from_mysql()
            df1.show()
            # tranform_process = transform.Transform(self.spark)
            # df = tranform_process.transform_data(df1)
            # persist_process = persist.Persist(self.spark)
            # persist_process.persist_data(df)
            # return
        except Exception as exp:
            logging.error("An error occured while running the pipeline " + str(exp))

    def create_spark_session(self):
        self.spark = SparkSession.builder.master("local[2]")\
            .config("spark.driver.extraClassPath", "external_jars\mysql-connector-java-8.0.22.jar" )\
            .appName("my first spark app")\
            .getOrCreate()


if __name__ == '__main__':
    logging.info("Application Started .. ")
    logging.warning("Application Started with warning.")
    logging.error("Application Started With Error..")
    pipeline = Pipeline()
    pipeline.create_spark_session()
    pipeline.run_pipeline()

