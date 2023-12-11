# Databricks notebook source
# MAGIC %md
# MAGIC Chapter 6: Feature Engineering
# MAGIC
# MAGIC ##Synthetic data - Updating to Feature Tables

# COMMAND ----------

# MAGIC %md ## Run Setup

# COMMAND ----------

# MAGIC %run ../../global-setup $project_name=synthetic_transactions $catalog=lakehouse_in_action

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE transaction_count_ft ALTER COLUMN CustomerID SET NOT NULL;
# MAGIC ALTER TABLE transaction_count_ft ADD PRIMARY KEY(CustomerID);
# MAGIC
# MAGIC ALTER TABLE transaction_count_history ALTER COLUMN CustomerID SET NOT NULL;
# MAGIC ALTER TABLE transaction_count_history ALTER COLUMN eventTimestamp SET NOT NULL;
# MAGIC ALTER TABLE transaction_count_history ADD PRIMARY KEY(CustomerID, eventTimestamp TIMESERIES);

# COMMAND ----------


