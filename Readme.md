# AWS Weather Data Pipeline

## What This Project Does
Fetches live weather data for Chennai, Mumbai, Delhi 
every hour automatically and stores it in AWS S3.

## Architecture
OpenWeather API → Python → AWS Lambda → S3 → Glue → Athena → QuickSight

## AWS Services Used
- Lambda (auto runs every hour)
- S3 (stores weather JSON files)
- Glue Crawler (detects data structure)
- Athena (SQL queries on S3)
- EventBridge (hourly schedule trigger)

## Progress
- Day 1: Fetch weather + save to S3
- Day 2: Multiple cities added
- Day 3: Lambda + EventBridge automation
- Day 4: Glue Crawler + Data Catalog setup