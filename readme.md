<!-- Please find attached a .PDF with the instructions for the take home test for the Cloud Data Engineering position at DASA. 
The test details the requirements on building an example ETL pipeline that can process the WikiMedia event stream in Python. 
The test will be used to gauge your knowledge of Python, SQL, Unix, ETL architecture, documentation, databases, and other useful skills. 
Please note that the test isn’t intended to be completed but do try to do as many of the tasks as you can within the time allotted. 
The product of this test should be a GitHub repository that contains your code and documentation submission. 
You will have three days to work on the test as much as you would like. 
Any time before midnight of the 6 th full day please check-in your submission to the repository and send me the URL. 
Updates or initial check-ins to the repository after midnight of the sixth day won’t be considered part of your test submission. 
TEST SUBMISSION CUTOFF: Midnight (UTC-3) May 31th You can use GCP, AWS, Azure services to solve the test. Ex: Pub/Sub, Kinesis, Spark, Dataflow, Glue, BigQuery, Athena, etc. If you choose to implement the test tasks using Cloud services please be sure to stay with the limits of the free tier those providers offers. 
Choosing to perform the test tasks outside of Cloud with a traditional BASH, Python, Docker technology stack will not have a negative impact on your test results. If you have any questions about the test please feel free to email me today or over the weekend. Good luck! -->

###### Discuss the planning of the task(s) that were completed and their final implementations.
**What is the goal?**
Get data from wikipedia and show/query it.
**What each task goal?**
*Task 1* - Answer some questions.
*Task 2* - Consume data from wikipedia api with some considerations.
*Task 3* - Save the data from wikipedia api into a database.
*Task 4* - Create a Graph in a webpage.
*Task 5* - Create a webpage where is possible make some queries.
*Task 6* - Containerize the pipeline (readstream data, save and show)

###### What were some of the design considerations?
I like to think in entire pipeline, so, could be good work on each task already containerize in order to save time, avoid issues, etc.

**Visualize**
 * https://github.com/apache/incubator-superset

**Query data**
 * https://github.com/azat-co/mongoui

###### Why was this technology stack chosen and implemented?
*Docker* -  We can run it anywhere, could be cloud platforms or on premise.
*Python* - Construction of etl process.
*Superset* - Visualize tool with some lovely graphs.
*MongoDB* - It is a ruge nosql database.


###### What are the pros/cons of this technology stack?
**pros**: 
    * Easy to use.
    * Possible vertical scaling.
    * Multi Platforms.
**cons**: 
    * Is not a distributed.
    * is not possible horizontal scaling
    * My acknologe in web applications.

###### What are some alternatives to the implemented technology stack?
Sure, cloud services for example Databricks, EMR, HDInsight and also Hortonworks Data Platform or Cloudera.

###### What are their strength's and weaknesses?
**strength**:
   * Environment
   * Simplicit
   
**Weaknesses**:
   * Performance

###Diagram
**Include a diagram of the overall pipeline that specifies the flow of the data and the architectural components of the stack.**
![](images/diagram.png)


<!-- Include installation instructions on how to install your code and dependencies. -->
<!-- All documentation and code should be checked into a Git compatible repository that is remotely accessible such as GitHub or BitBucket.
Documentation should be in Markdown ( .md ) format as a README.md at the root of the Git repository -->