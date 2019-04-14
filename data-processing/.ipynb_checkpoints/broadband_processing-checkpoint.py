# This script processes a dataset available in an S3 bucket conataining         # information about broadband availability across the United States.            # Specifically, the data shows available broadband speeds,the broadband         # infrastrucure technologies, and the provider names for broadband systems      # across the more than 11 million US census blocks in the United States.


import re

def extract_transform_load_broadband(input_data_txt):


    rdd_BROADBAND = sc.textFile(input_data_txt)

    # This file is a comma separated file and has some commas embedded within       # string objects within some of the columns. The file is first read in to       # an RDD and this function is used in a map transformation (below) to           # remove those commas.

    def remove_commas(row):

        row = re.sub('(?!(([^"]*"){2})*[^"]*$),', '', row)

        return row

    # The first 11 numbers of a census block number match the 11 numbers in a       # census tract number. While the census block numbers in this file are 15       # digits long, the other datasets to be joined with this file for the           # database (containing housing data and zip codes) only have the 11 digit       # census tract data. Therefore, this function is used in a map                  # transformation (below) to keep only the first 11 numbers of the census        # block numbers. This column will be used to join this file by other files      # containing census tract numbers.

    def reduce_census_block_code(row):

        row[9] = row[9][:11]

        return row

    # This block removes the header, which is necessary for implementing the        # code below.

    header = rdd_BROADBAND.first()

    rdd_BROADBAND = rdd_BROADBAND.filter(lambda line: line != header)


    # This block of code removes ascii unicode information, removes commas          # embedded in within strings in some of the columns, splits the RDD object      # on the commas, and reduces the length of the census blocks from 15 to 11      # digits.

    rdd_transformed_BROADBAND = rdd_BROADBAND\
                                    .map(lambda x: x.encode('ascii', 'ignore'))\
                                    .map(lambda x: remove_commas(x))\
                                    .map(lambda x: x.split(','))\
                                    .map(lambda x: reduce_census_block_code(x))


    df_transformed_BROADBAND = spark.read.csv(rdd_transformed_BROADBAND, header=False, mode="DROPMALFORMED", sep=',', escape='"')


    # This code renames the columns I want to keep.

    df_transformed_BROADBAND = df_transformed_BROADBAND\
                                .withColumnRenamed("_c8", "state")\
                                .withColumnRenamed("_c9", "census_tract")\
                                .withColumnRenamed("_c10", "technology_code")\
                                .withColumnRenamed("_c12", "max_adver_downstr_speed")\
                                .withColumnRenamed("_c13", "max_adver_upstr_speed")\
                                .withColumnRenamed("_c15", "max_cir_downstr_speed")\
                                .withColumnRenamed("_c16", "max_cir_upstr_speed")


    # This code selects and saves just seven of the 16 columns from the original    # file that have some clear potential value for the database.


    df_transformed_BROADBAND = df_transformed_BROADBAND\
                                        .select(
                                        "census_tract",\
                                        "state",\
                                        "technology_code",\
                                        "max_adver_downstr_speed",\
                                        "max_adver_upstr_speed",\
                                        "max_cir_downstr_speed",\
                                        "max_cir_upstr_speed")
    
    df_transformed_BROADBAND.write\
                .mode("overwrite")\
                .save(output_data_txt)


def main():
    input_data_txt = sys.argv[1]
    output_data_txt = sys.argv[2]
    extract_transform_load_broadband(input_data_txt, output_data_txt)

if __name__ == '__main__':
    main()
