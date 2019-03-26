# From Messy, Fragmented Data Lakes to Cleansed, Integrated Databases: Making Sense of Mortgage and Housing Information With Big Data

### Problem Statement:

A persistent problem for companies from all industries is that while there is really no shortgage of accessible, interesting information in the "big data" age, most organizations continue to experience problems of messiness and fragmentation of the accessible data. In effect, in many cases, the data may as well be inaccessible.

The housing industry is one example of an industry with persistent problems dealing with unclean data from a fragmented ocean of historical datasets and APIs. Fannie Mae and Freddie Mac have massive datasets containing data involving acquisitions and performance of mortgages over the past few decades, for example, and important insights can be drawn from these datasets about trends in housing values. But the utility of such datasets can be enhanced when joined with demographic data from datasets such as the American Housing Survey and the General Social Survey.

The insights that data scienctists can glean from advanced analytics methods can improve a company's understanding of their industry, but making such strives is highly dependent not only on accessing the information that can fuel these insights but having the data cleaned and ready to go in a database that allows queries and analysis of massive datasets.

types of companies, their data science teams, and the general public as a whole have an interest in having fair and accurate housing valuations. However, prior to the rise of big data, the process of determining housing values was a somewhat unscientific process determined by lenders, realtors, and a set of standards that lacked sufficient information. And besides the basic goal of people wanting to get their fair money's worth out of their homes and the industry seeking better standards, problems like the housing bubble burst that occurred in the United States around 2006 were arguably due at least in part to artificially inflated housing values that were the product of a inadequately informed valuation process. In that sense, accuracy in housing values

As big data exploded and new forms of data science developed, one way that data science professionals and students have sought to apply data science has been to create machine learning models aimed at predicting the sale price of housing. Further, finding methods for improving predictions of housing values can lead to better information to inform the process of setting informed standards for determining housing values. These  efforts have led to the creation of existing machine learning models with relatively high degrees of predictive accuracy. However, many of these efforts to develop machine learning models for predicting housing prices have been applied to relatively small-scale data. Building machine learning models that can scale for massive amounts of data presents numerous challenges.

### Solution:

We can put one or more of these machine learning models into a production-level data engineering pipeline that's capable of handling massive amounts of streaming and rest API data from multiple real estate APIs. Data can be stored in a database and combined with new data coming in and data scientists could then refine their machine learning model (or models) on existing and newly incoming data.


### Data Pipeline:

This project will be designed, first, to ingest and proecess massive amounts of streaming and rest API data from multiple real estate APIs, such as Zillow.com, Trulia.com, Attomdata.com. It will also facilitate processing of stream and restful data processing, clean the data as it comes in, enabling real-time training of the machine learning model on that data, allowing adjustments to the model (or models) by data scientists as needed, and store historical data in a database that can become the basis of a very robust machine learning model for predicting housing values.  Based on these needs for my pipeline, I propose the following tools for my pipeline:

- **File System** -------------> AWS S3 

      - Rationale: most obvious choice for working in AWS architecture


- **Ingestion** ---------------> Kafka

      - Rationale:
                  - Enables quick and reliable ingestion of streaming and rest API data from multiple sources/APIs
                  - High throughput for data at massive scale
                  - Works seamlessly with Kafka Streams and KSQL (which enables data wrangling on streaming and rest API  
                    data with SQL)


- **Stream Processing** -------> Kafka Streams / KSQL
                  
      - Rationale:
                  - Works seamlessly with Kafka's ingestion tool and KSQL
                  - It's light-weight
                  - Enables *real-time analytics*, allowing for data scientists to tweak MLM training model on 
                    streaming/rest API data
                  - *Widespread adoption* of Kafka means that many organizations could see potential for running their  
                    machine learning projects on this kind of pipeline
                  - KSQL allows for real-time data wrangling using SQL queries, allowing for necessary data cleaning of data                     requiring application of regular expressions, removing characters, filtering, joins of dataframes from
                    multiple APIs, and more 
                    

- **Scheduling/Monitoring** ---> Airflow

                  - Necessary for scheduling data pulls from some APIs that have limits on data requests
                  - Works well with Kafka tools
                  - Its UI enables visualization, monitoring, and troubleshooting of a production-level pipeline
                  - Allows SQL queries
               

- **DB Storage** --------------> Amazon Redshift

                  - Integrated with analytics within AWS and optimized for analytics
                  - Fully scalable for a massive database


### MVP:

      - Use a single machine learning model and data from at least two real estate APIs

### Stretch goals: 

      - Muliple machine learning models
      - Multiple versions of each machine learning model
      - Add data from additional APIs that may be available
      

