import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://shadowfox.in/"

try:
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")

        headings = []

        for heading in soup.find_all(["h1", "h2", "h3"]):

            text = heading.get_text(strip=True)

            if text:
                headings.append(text)

        data = pd.DataFrame({
            "Headings": headings
        })

        data.to_csv("scraped_data.csv", index=False)

        print("Data Scraped Successfully!")

        print(data)

    else:
        print("Website not opened")

except Exception as e:
    print("Error:", e)