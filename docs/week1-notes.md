## Course Introduction
* [⏺️ Session 1 Zoom Recording, March 2, 2022](https://vimeo.com/686322038)
  * [👨‍🏫 Course Intro Slides](https://docs.google.com/presentation/d/1Outh5yuWk0CBXMpp6JeY0u6aqPJH1ilcMJGPUN_74gc/edit?usp=sharing)

## Workshop A: Getting Started with Databricks and Spark

### Section 1:  Configuring Spark Clusters in Databricks
* [⏺️ Session 2 Zoom Recording, March 7, 2022](/user164883159/review/686307561/b5cff3b0f8)
  * [👨‍🏫 Spark Databricks Clusters Slides](https://docs.google.com/presentation/d/1a9bBh3Vsy3xpBLZsVvop7a0zdAH1Fdzsq5eNx1Om7kY/edit?usp=sharing)
  * [Office hours Recording, March 8, 2022](https://us06web.zoom.us/rec/play/Nl0FkENcFg8pytAbvRpKrDw6pgBmf2BGfpYWCjBBpxSgb6lp6ni26xtPJKdrYDjLfwZTWuamweOwtF2i.I0HEmOa77A4ansnq?startTime=1646780516000&_x_zm_rtaid=9azCc9IcQ1up30PvmIZJHg.1651796642444.be21de1877d6295b141e6fcf3f381853&_x_zm_rhtaid=598)
* [Cluster Configuration](https://github.com/FourthBrain/HAL-MLOps/blob/main/docs/creating_clusters.md)
* [Databricks Clusters Azure Docs](https://docs.microsoft.com/en-us/azure/databricks/clusters/)

### Section 2:  Using Databrick Notebooks
* [⏺️ Session 3 Zoom Recording, March 9, 2022](https://vimeo.com/701806807)
  * [👨‍🏫 Spark Databricks Notebooks Slides](https://docs.google.com/presentation/d/1hgXX5cdcukZCQQhF6VZMNn9A8gLRVVoFe46Z2cHIZd4/edit?usp=sharing)
* [Databrick Notebooks Azure Docs](https://docs.microsoft.com/en-us/azure/databricks/notebooks/)
* [CI/CD for Databricks](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/ci-cd-jenkins)

### Section 3: Using Data with Databricks Spark
* [👨‍🏫 Using Data in Databricks Spark Slides](https://docs.google.com/presentation/d/1KQvpJjaRGvYkYLXduMm6SvxA_fNeI9V8VYrvGosJlGs/edit?usp=sharing)
* [Creating Github Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
* [Databricks datasets](https://docs.microsoft.com/en-us/azure/databricks/data/databricks-datasets)
* [Example databricks notebooks](https://github.com/FourthBrain/databricks-zero-to-mlops/tree/main/src/week1-getting-started)

## Workshop B: Foundational Pyspark Skills for MLOps

### Section 1: Learning Pyspark and Pandas APIs
* [👨‍🏫 Learning PySpark Slides](https://docs.google.com/presentation/d/1Irs50hbKpBcoF9CW0sPa-w8LooMYKydS6Vt7V0auQ0I/edit?usp=sharing)
* [Example databricks notebooks](https://github.com/FourthBrain/databricks-zero-to-mlops/tree/main/src/week1-getting-started)
* [pandas api](https://docs.databricks.com/languages/python.html#pandas-api-on-spark)
* [Azure Open Datasets Spark](https://github.com/Azure/OpenDatasetsNotebooks/blob/master/tutorials/data-access/01-weather-to-spark-dataframe.ipynb)
* [Using third party editors](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect#visual-studio-code)

### Section 2: Developing with Databricks Workspaces and Repositories for Pyspark
* [👨‍🏫 Developing With Workspaces PySpark Slides](https://docs.google.com/presentation/d/1hMQUwImigJljw4eXhhE0piIfBTctDk6llGIq1a8agag/edit?usp=sharing)

### Section 3:  What is MLOps and Getting Started with Continuous Integration for MLOps
* [👨‍🏫 Getting Started with Continuous Integration for MLOps Slides](https://docs.google.com/presentation/d/1yxQDmEODxkf1M29G_Gfjg9KJMGuLJuXYL-pXahVZ8dg/edit?usp=sharing)

## Appendix

##### Create tables directly from imported data
* [Introduction to importing, reading, and modifying data](https://docs.microsoft.com/en-us/azure/databricks/data/data)
* [Databases and tables](https://docs.microsoft.com/en-us/azure/databricks/data/tables)
* [Metastores](https://docs.microsoft.com/en-us/azure/databricks/data/metastores/)

##### Ingest data into Azure Databricks
* [Databricks integrations](https://docs.microsoft.com/en-us/azure/databricks/integrations/)

##### Access data in Apache Spark formats and from external data sources
* [Data sources](https://docs.microsoft.com/en-us/azure/databricks/data/data-sources/)
* [Delta Lake guide](https://docs.microsoft.com/en-us/azure/databricks/delta/)

#### Labs
* [Github Actions pytest](https://github.com/noahgift/github-actions-pytest)
* [quickstart-create-databricks-workspace-portal](https://docs.microsoft.com/azure/azure-databricks/quickstart-create-databricks-workspace-portal)

#### Discussions
* Why is CI (Continuous Integration) a foundational component for MLOps?
* Why is logging, monitoring, and instrumentation so critical with distributed systems like Spark?
* What is the advantage of scheduling a notebook job in Databricks Spark?
* What are two ways to use data in Databricks Spark?

#### Assignments (Demo)
* Build out your own Github repository with a Python scaffold of:  `Makefile`, `requirements.txt`, a source file, and a test file and do:  `make lint && make test && make format`.
* Add a Jupyter Notebook to your Continuous Integration setup and test it with `pytest --nbval`. [nbval plugin reference](https://github.com/computationalmodelling/nbval). 
* Perform Exploratory Data Analysis with a Databricks Spark Cluster using the [Azure Open Datasets](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-catalog). imported data or Databricks sample datasets. Please try both regular Pyspark as well as the new Pandas API.
* Schedule a notebook job to run nightly at midnight
* Create source code repository, integrate it with Databricks, and build out a notebook in it that you can commit changes to.
* (Optional-Advanced):  Ingest your own dataset to DBFS, then do EDA
