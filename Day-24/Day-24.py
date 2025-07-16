
   #   ASSIGNMENT


#-->>  File Upload and Read CSV

df1 = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("dbfs:/Volumes/workspace/default/skitt/customers_2030-07-25.csv")
df2 = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("dbfs:/Volumes/workspace/default/skitt/customers_2030-07-26.csv")


#-->>  Add Extra Columns  and CREATE DELTA TABLE OKK

from pyspark.sql.functions import current_date, lit

df_customer = df1 \
    .withColumn("StartDate", current_date()) \
    .withColumn("EndDate", lit("2200-01-01")) \
    .withColumn("CurrentFlag", lit("Y"))

df_customer.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.Customer")

display(df_customer)

#-->>  READ DYNAMIC  FILE

dbutils.widgets.text("file_date", "2030-07-25", "Enter file date")
file_date = dbutils.widgets.get("file_date")
file_path = f"dbfs:/Volumes/workspace/default/skitt/customers_{file_date}.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)
# df.show()
spark.sql("SELECT * FROM default.customer").show()


#-->>  READ  OUTER TABLE / NEW DATA

df_OUTER = spark.read.format("delta").table("default.Customer")

df_OUTER.show()

# -->>  END DATE UPDATE H
from delta.tables import DeltaTable
from pyspark.sql.functions import lit


deltaTable = DeltaTable.forName(spark, "default.Customer")
deltaTable.update(
  condition = "CurrentFlag = 'Y'",
  set = {  "EndDate": lit(file_date),
           "CurrentFlag": lit("N")}
)

df_customer.write.format("delta") \
    .mode("append") \
    .saveAsTable("default.Customer")


# df = spark.read.format("delta").table("default.Customer")
# df.show(truncate=False)

spark.sql("SELECT * FROM default.Customer").show()