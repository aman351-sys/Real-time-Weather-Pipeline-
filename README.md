# Real-time-Weather-Pipeline-

## Project Overview 
●	Engineered an ETL  Pipeline ingesting data from API and exporting  analysis  ready table to PostgreSQL ,cutting
Manual data prep. From Hours to minutes          

A  real-time weather data pipeline that fetches live weather information through APIs and stores it in PostgreSQL for analysis and historical tracking.

## About me 
Hi ! I am  Aman Maniyar , a Data Analyst I created this project to demonstrate my skills in Python,SQL. 

## Table of Contents - For easy navigation
** Features**  - 
Automated Pipeline extract live weather,
multi-location support - fetch weather for multiple cities 
PostgreSQL -storage of  weather data  for historical analysis.

Tech Stack - Technologies used (APIs, database, frameworks)
Architecture - System design/data flow diagram
Database Schema - Tables and structure
API Integration - Openmeteo.com

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7+
- PostgreSQL 12+
- pip (Python package manager)
- Git

## Architecture

```
┌─────────────────────────────────────────────────┐
│         Weather API (https://api.open-meteo.com)            │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│        Data Fetcher Module                      │
│  - API requests                                 │
│  - Error handling & retries                     │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│        Data Transformer Module                  │
│  - Data cleaning & validation                   │
│  - Format conversion                            │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│     Database Storage (PostgreSQL)               │
│  - weather_data table                           │
│  - Historical tracking                          │
└─────────────────────────────────────────────────┘
```
**Last Updated**: August 2026

## file included 
pipeline.py : Python script to extract data 
SQL OPERATION.sql  : run  sql query . 
