import sys,time,random
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# parameters
HOST=sys.argv[1]
ROUND=sys.argv[2]

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.geolocation": 1})

driver = webdriver.Chrome(options=chrome_options)

# Honolulu: 21.3281792,-157.8691131
# Mauritius: -21.0752381,57.0387649
# South Africa: -33.914651,18.3758793
# China: 30.2325248,120.1400391
latitude = [21.3281792,-21.0752381,-33.914651,30.2325248]
longitude = [-157.8691131,57.0387649,18.3758793,120.1400391]
i = random.choice([0, 1, 2, 3])
driver.execute_cdp_cmd(
    "Emulation.setGeolocationOverride",
    {
        "latitude": latitude[i],
        "longitude": longitude[i],
        "accuracy": 100,
    },
)

def try_and_click(driver, by_type, by_path):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, by_path))).click()
    except:
        print("there was a retry for: " + by_path)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, by_path))).click()

print("-->START:" + ROUND)

driver.get(HOST)

driver.refresh()

try_and_click(driver, By.LINK_TEXT, "Login / Register")
try_and_click(driver, By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div[2]/table[1]/tbody/tr[1]/td[2]/input")
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div[2]/table[1]/tbody/tr[1]/td[2]/input").send_keys("stan")
driver.find_element(By.XPATH, "//input[@type=\'password\']").click()
driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("bigbrain")
driver.find_element(By.XPATH, "//button[contains(.,\'Login\')]").click()
try_and_click(driver, By.XPATH, "//span[contains(.,\'Artificial Intelligence\')]")
try_and_click(driver, By.XPATH, "//a[contains(text(),\'Ewooid\')]")
try_and_click(driver, By.ID, "vote-4")
try_and_click(driver, By.LINK_TEXT, "Stan")
try_and_click(driver, By.CSS_SELECTOR, ".ng-scope > button")
try_and_click(driver, By.LINK_TEXT, "Watson")
try_and_click(driver, By.XPATH, "//button[contains(.,\'Add to cart\')]")
try_and_click(driver, By.XPATH, "//span[contains(.,\'Robot\')]")
try_and_click(driver, By.LINK_TEXT, "Cybernated Neutralization Android")
try_and_click(driver, By.ID, "vote-5")
try_and_click(driver, By.LINK_TEXT, "Cart")
try_and_click(driver, By.XPATH, "//button[contains(.,\'Checkout\')]")

driver.quit()

print("-->END:" + ROUND)
