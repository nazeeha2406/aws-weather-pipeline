-- View all weather data
SELECT * FROM raw_data LIMIT 10;

-- Hottest city
SELECT city, MAX(temperature) AS max_temp
FROM raw_data
GROUP BY city;

-- Average humidity per city
SELECT city, ROUND(AVG(humidity), 2) AS avg_humidity
FROM raw_data
GROUP BY city;

-- Chennai data only
SELECT * FROM raw_data
WHERE city = 'Chennai'
ORDER BY timestamp DESC;

-- Count records per city
SELECT city, COUNT(*) AS total_records
FROM raw_data
GROUP BY city;