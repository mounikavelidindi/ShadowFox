import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_shadowfox():
    url = "https://shadowfox.in/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        headings_data = []
        
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            text = heading.get_text(strip=True)
            if text:
                headings_data.append({
                    "Tag": heading.name.upper(),
                    "Content": text
                })
        
        if headings_data:
            df = pd.DataFrame(headings_data)
            
            # 1. CSV save chey - Task kosam
            df.to_csv("scraped_data.csv", index=False, encoding="utf-8")
            
            # 2. Console lo neat table la print chey
            print("\n" + "="*70)
            print("SHADOWFOX.IN - SCRAPED HEADINGS")
            print("="*70)
            print(df.to_string(index=False)) # Index theeyadam tho clean ga untadi
            print("="*70)
            print(f"\nData Scraped Successfully! Total {len(df)} headings saved to scraped_data.csv")
            
        else:
            print("No headings found.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_shadowfox()