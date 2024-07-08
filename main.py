from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Initialize Spark Session
spark = SparkSession.builder.appName('music_streaming_etl').getOrCreate()

# Load data from Spotify API
spotify_df = spark.read.json('spotify_data.json')

# Load data from Apple Music API
apple_df = spark.read.json('apple_music_data.json')

# Load data from Tidal API
tidal_df = spark.read.json('tidal_data.json')

# Clean and transform the data
def clean_transform_data(df):
    return df.dropna() \\
              .withColumn('streams', df['streams'].cast('integer')) \\
              .withColumn('date', to_date(df['date'], 'MM/dd/yyyy')) \\
              .filter(col('streams') > 0)

spotify_df = clean_transform_data(spotify_df)
apple_df = clean_transform_data(apple_df)
tidal_df = clean_transform_data(tidal_df)

# Combine all data into one DataFrame
combined_df = spotify_df.union(apple_df).union(tidal_df)

# Load the data into a data warehouse (HDFS)
combined_df.write.parquet('hdfs://localhost:9000/user/music_streaming_data')
