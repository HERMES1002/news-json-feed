import json
from datetime import datetime, timedelta

# Simulated news events (replace with real API or RSS later)
news = [
    {
        "currency": "USD",
        "description": "CPI Report",
        "datetime": (datetime.utcnow() + timedelta(hours=2)).strftime("%Y.%m.%d %H:%M")
    },
    {
        "currency": "EUR",
        "description": "ECB Rate Decision",
        "datetime": (datetime.utcnow() + timedelta(hours=5)).strftime("%Y.%m.%d %H:%M")
    }
]

# Save to JSON file
with open("news_events.json", "w") as f:
    json.dump(news, f, indent=2)

print("✅ news_events.json updated")
