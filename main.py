from selenium import webdriver
# from selenium.webdriver.chrome.options import COptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def pagewait(driver):
    # JavaScript to check if the page is idle
    js_script = """
    return (window.document.readyState === "complete" &&
            (typeof window.jQuery === "undefined" || (window.jQuery && window.jQuery.active === 0)) &&
            (typeof window.angular === "undefined" || (window.angular && !window.angular.element(document).injector().get('$http').pendingRequests.length)));
    """

    try:
        # Wait for the custom condition to become true
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script(js_script))

    except TimeoutException:
        print("Timeout waiting for the page to be idle.")


def gridchrome(ver=None):
    url = "http://localhost:4444"
    options = webdriver.ChromeOptions()
    if ver:
        options.binary_location = f"C:/Users/fisch/ucsd/selenium_chrome/Se{ver}/chrome/chrome.exe"
        options.add_argument(f"--browserVersion={ver}")
    options.add_argument("--browserName=chrome")

    options.add_argument("--platform=WINDOWS")
    options.add_argument("--window-size=800,600")
    options.add_argument("--window-position=10,10")
    driver = webdriver.Remote(command_executor=url, options=options)
    driver.set_page_load_timeout(30)
    driver.get("https://map.google.com")
    pagewait(driver)

    # driver.get("https://spotify.com")
    # pagewait(driver)
    driver.get("https://blink.ucsd.edu/")
    pagewait(driver)
    driver.get("https://ucsd.edu")
    pagewait(driver)

    driver.quit()


if __name__ == '__main__':
    gridchrome()
    gridchrome("115")
    gridchrome("116")
    gridchrome("117")
    gridchrome("118")
    gridchrome("119")
    gridchrome("120")
    # gridfox()


def gridfox():
    url = "http://localhost:4444"
    options = webdriver.FirefoxOptions()
    options.add_argument("--browserName=firefox")
    options.add_argument("--platform=WINDOWS")
    options.add_argument("--window-size=800,600")
    options.add_argument("--window-position=10,10")

    driver = webdriver.Remote(command_executor=url, options=options)
    driver.set_page_load_timeout(30)
    driver.get("https://map.google.com")
    pagewait(driver)

    driver.get("https://spotify.com")
    pagewait(driver)
    driver.get("https://blink.ucsd.edu/")
    pagewait(driver)
    driver.get("https://ucsd.edu")
    pagewait(driver)

    driver.quit()

# def segrid1():
#     # Replace with your Hub URL and port
#     hub_url = "http://192.168.56.1:4444"
#     url = "http://localhost:4444"
#     # Set desired Chrome version
#     desired_version = "119"
#     # Set desired capabilities through options
#     # options = webdriver.ChromeOptions()
#     # options.binary_location = "C:/Users/fisch/ucsd/selenium_chrome/se120/chrome-win64/chrome.exe"
#     # chromedriver_bin="C:/Users/fisch/ucsd/selenium_chrome/se120/chromedriver.exe"
#     # service = webdriver.ChromeService(executable_path=chromedriver_bin)
#     options = Options()
#     options.add_argument("--browserName=chrome")
#     options.add_argument("--platform=WINDOWS")
#     options.add_argument("--window-size=800,600")
#     options.add_argument("--window-position=10,10")
#     # Specify desired Chrome version if needed
#     options.add_argument(f"--browserVersion={desired_version}")
#
#     # Allow remote debugging
#     options.add_argument("--remote-debugging-port=9222")
#
#     # Connect to Selenium Grid
#     driver = webdriver.Remote(command_executor=url, options=options)
#     # Navigate to a website
#     driver.set_page_load_timeout(30)
#     driver.get("https://map.google.com")
#     pagewait(driver)
#
#     driver.get("https://spotify.com")
#     pagewait(driver)
#     driver.get("https://blink.ucsd.edu/")
#     pagewait(driver)
#     driver.get("https://ucsd.edu")
#     pagewait(driver)
#     # Quit the browser
#     driver.quit()
#
#
# def driver_location(chromedriver_bin, chrome_bin):
#     options = webdriver.ChromeOptions()
#     options.binary_location = chrome_bin
#
#     service = webdriver.ChromeService(executable_path=chromedriver_bin)
#
#     driver = webdriver.Chrome(service=service, options=options)
#
#     driver.quit()
