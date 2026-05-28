from playwright.sync_api import sync_playwright

with sync_playwright() as iqra:
    browser = iqra.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/login" , timeout = 60000)
    
    login_link = page.get_by_role("link", name="Login")
    page.wait_for_timeout(5000)
    browser.close()
    print (page.title())
    print (page.url)
    page.screenshot(path="login.png")
    browser.close()