from playwright.sync_api import sync_playwright, expect

with sync_playwright() as iqra:
    browser = iqra.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/" , timeout = 80000)
    
    page.get_by_role("link",name="Signup / Login").click()
    signup_heading = page.get_by_text("New User Signup!")
    expect(signup_heading).to_be_visible()
    name_input = page.locator('[data-qa="signup-name"]')
    name_input.fill("test")
    email_input = page.locator('[data-qa="signup-email"]')
    email_input.fill("testuser_iqra123@gmail.com")
    page.get_by_role("button",name="Signup").click()

    # Step 1: Verify "Enter Account Information" page is opened successfully
    account_info_heading = page.get_by_text("Enter Account Information")
    expect(account_info_heading).to_be_visible()

    # Step 2: Verify "Title" section is visible (parent section check)
    title_section = page.get_by_text("Title" , exact=True)
    expect(title_section).to_be_visible()
    page.get_by_role("radio" , name ="Mrs.").check()
    password_input = page.locator('[data-qa="password"]')
    password_input.fill("Test@1234")

    # Step 5: Select date of birth - Day
    day_dropdown = page.locator('[data-qa="days"]')
    day_dropdown.select_option("19")

    #Step 6: Select date of birth - Month
    month_dropdown = page.locator('[data-qa="months"]')
    month_dropdown.select_option("12")

    # Step 7 : Select date of birth - Year
    year_dropdown = page.locator('[data-qa="years"]')
    year_dropdown.select_option("1999")

    # Step 7: Subscribe to newsletter
    page.get_by_role("checkbox" , name="Sign up for our newsletter!").check()
    page.get_by_role("checkbox" , name="Receive special offers from our partners!").check()

    # Address Information
    address_info_heading = page.get_by_text("Address Information" , exact=True)
    expect(address_info_heading).to_be_visible()
    first_name = page.locator('[data-qa="first_name"]')
    first_name.fill("Test")
    last_name = page.locator('[data-qa="last_name"]')
    last_name.fill("QA")
    company_name = page.locator('[data-qa="company"]')
    company_name.fill("Test Company")

    # Step 13: Enter address
    address = page.locator('[data-qa="address"]')
    address.fill("123 Main Street")

    # Step 14: Enter address line 2
    address2 = page.locator('[data-qa="address2"]')
    address2.fill("Apartment 4B")

    # Step 15: Select country from dropdown
    country_dropdown = page.locator('[data-qa="country"]')
    country_dropdown.select_option("Singapore")

    # Step 16: Enter State
    state = page.locator('[data-qa="state"]')
    state.fill("Test State")

    # Step 17 : Enter City
    city = page.locator('[data-qa="city"]')
    city.fill("Lahore")

    # Step 18: Enter Zipcode
    zipcode = page.locator('[data-qa="zipcode"]')
    zipcode.fill("54000")

    #Step 19 : Enter Mobile Number
    mobile_number = page.locator('[data-qa="mobile_number"]')
    mobile_number.fill("123456789")
    page.get_by_role ("button",name="Create Account").click()

    # Pause for manual inspection (keep browser open)
    input("Press Enter to close browser...")
    browser.close()