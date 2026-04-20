import requests
from bs4 import BeautifulSoup
import csv

# The URL - a safe site for practicing scraping
url = "https://www.scrapethissite.com/pages/simple/"

print("--- STEP 1: Connecting to the website ---")
try:
    # 1. Get the website content
    # We add a 'timeout' so it doesn't hang forever
    response = requests.get(url, timeout=10)
    
    # Check if the website allowed us in (Status 200 is good)
    if response.status_code == 200:
        print("Connection Successful!")
        
        # 2. Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 3. Find country names
        countries = soup.find_all('h3', class_='country-name')
        
        print(f"Found {len(countries)} countries.")

        # 4. Save to a CSV (Excel) file
        with open('my_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Index", "Country Name"]) # Header
            
            for i, country in enumerate(countries, 1):
                name = country.text.strip()
                writer.writerow([i, name])
                if i <= 5: # Just show first 5 in terminal to keep it clean
                    print(f"Adding to file: {name}")

        print("\n--- DONE! ---")
        print("Look for a new file named 'my_data.csv' in your sidebar.")

    else:
        print(f"Website returned an error code: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")
    print("Make sure you are connected to the WiFi!")