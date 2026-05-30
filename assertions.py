from playwright.sync_api import sync_playwright, expect

with sync_playwright() as iqra:
    browser = iqra.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com", timeout = 60000)
    #Assertion 1 "Check page title"
    expect(page).to_have_title("Automation Exercise")
    #Assertion 2 "Check page URL"
    expect(page).to_have_url("https://www.automationexercise.com/")
    #Assertion 3 "Check element, button, image to be visible"
    expect(page.get_by_role("link", name ="Home")).to_be_visible()
    #Assertion 4 : to_have_text
    page.goto("https://www.automationexercise.com/login", timeout = 60000)
    expect(page.get_by_role("link", name ="Signup / Login")).to_have_text("Signup / Login")
    #Assertion 5 : to be enabled
    # Assertion 5: Login form ka Email field enabled hai verify karna
    expect(page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")).to_be_enabled()
    browser.close()