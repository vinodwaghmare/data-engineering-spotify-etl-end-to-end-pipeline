# data-engineering-spotify-etl-end-to-end-pipeline

Description
--
In this Project, we are going to use Spotify API dataset to perform analysis & getting insights, here we will build ETL (extract, Transform, Load ) pipeline to fetch raw data from the source ( Spofity API) & transform it in the meaningful dataset.

Technologies used :
--
AWS S3 : Store API fetch data, transformed data.
AWS Lambda : To execute extract load & transform function.
AWS Glue Crawler : To create metadata table pointed towards S3.
AWS Athena : For query execution on the top of data catalog tables to perform analysis.
