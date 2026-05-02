from dotenv import load_dotenv
import os
import requests
import json
import boto3
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
CITY = "Chennai"

# Step 1 - Fetch weather
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
raw = response.json()

# Step 2 - Extract only useful fields
data = {
    "city": raw["name"],
    "temperature": raw["main"]["temp"],
    "feels_like": raw["main"]["feels_like"],
    "humidity": raw["main"]["humidity"],
    "wind_speed": raw["wind"]["speed"],
    "description": raw["weather"][0]["description"],
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

print(json.dumps(data, indent=2))

# Step 3 - Save to S3
s3 = boto3.client("s3")
filename = f"raw-data/chennai_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

s3.put_object(
    Bucket=BUCKET_NAME,
    Key=filename,
    Body=json.dumps(data)
)

print(f"✅ Saved to S3: {filename}")