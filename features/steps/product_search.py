from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from behave import given, when, then
from time import sleep


LOGIN_EMAIL = (By.ID, 'email-2')
LOGIN_PASSWORD = (By.ID, 'field')


@given('Open Reely home page')
def open_reely(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    # context.driver.refresh()

@when('Log into the page')
def click_login(context):
    context.driver.find_element(*LOGIN_EMAIL).click()
    sleep(2)
    context.driver.find_element(*LOGIN_EMAIL).send_keys('dimawarehouse@yahoo.com')
    sleep(2)
    context.driver.find_element(*LOGIN_PASSWORD).send_keys('Mommalove@123')
    element = WebDriverWait(context.driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"a.login-button.w-button"))
    )
    element.click()
    sleep(10)


@when('Click on Connect Agency')
def click_connect_agency(context):
    element1 = context.driver.find_element(By.CSS_SELECTOR,
    "div.get-free-period.menu")
    element1.click()
    sleep(2)


@when('Switch the new tab')
def switch_to_new_tab(context):
    new_tab_handle = context.driver.window_handles[-1]
    sleep(1)


@then('Verify there are 4 steps on the presentation page')
def verify_4_steps(context):
    steps = context.driver.find_element(By.CSS_SELECTOR, '[class="w-layout-grid steps-grid"]')
    text = steps.text
    print(text)
    # visible_elements = 0
    # for step in steps:
    #     if step.is_displayed() and step.is_eneabled():
    #         visible_elements += 1
    # print(f'Number of visible steps found:{visible_elements}')




@then('Verify Subscription Plans button is clickable')
def verify_subscription_plan_clickable(context):
    element2 = context.driver.find_element(By.XPATH, "//a[contains(@href, '/pro')]")

    if element2.is_enabled():
        print("Subscription plans button is clickable.")
    else:
        print("Subscription plans button is not clickable.")