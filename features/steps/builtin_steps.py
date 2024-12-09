from behave_webdriver.steps import *  # ignore
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



@given('I open the url "{url}"')
def open_url(context, url):
    context.behave_driver.get(url)



######ENCODE MESSAGE/DECODE MESSAGE TOGETHER#########


@when('I click on the "{encode_option}" option in the settings')
def click_encode_or_decode(context, encode_option):
    settings_dropdown = Select(context.behave_driver.find_element(By.ID, "decoder-setting"))
    settings_dropdown.select_by_visible_text(encode_option)


@when('I input the "{message}" into the text box labeled "Type message here"')
def input_message_into_textbox(context, message):
    text_box = context.behave_driver.find_element(By.ID, "letters")
    text_box.send_keys(message)


@when('I select the correct shift or key for the encoded message')
def select_shift(context):
    ceaser_shift_dropdown = Select(context.behave_driver.find_element(By.ID, "shift-amount"))
    ceaser_shift_dropdown.select_by_value("5") 


@then('I click the "translate_message" button')
def click_translate_message_button(context):
    translate_button = context.behave_driver.find_element(By.ID, "submit")
    translate_button.click()

@then('I should see the encoded message displayed on the screen')
def verify_encoded_message(context):
    result_element = context.behave_driver.find_element(By.ID, "decoded_message")
    encoded_message = result_element.text

    
@then('I should see the decoded message displayed on the screen')
def verify_decoded_message(context):
    result_element = context.behave_driver.find_element(By.ID, "decoded_message")
    decoded_message = result_element.text

   

   



