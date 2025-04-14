import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Active OpenWeatherMap API key
API_KEY = "8464ba428d765f51bfca7457459bc158"
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(URL)
data = response.json()

# Extracting date and temperature
dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])

# Visualization
plt.figure(figsize=(14, 6))
sns.lineplot(x=dates, y=temps, marker="o", color="skyblue")
plt.xticks(rotation=45)
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.grid(True)
plt.show()