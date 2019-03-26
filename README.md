# From Messy, Fragmented Data Lakes to Cleansed, Integrated Databases: Making Sense of Mortgage and Housing Information With Big Data Engineering

### Problem Statement:

A persistent problem for companies and researchers from all industriesis that while there is really no shortgage of accessible, interesting information in the "big data" age, most organizations continue to experience problems of messiness and fragmentation of the accessible data. I many cases, much of the data that's technically available to use may as well be inaccessible for all intents and purposes.

The housing industry is one example of an industry with persistent problems dealing with unclean data from a fragmented ocean of historical datasets and APIs. Fannie Mae and Freddie Mac have massive datasets containing data involving acquisitions and performance of mortgages over the past few decades, for example, and important insights can be drawn from these datasets about trends in housing values. But the utility of such datasets can be enhanced when joined with demographic data from datasets such as the American Housing Survey and the General Social Survey or housing data from real estate sites like Zillow.com.

The insights that data scienctists can glean from advanced analytics methods on such joined datasets can improve a company's understanding of their industry and business goals, but making such strives is highly dependent not only on accessing the information that can fuel these insights but having the data cleaned and ready to go in a database that allows queries and analysis of massive datasets.

### Solution:

With the use of AWS services and a series of compatible tools for big data processing, wrangling, querying, and storage, this project will construct a production-level data engineering pipeline that's capable of ingesting and joining together numerous massive datasets from historical datasets and potentially streaming and rest API data.  The data will be pre-processed, stored in a database, and readied for queries by data scientists who would like to glean insights from the data.


### Data Pipeline:

This project will be designed, first, to ingest and proecess massive amounts of streaming and rest API data from multiple real estate APIs, such as Zillow.com, Trulia.com, Attomdata.com. It will also facilitate processing of stream and restful data processing, clean the data as it comes in, enabling real-time training of the machine learning model on that data, allowing adjustments to the model (or models) by data scientists as needed, and store historical data in a database that can become the basis of a very robust machine learning model for predicting housing values.  Based on these needs for my pipeline, I propose the following tools for my pipeline:

- **File System** -------------> AWS S3 

      - Rationale: most obvious choice for working in AWS architecture


- **Ingestion** ---------------> Spark

      - Rationale:
                  - Enables quick and reliable ingestion of historical datasets
                  - With Spark Streaming, also capable of ingesting streaming and rest API data from multiple sources/APIs
                  - High throughput for data at massive scale
                  - Works seamlessly with AWS
                  

- **DB Storage** --------------> Amazon Redshift

                  - Optimized for facilitating analytics by data scientists
                  - Fully scalable for a massive database
                  - Again, works seamlessly with AWS

### MVP:

      - Combine and clean datasets from at least 4 sources including 2 sources of mortgage and real estate data
        (Fannie Mae and Freddie Mac for Mortgage Data and Zillow for real estate) and 2 sources of demographic data including 
        the American Housing Survey and the General Social Survey).

### Stretch goals: 

      - Identify and incorporate other relevant datasets that could enhance my insights into the mortgage/housing industries
      - Find additional novel questions to ask about the data toward demonstrating business value
      - Add data from APIs as available
      

