from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

# --- Configuration ---
link = "https://uvoonaix.top/4/9250181"  # Replace with your ad link
min_wait = 5  # seconds
max_wait = 10
total_loops = 10

# --- Setup Chrome Options ---
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# --- Loop for Multiple Visits ---
for i in range(total_loops):
    print(f"[{i+1}/{total_loops}] Visiting: {link}")
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    
    # Wait for ad to load and simulate stay
    delay = random.randint(min_wait, max_wait)
    print(f"Waiting {delay} seconds...")
    time.sleep(delay)
    
    driver.quit()
    print("Closed browser\n")
    time.sleep(2)
