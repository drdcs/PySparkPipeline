# Distribution of Executors, Cores and Memory for a Spark Application running in Yarn:

```bash
spark-submit --class <CLASS_NAME> --num-executors ? --executor-cores ? --executor-memory ? ....
```

Following list captures some recommendations to keep in mind while configuring them:
* **Hadoop/Yarn/OS Deamons** : When we run spark application using a cluster manager like Yarn, there’ll be several daemons that’ll run in the background like NameNode, Secondary NameNode, DataNode, JobTracker and TaskTracker. So, while specifying num-executors, we need to make sure that we leave aside enough cores (~1 core per node) for these daemons to run smoothly.
* **Yarn ApplicationMaster (AM** : ApplicationMaster is responsible for negotiating resources from the ResourceManager and working with the NodeManagers to execute and monitor the containers and their resource consumption. If we are running spark on yarn, then we need to budget in the resources that AM would need (~1024MB and 1 Executor).
* **HDFS Throughput** : HDFS client has trouble with tons of concurrent threads. It was observed that HDFS achieves full write throughput with ~5 tasks per executor . So it’s good to keep the number of cores per executor below that number.


### Ever wondered how to configure --num-executors, --executor-memory and --execuor-cores spark config params for your cluster?

```
** Cluster Config:**
10 Nodes
16 cores per Node
64GB RAM per Node
```

According to the recommendations which we discussed above:

* Based on the recommendations mentioned above, Let’s assign 5 core per executors => --executor-cores = 5 (for good HDFS throughput)
* Leave 1 core per node for Hadoop/Yarn daemons => Num cores available per node = 16-1 = 15
* So, Total available of cores in cluster = 15 x 10 = 150
* Number of available executors = (total cores/num-cores-per-executor) = 150/5 = 30
* Leaving 1 executor for ApplicationManager => --num-executors = 29
* Number of executors per node = 30/10 = 3
* Memory per executor = 64GB/3 = 21GB
* Counting off heap overhead = 7% of 21GB = 3GB. So, actual --executor-memory = 21 - 3 = 18GB
* So, recommended config is: 29 executors, 18GB memory each and 5 cores each!!

* **Analysis**: It is obvious as to how this third approach has found right balance between Fat vs Tiny approaches. 
