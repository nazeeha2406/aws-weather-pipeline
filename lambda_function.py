import json
import boto3
import os
import urllib.request
from datetime import datetime

def lambda_handler(event, context):
    API_KEY = os.environ["API_KEY"]
    BUCKET_NAME = os.environ["BUCKET_NAME"]
    CITIES = ["Chennai", "Mumbai", "Delhi"]

    s3 = boto3.client("s3")

    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        with urllib.request.urlopen(url) as response:
            raw = json.loads(response.read().decode())

        data = {
            "city": raw["name"],
            "temperature": raw["main"]["temp"],
            "feels_like": raw["main"]["feels_like"],
            "humidity": raw["main"]["humidity"],
            "wind_speed": raw["wind"]["speed"],
            "description": raw["weather"][0]["description"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        filename = f"raw-data/{city.lower()}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=json.dumps(data)
        )
        print(f"✅ {city}: {data['temperature']}°C saved to S3")

    return {
        "statusCode": 200,
        "body": "Weather data collected successfully"
    }