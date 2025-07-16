  #    ASSIGNMENT


import os
os.environ["SPARK_VERSION"] = "3.3"

from pyspark.sql.functions import col
from delta.tables import DeltaTable

dbutils.widgets.text("arrival_date", "2024-07-25")
input_date = dbutils.widgets.get("arrival_date")

booking_path = f"/Volumes/workspace/default/my/booking/bookings_{input_date}.csv"
customer_path = f"/Volumes/workspace/default/my/customer/customers_{input_date}.csv"

def load_csv(path: str):
    return spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .option("multiLine", "true") \
        .option("quote", "\"") \
        .option("escape", "\"") \
        .load(path)

booking_df = load_csv(booking_path)
customer_df = load_csv(customer_path)

display(booking_df)
display(customer_df)

def count_nulls(df, col_name):
    nulls = df.filter(col(col_name).isNull()).count()
    print(f"Null values in '{col_name}': {nulls}")
    return nulls

for column in ["booking_id", "customer_id", "amount"]:
    count_nulls(booking_df, column)

essential_cols = ["booking_id", "amount"]
clean_df = booking_df.dropna(subset=essential_cols).dropDuplicates(["booking_id"])

def upsert_to_delta(target_table: str, source_df):
    if not spark._jsparkSession.catalog().tableExists(target_table):
        source_df.write.format("delta").mode("overwrite").saveAsTable(target_table)
    else:
        delta_tbl = DeltaTable.forName(spark, target_table)
        delta_tbl.alias("target").merge(
            source_df.alias("source"),
            "target.booking_id = source.booking_id"
        ).whenMatchedUpdateAll() \
         .whenNotMatchedInsertAll() \
         .execute()

upsert_to_delta("workspace.default.skittt", clean_df)

display(spark.sql("SELECT * FROM workspace.default.skittt"))
