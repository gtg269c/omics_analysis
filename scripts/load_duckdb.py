"""
script to load data into duckdb
"""

import pandas
import duckdb

# Specify the Parquet file path and the size of each chunk to read
parquet_file = '/mnt/d/Research/Omics/Xena/data/file_tpm_pheno_gene_pqt.parquet'
database_name = '/mnt/d/Research/Omics/Xena/data/TcgaTargetGtex_xena.duckdb'
# query data from parquet and save to duckdb table
# load_query = """
#     CREATE OR REPLACE TABLE stt3a_gtex_table
#     AS SELECT tpm, gene, _study, _primary_site
#     FROM parquet_scan('{}')
#     WHERE gene = 'STT3A' AND _study = 'GTEX'
#     """.format(input_file)

chunk_size = 1000

# Connect to DuckDB in memory database
conn = duckdb.connect(database=database_name, read_only=False)

# create table in duckdb and load data from parquet
# conn.execute("CREATE OR REPLACE TABLE gtex_table AS SELECT tpm, gene, _study, _primary_site FROM parquet_scan('{}') WHERE _study = 'GTEX'".format(parquet_file))

# count records in duckdb table
df = conn.execute("SELECT COUNT(*) FROM gtex_table WHERE gene='SPTLC1'").df()
print(f"Number of records in duckdb table: {df}")

# conn = duckdb.connect(database=":memory:", read_only=False)
# conn.execute(
#     'CREATE OR REPLACE TABLE gtex_table (tpm FLOAT, gene STRING, _study STRING, _primary_site STRING, detailed_category STRING)')

# # Read the Parquet file in chunks and insert each chunk into the DuckDB table
# with pq.ParquetFile(parquet_file) as pf:
#     for i in range(pf.num_row_groups):
#         start = i * chunk_size
#         end = min(start + chunk_size, pf.metadata.num_rows)
#         table = pf.read(columns=['tpm', 'gene', '_study',
#                         '_primary_site', 'detailed_category'], row_group=i, start=start, stop=end)
#         rows = [tuple(row) for row in table]
#         query = f"INSERT INTO stt3a_gtex_table VALUES {','.join(['(?,?,?,?)']*len(rows))}"
#         conn.execute(query, rows)

# # count the number of rows in the parquet file using duckdb
# conn.execute(
#     "SELECT COUNT(*) FROM parquet_scan('{}')".format(parquet_file)).fetchall()
