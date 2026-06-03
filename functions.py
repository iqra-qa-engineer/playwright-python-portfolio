#from playwright.sync_api import sync_playwright
#def login(page, email, password):
    #page.goto("https://automationexercise.com/")
    #page.get_by_role("link", name = "Signup / Login").click()
    #Login email field
    #page.locator('[data-qa="login-email"]').fill(email)
    #Login password field
    #page.locator('[data-qa="login-password"]').fill(password)
    #Login button
    #page.locator('[data-qa="login-button"]').click()

#with sync_playwright() as p:
    #browser = p.chromium.launch(headless=False)
    #page = browser.new_page()
    #login(page, "iqrasqa@gmail.com", "123456")
    #browser.close()

# Function for navigate to products page 
#from playwright.sync_api import sync_playwright
#def navigate_to_products_page(page):
    #page.goto("https://automationexercise.com/products")

#with sync_playwright() as p:
    #browser = p.chromium.launch(headless=False)
    #page = browser.new_page()
    #navigate_to_products_page(page)
    #browser.close()


#Function for login and then navigate to prducts page:
#from playwright.sync_api import sync_playwright
#def login_search_and_add_to_cart( page, search, email, password):
    #page.goto("https://automationexercise.com/")
    #page.get_by_role("link", name = "Signup / Login").click()
    #page.locator('[data-qa="login-email"]').fill(email)
    #page.locator('[data-qa="login-password"]').fill(password)
    #page.locator('[data-qa="login-button"]').click()
    #page.wait_for_load_state("load")
    #page.goto("https://automationexercise.com/products")
    #page.get_by_placeholder("Search Product").fill(search)
    #page.locator("#submit_search").click()
    #page.locator(".add-to-cart").first.click()
    #page.wait_for_timeout(3000)

#with sync_playwright() as p:
    #browser = p.chromium.launch(headless=False)
    #page = browser.new_page()
    #login_search_and_add_to_cart(page, "Women",  "iqrasqa@gmail.com", "123456")
    #browser.close()


#Function for function with return value:
#from playwright.sync_api import sync_playwright
#def website_url():
    #url = "https://automationexercise.com/"
    #return url
#with sync_playwright() as p:
    #browser = p.chromium.launch(headless=False)
    #page = browser.new_page()
    #result = website_url()
    #print (result)
    #browser.close()

#function with parameters

#from playwright.sync_api import sync_playwright
#def page_title(title):
    #return title
#with sync_playwright() as p:
    #browser = p.chromium.launch(headless=False)
    #page = browser.new_page()
    #page.goto("https://automationexercise.com/")
    #title = page.title()
    #result = page_title(title)
    ##print (result)
    #browser.close()

from playwright.sync_api import sync_playwright

# Function 1 — site kholo
def open_site(page):
    page.goto("https://automationexercise.com/")

# Function 2 — login page pe jao
# pehle open_site call kiya — phir login link click kiya
def go_to_login(page):
    open_site(page)          # Function 1 andar call hua — site khuli
    page.get_by_role("link", name="Signup / Login").click()

# with block — sirf ek call
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    go_to_login(page)        # sirf yeh ek call — andar sab hua
    browser.close()