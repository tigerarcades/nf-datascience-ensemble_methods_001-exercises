import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

pq.write_table(
    pa.Table.from_pandas(
        pd.read_csv('https://s3.amazonaws.com/projects-rf/clean_data.csv')),
    'data/public-health-surveys_2011-2015.parquet')
