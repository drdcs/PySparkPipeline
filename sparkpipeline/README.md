## Data Pipeline Python Structure

<font color="red"> <b>Folder structure </b> </font><br> </br>

- sparkpipeline - project name
- data_pipeline.py - main entry point of programme
- external_jars - jar files like driver, kafka-client etc.
- pipeline folder - split ingestion, transformation and load py files.
- resources folder 
    - pipeline.ini for externalize configuration.
    - configs for logging mechanism

```
\---sparkpipeline
    |   data_pipeline.py
    +---external_jars
    |       mysql-connector-java-8.0.22.jar
    |       
    +---pipeline
    |   |   ingest.py
    |   |   persist.py
    |   |   transform.py
    |   |   
    |   +---resources
    |   |   |   pipeline.ini
    |   |   |   
    |   |   \---configs
    |   |           logging.conf          

```
Once the task is over move the python and config files to the cluster environment.

<font color="blue"> spark-submit data_pipeline.py </font><br> </br>
