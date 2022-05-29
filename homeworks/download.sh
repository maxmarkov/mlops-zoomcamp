#!/bin/bash

## === Download data === 
mkdir data

## Green Taxi Trip Records
wget https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2021-01.parquet -P data
wget https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2021-02.parquet -P data
wget https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2021-03.parquet -P data

## For-Hire Vehicle Trip Records
wget https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2021-01.parquet -P data 
wget https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2021-02.parquet -P data
wget https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2021-03.parquet -P data

mv data homeworks/ 
