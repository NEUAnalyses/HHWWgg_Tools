import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

f = "test.parquet"

np_arr = np.array([1.3, 4.22, -5], dtype=np.float32)
pa_table = pa.table({"data": np_arr})
pa.parquet.write_table(pa_table, f)

table = pq.read_table(f)
print("table:",table)