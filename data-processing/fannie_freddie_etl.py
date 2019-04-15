#!/usr/bin/env python

# Reading the Fannie Mae and Freddie Mac housing datasets, transforming them, reading in the 
# relevant columns to a dataframe, and uniting those datasets into one.

# Data is available here: 


from pyspark.sql.functions import regexp_replace, col


pathname_FANNIE = 's3a://sparkforinsightproject/fnma_sf2017c_loans.txt'


pathname_FREDDIE = 's3a://sparkforinsightproject/fhlmc_sf2017c_loans.txt'


pathname_output_UNITED = 's3a://sparkforinsightproject/database_data/transformed_fhlmc_fnma_HOUSING_dataset'


def etl_fannie_freddie_data(input_FANNIE_txt, input_FREDDIE_txt, output_UNITED_txt):
    
    rdd_FANNIE_data = sc.textFile(input_FANNIE_txt)


    rdd_FANNIE_data = rdd_FANNIE_data.map(lambda x: x.encode('ascii', 'ignore'))\
                            .map(lambda l: l.split())\
                            .map(lambda l: (l[2] + l[4] + l[5], int(l[13]), int(l[36])))

    df_FANNIE_data = spark.read.csv(rdd_FANNIE_data, mode='DROPMALFORMED', sep=',', header=False)                                    .withColumn("_c0",regexp_replace(col("_c0"), "\(", ""))                                    .withColumn("_c2",regexp_replace(col("_c2"), "\)", ""))
    
        
    rdd_FREDDIE_data = sc.textFile(input_FREDDIE_txt)


    rdd_FREDDIE_data = rdd_FREDDIE_data.map(lambda x: x.encode('ascii', 'ignore')).                            map(lambda l: l.split()).                            map(lambda l: (l[2] + l[4] + l[5], int(l[13]), int(l[36])))

    df_FREDDIE_data = spark.read.csv(rdd_FREDDIE_data, mode='DROPMALFORMED', sep=',', header=False)                                    .withColumn("_c0",regexp_replace(col("_c0"), "\(", ""))                                    .withColumn("_c2",regexp_replace(col("_c2"), "\)", ""))
    

    
    # Join housing datasets, adding column headers, and writing to S3

    df_FRANNIE_FREDDIE_UNITED = df_FANNIE_data.union(df_FREDDIE_data)

    df_FRANNIE_FREDDIE_UNITED = df_FRANNIE_FREDDIE_UNITED.withColumnRenamed("_c0", "census_tract").                                                withColumnRenamed("_c1", "original_upb").                                                withColumnRenamed("_c2", "property_type")

    df_FRANNIE_FREDDIE_UNITED.show(10)

    df_FHLMC_FNMA_sf2017_UNITED.write\
     .mode("overwrite")\
     .save("s3a://sparkforinsightproject/database_data/transformed_fhlmc_fnma_HOUSING_dataset")

    
    
df_united_FANNIE_FREDDIE = etl_fannie_freddie_data(pathname_FANNIE, pathname_FREDDIE)
