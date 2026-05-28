from playwright.sync_api import sync_playwright, expect

with sync_playwright() as iqra:
    browser = iqra.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/" , timeout = 80000)
    
    login_link = page.get_by_role("link", name="Signup / Login").click()
    login_heading = page.get_by_text("Login to your account")
    expect(login_heading).to_be_visible()
    email_input = page.locator('[data-qa="login-email"]')
    email_input.fill("test@gmail.com")
    password_input = page.locator('[data-qa="login-password"]')
    password_input.fill("test@123")
    login_button = page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(5000)
    browser.close()
   
