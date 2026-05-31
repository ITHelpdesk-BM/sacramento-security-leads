import pandas as pd
import requests
from bs4 import BeautifulSoup

def run_scrape():
    # Replace with real Sacramento Planning URL logic
    data = {"Project": ["Example"], "Status": ["Pending"]}
    df = pd.DataFrame(data)
    # Save to a file that app.py will read
    df.to_csv("results.csv", index=False)

if __name__ == "__main__":
    run_scrape()
