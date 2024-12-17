# from django.contrib import admin

# # Register your models here.

from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = ""
africastalking.initialize(username, api_key)
sms = africastalking.SMS


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get('sessionId', None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    # ussd logic
    if text == "":
        # main menu
        response = "CON Welcome to Mboka services \n"
        response += "1. Enter username\n"
        response += "2. Enter phone number\n"
    elif text == "1":
        # sub menu 1
        response = "CON What would you like to check on your account?\n"
        response += "1. username \n"
        response += "2. phone number"
    elif text == "1":
        # sub menu 1
        response = "END Your username is {}".format(username)
    elif text == "2":
        response = "END Your phone number is {}".format(phone_number)
    # elif text == "1*1":
    #     # ussd menus are split using *
    #     account_number = "1243324376742"
    #     response = "END Your account number is {}".format(account_number)
    # elif text == "1*2":
    #     account_balance = "100,000"
    #     response = "END Your account balance is USD {}".format(account_balance)
    else:
        response = "END Invalid input. Try again."
    return response


if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))