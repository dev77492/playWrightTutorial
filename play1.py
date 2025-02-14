import re
from playwright.sync_api import Playwright, sync_playwright, expect
from random import randint

userName = "Harsh" + str(randint(1,10000))
passWord = "Harshpass" + str(randint(1,10000))



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.demoblaze.com/index.html")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(userName)
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill(passWord)
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Sign up").click()
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").click()
    page.locator("#loginusername").fill(userName)
    page.locator("#loginpassword").click()
    page.locator("#loginpassword").fill(passWord)
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("link", name="Iphone 6 32gb").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.get_by_role("button", name="Place Order").click()
    page.get_by_role("textbox", name="Total: 790 Name:").fill(userName)
    page.get_by_text("Total: 790 Name: Country:").click()
    page.get_by_role("textbox", name="Country:").click()
    page.get_by_role("textbox", name="Country:").fill("India")
    page.get_by_role("textbox", name="City:").click()
    page.get_by_role("textbox", name="City:").fill("Pune")
    page.get_by_role("textbox", name="Credit card:").click()
    page.get_by_role("textbox", name="Credit card:").fill("123")
    page.get_by_role("textbox", name="Month:").click()
    page.get_by_role("textbox", name="Month:").fill("12")
    page.get_by_role("textbox", name="Year:").click()
    page.get_by_role("textbox", name="Year:").fill("32")
    page.get_by_role("button", name="Purchase").click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("link", name="Log out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
