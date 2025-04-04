import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

URL = "https://www.forexfactory.com/calendar"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Get current day
now = datetime.utcnow()
today = now.strftime("%a %b %d, %Y")

# Fetch the page
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')

# Prepare output
news_data = []

# Parse rows
for row in soup.select("tr.calendar__row"):
    impact = row.select_one(".impact span")
    time_el = row.select_one(".time")
    currency_el = row.select_one(".currency")
    event_el = row.select_one(".event")

    if not all([impact, time_el, currency_el, event_el]):
        continue

    if "High" not in impact.get("title"):
        continue  # only high-impact events

    time_str = time_el.text.strip()
    if time_str.lower() == "all day" or not time_str:
        continue

    try:
        event_time = datetime.strptime(f"{today} {time_str}", "%a %b %d, %Y %I:%M%p")
    except:
        try:
            event_time = datetime.strptime(f"{today} {time_str}", "%a %b %d, %Y %H:%M")
        except:
            continue

    # Convert to MT5 format
    formatted_time = event_time.strftime("%Y.%m.%d %H:%M")

    news_data.append({
        "currency": currency_el.text.strip(),
        "description": event_el.text.strip(),
        "datetime": formatted_time
    })

# Save
with open("news_events.json", "w") as f:
    json.dump(news_data, f, indent=2)

print("✅ Real ForexFactory news saved to news_events.json")
