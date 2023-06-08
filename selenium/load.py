import sys,time,random
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# parameters
HOST=sys.argv[1]
ROUND=sys.argv[2]

# Ref:
# - https://lite.ip2location.com/ip-address-ranges-by-country?lang=en_US
# - https://www.maxmind.com/en/geoip-demo
# US: 6.35.44.34
# CN: 101.102.100.66
# JP: 1.5.31.20
# IN: 1.38.2.12
# AU: 103.179.202.88
# BR: 101.33.22.66
# RU: 104.110.184.10
# CA: 103.140.120.68
ip_from_countries = ["6.35.44.34", "101.102.100.66", "1.5.31.20", "1.38.2.12", "103.179.202.88", "101.33.22.66", "104.110.184.10", "103.140.120.68"]
i = random.choice([0, 1, 2, 3, 4, 5, 6, 7])

def request_interceptor(request):
    request.headers['X-Forwarded-For'] = ip_from_countries[i]

def try_and_click(driver, by_type, by_path):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, by_path))).click()
    except Exception as error:
        # handle the exception
        print("there was a retry for: " + by_path + " due to: " + type(error).__name__)
        time.sleep(0.2)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, by_path))).click()

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=chrome_options)
driver.request_interceptor = request_interceptor

print("--> HOST: " + HOST)
print("--> START: " + ROUND)
print("--> X-Forwarded-For:" + ip_from_countries[i])

try:
    driver.get(HOST)

    driver.refresh()

    try_and_click(driver, By.XPATH, "//a[contains(text(),\'Login / Register\')]")
    try_and_click(driver, By.XPATH, "(//input[@type=\'text\'])[2]")
    driver.find_element(By.XPATH,   "(//input[@type=\'text\'])[2]").send_keys("stan")
    try_and_click(driver, By.XPATH, "//input[@type=\'password\']")
    driver.find_element(By.XPATH,   "//input[@type=\'password\']").send_keys("bigbrain")
    try_and_click(driver, By.XPATH, "//button[contains(.,\'Login\')]")

    try_and_click(driver, By.XPATH, "//span[contains(.,\'Artificial Intelligence\')]")
    try_and_click(driver, By.XPATH, "//a[contains(text(),\'Ewooid\')]")
    try_and_click(driver, By.ID,    "vote-4")
    try_and_click(driver, By.XPATH, "//a[contains(text(),\'Watson\')]")
    try_and_click(driver, By.XPATH, "//button[contains(.,\'Add to cart\')]")
    try_and_click(driver, By.XPATH, "//a[contains(@href, \'cart\')]")
    try_and_click(driver, By.XPATH, "//button[contains(.,\'Checkout\')]")

finally:
    driver.quit()


print("--> END: " + ROUND)
