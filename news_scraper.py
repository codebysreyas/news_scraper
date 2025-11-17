import requests
from bs4 import BeautifulSoup

# URL of a news website (you can change)
url = "https://www.bbc.com/news"

# Send GET request
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Check if request succeeded
if response.status_code != 200:
    print("Failed to fetch page")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all headlines (BBC uses <h2> and <h3>)
headlines = []

for h in soup.find_all(['h2', 'h3']):
    text = h.get_text(strip=True)
    if len(text) > 10:  # avoid small irrelevant text
        headlines.append(text)

# Save to file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for line in headlines:
        file.write(line + "\n")

print("Scraping completed! Saved to headlines.txt")
