# Databricks notebook source
import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import pyspark.pandas as ps

# COMMAND ----------

# MAGIC %md
# MAGIC loading data

# COMMAND ----------

df = pd.read_parquet("https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/bing_covid-19_data/latest/bing_covid-19_data.parquet")
df.head(10)

# COMMAND ----------

df.dtypes

# COMMAND ----------

df_country=df[df['country_region']!='Worldwide']
df_country.head(10)

# COMMAND ----------

psdf = ps.DataFrame(df_country)
display(psdf)

# COMMAND ----------

# MAGIC %md
# MAGIC Plot by countries

# COMMAND ----------

psdf_confirm=psdf.groupby('country_region').sum().sort_values(by='confirmed',ascending=False).head(20)
psdf_death=psdf.groupby('country_region').sum().sort_values(by='deaths',ascending=False).head(20)

# COMMAND ----------

display(psdf_confirm.reset_index())

# COMMAND ----------

display(psdf_death.reset_index())

# COMMAND ----------

# MAGIC %md
# MAGIC Plot worldwide tendency

# COMMAND ----------

df_world=df[df['country_region']=='Worldwide']

# COMMAND ----------

df_world.plot(kind='line',x='updated',y="confirmed",grid=True)
df_world.plot(kind='line',x='updated',y="deaths",grid=True)
df_world.plot(kind='line',x='updated',y="confirmed_change",grid=True)
df_world.plot(kind='line',x='updated',y="deaths_change",grid=True)
df_world.plot(kind='line',x='updated',y="recovered",grid=True)
df_world.plot(kind='line',x='updated',y="recovered_change",grid=True)
