# Broadband Scout

### Problem Statement:

In recent years, the difference between property costs in large metropolitan areas and everywhere else has become more extreme than ever before. These low property costs outside of big cities can be attractive to companies that might be looking to build or buy a new facility, but one significant factor they can't overlook in choosing a new business site is the quality and speed of the broadband access in their chosen areas of interest. But do companies even know where to look to easily find this information?

This project seeks to help solve this problem. When a company decides they want to take advantage of the cost savings of setting up a business outside of the big city, Broadband Scout is an information database that companies can use to help make decisions about where they should build or buy a new building for their business.

### Solution:

Using a series of large, publically available datasets containing information all mapped by zip code and also including broadband speeds, housing values, population data, demographics, and GPS coordinates, Broadband Geoptimizer is a tool that centralizes this disparate data together to help people identify areas in the US that have a desirable combination of fast broadband speeds and an ideal location for their desires and needs.

With the use of AWS services and a series of compatible tools for big data processing, wrangling, querying, and storage, for this project I constructed a production-level data pipeline that's capable of ingesting and joining together these massive historical datasets. Further, it would be built to easily allow future enhancement -- that is, the tools used in my data pipeline will allow for higher future scalability and extensibility, meaning that I will be able to add additional existing datasets or data from APIs to ingest updated information.

### Data Pipeline:

This project was designed, first, to ingest and proecess several separate existing datasets with the infrastructure needed to easily extend the ingestion process to include streaming and rest API data. After ingestion of the data, the data is be pre-processed, stored in a database, and made available for queries by data scientists, companies, or anyone with an interest in finding the best place for them to live or work based on the data available in my database.

## **Cloud Architecture** 
![Amazon Web Services](https://assets.pcmag.com/media/images/408546-amazon-web-services-logo.jpg)


#### **File System** 
![AWS S3](https://braze-marketing-assets.s3.amazonaws.com/images/partner_logos/amazon-s3.png)

      - Rationale: most obvious choice for working in AWS architecture


#### **Ingestion**   
![Spark](https://cdn-images-1.medium.com/max/1600/1*Pa7PO1v7bANI7C-eHMS_PQ.png)


      - Rationale:
                  - Enables quick and reliable ingestion of historical datasets
                  - With Spark Streaming, also capable of ingesting streaming and rest API data from multiple sources/APIs
                  - High throughput for data at massive scale
                  - Works seamlessly with AWS
                  

#### **DB Storage**  
![Amazon Redshift](https://cdn.filestackcontent.com/Ahfkqi4FTFCMEb7GQrHm)


                  - Optimized for facilitating analytics by data scientists
                  - Fully scalable for a massive database
                  - Again, works seamlessly with AWS
                  
                  

### Stretch goals: 

      - Identify and incorporate other relevant datasets and/or sources of API data that could be incorporated based on 
      user feedback loops that may include requests for information not yet included in these datasets.
      mortgage/housing industries
      - Build custom, interactive User Interface using:
      
 ![Flask](https://cdn-images-1.medium.com/max/1200/1*0G5zu7CnXdMT9pGbYUTQLQ.png)
      

