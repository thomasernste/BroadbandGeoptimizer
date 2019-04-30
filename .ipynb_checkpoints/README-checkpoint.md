# Broadband Scout

### Problem Statement:

Every company strives for growth. In many cases, growth means expansion to new locations. And the huge property cost gap between large metropolitan areas and everywhere else makes it tempting for growing businesses to consider looking outside the city for new business locations, especially if the new location is something like a data center. But not every non-urbabn location has the extremely fast, reliable fiber optic broadband infrastructure that is required in modern data driven business environment

My project is aimed at helping companies and professionals research those areas outside of big cities with low property values that also have the kind of broadband infrastructure that's crucial to keeping businesses competitive in the modern business environment. Additionally, the database is augmented by other location-specific information about demographics and property costs that companies might use to compare potential new business locations.

### Solution:

Using a series of large, publically available datasets containing information including broadband speeds, housing values, a Housing Price Index, population data, demographics, and GPS coordinates, Broadband Scout is a tool that centralizes this disparate data together to help identify areas all across the United States that have a desirable combination of fast broadband speeds and other ideal locational features for their desires and needs.

With the use of AWS services and a series of compatible tools for big data processing, wrangling, storage, and querying, for this project I constructed a production-level data pipeline that's capable of processing these datasets and storing them in a database for business analytics purposes. Further, the functionality of the tools used allow for easy future enhancements to the database such as increasing the scale of the data by adding additional existing datasets or incorporating new data from APIs to ingest updated information.

### Data Pipeline:

This project was designed, first, to ingest and proecess several separate existing datasets with the infrastructure needed to easily extend the ingestion process to include streaming and rest API data. After ingestion of the data, the data is be pre-processed, stored in a database, and made available for queries by data scientists, companies, or anyone with an interest in finding the best place for them to live or work based on the data available in my database.

## **Cloud Architecture** 
![Amazon Web Services](https://assets.pcmag.com/media/images/408546-amazon-web-services-logo.jpg)


#### **File Storage System** 
![AWS S3](https://braze-marketing-assets.s3.amazonaws.com/images/partner_logos/amazon-s3.png)

      - Rationale: most obvious choice for working in AWS architecture


#### **Processing**   
![Spark](https://cdn-images-1.medium.com/max/1600/1*Pa7PO1v7bANI7C-eHMS_PQ.png)


      - Rationale:
                  - Enables extremely fast and reliable processing of historical datasets
                  - High throughput for data at massive scale
                  - Works seamlessly with AWS architecture
                  - With Spark Streaming, also capable of ingesting streaming and rest API data from multiple sources/APIs

                  

#### **DB Storage**  
![PostgreSQL](https://zdnet4.cbsistatic.com/hub/i/r/2018/04/19/092cbf81-acac-4f3a-91a1-5a26abc1721f/resize/370xauto/ce84e38cb1c1a7c5a2c9e4c337e108ba/postgresql-logo.png)


                  - Well-supported for facilitating analytics by data scientists
                  - Scalable for large storage needs
                  - Less expensive than other alternatives
                  
 #### **Front End**     
 ![Dash](https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_1540217128/plotly-dash.png)
