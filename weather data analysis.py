import csv
import statistics
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]
import os

# Find weather.csv in the same folder as this Python file
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "weather.csv")

# 1. Load CSV file with Python's standard library
with open(file_path, newline="", encoding="utf-8") as csv_file:
	df = list(csv.DictReader(csv_file))

for row in df:
	row["Temperature"] = float(row["Temperature"])
	row["Humidity"] = float(row["Humidity"])

print("Weather Data:")
for row in df:
	print(row)

# 2. Calculate average, maximum, and minimum temperatures
temperatures = [row["Temperature"] for row in df]
average_temp = statistics.mean(temperatures)
maximum_temp = max(temperatures)
minimum_temp = min(temperatures)

print("\n--- Temperature Analysis ---")
print(f"Average Temperature: {average_temp:.2f} °C")
print(f"Maximum Temperature: {maximum_temp} °C")
print(f"Minimum Temperature: {minimum_temp} °C")

# 3. Identify the day with the highest temperature
hottest_day = max(df, key=lambda row: row["Temperature"])

print("\n--- Hottest Day ---")
print("Date:", hottest_day["Date"])
print("Temperature:", hottest_day["Temperature"], "°C")

# 4. Line chart: Daily temperature changes
plt.figure(figsize=(8, 5))
plt.plot([row["Date"] for row in df], temperatures, marker="o")
plt.title("Daily Temperature Changes")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Histogram: Distribution of temperatures
plt.figure(figsize=(8, 5))
plt.hist(temperatures, bins=5, edgecolor="black")
plt.title("Distribution of Temperatures")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 6. Scatter plot: Humidity vs temperature
plt.figure(figsize=(8, 5))
plt.scatter([row["Humidity"] for row in df], temperatures)
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity (%)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()