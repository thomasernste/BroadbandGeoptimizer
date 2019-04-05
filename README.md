# Broadband Geoptimizer

## (Alternate title: Broadband GeoValueOptimizer)

### Problem Statement:
In recent years, the distribution of property costs between large metropolitan areas and everywhere else has become more extreme than ever before (need a source). For some people, the costs of living in or near the center of the city are worth the benefits. But increasingly, these skyrocketing costs are pushing businesses and their employees to consider other options.

In the 21st century, when families and businesses decide where they'd like to live or run a business, it has become essential that they must consider the availability of high-speed, quality broadband in any geographic area they might consider. Companies and individual workers seeking to find areas in the country that have the combination of low property values and high broadband speeds need information to help inform those decisions. While all businesses and people would like to keep their broadband speeds high and property values as low as possible, they might have some other different wants and needs. For example, here are two possible combinations:

(1) Some may want to find places with the fast broadband and cheap living that are located far away from any major cities. These might be remote workers who want to live out in the woods, for example.

(2) Others may want to live close enough to a major city -- maybe within 50 miles from a city -- but still have relatively low property values and fast broadband.


### Solution:

Using a series of large, publically available datasets containing information all mapped by zip code and also including broadband speeds, housing values, population data, and GPS coordinates, Broadband Geoptimizer is a tool that centralizes this disparate data together to help people identify areas in the US that have a desirable combination of fast broadband speeds and an ideal location for their desires and needs.

With the use of AWS services and a series of compatible tools for big data processing, wrangling, querying, and storage, this project will construct a production-level data engineering pipeline that's capable of ingesting and joining together these massive historical datasets. Further, it would be built to easily allow future enhancement -- that is, the tools used in my data pipeline will allow for high scalability and extensibility, meaning that I will be able to add additional existing datasets or data from APIs to ingest updated information.  After ingestion of the data, the data will be pre-processed, stored in a database, and made available for queries by data scientists, companies, or anyone with an interest in finding the best place for them to live or work.


### Data Pipeline:

This project will be designed, first, to ingest and proecess several separate existing datasets with the infrastructure needed to easily extend the ingestion process to include streaming and rest API data. It will also facilitate the efficient processing of unclean data and storage in a database equipped for extreme scalability, customized interactive queries, and real-time calculations performed by data scientists..  Based on these needs for my pipeline, I propose the following tools for my pipeline:

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
      

