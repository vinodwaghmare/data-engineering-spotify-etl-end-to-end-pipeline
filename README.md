# Data Engineering Complete Spotify ETL Pipeline 

# Description
--
In this Project, we are going to use Spotify API dataset to perform analysis & getting insights, here we will build ETL (extract, Transform, Load ) pipeline to fetch raw data from the source ( Spofity API) & transform it in the meaningful dataset.

Steps For Complete ETL Pipeline 
--
Spotify API dataset extraction using AWS lambda function.

Adding trigger on extract load function by scheduling it.

Deploying Transformation function code in AWS lambda function.

Again adding trigger on transformation function based on events in S3 directory. 

Building Analytics Tables on data files in AWS S3 using Glue and Athena.

Technologies used :
--
*AWS S3 : Store API fetch data, transformed data.

AWS Lambda : To execute extract load & transform function.

AWS Glue Crawler : To create metadata table pointed towards S3.

AWS Athena : For query execution on the top of data catalog tables to perform analysis.
 
