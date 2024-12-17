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
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    # Handle the USSD flow based on user input
    if text == "":
        # Step 2: Initial Menu
        response = "CON Welcome to Mboka Services\n"
        response += "1. Enter username\n"
        response += "2. Enter phone number\n"
    elif text == "1":
        # Prompt for username
        response = "CON Enter username:\n"
    elif text == "1*1":
        response = f"END Your username is {username}.\nProcessing your request..."
    elif text  == "1*2":
        response = f"Your phone number is {phone_number}\nProcessing your request..."
    # elif text == "2":
    #     # sub menu 1
    #     response = "CON What would you like to check on your account?\n"
    #     response += "1. Account number \n"
    #     response += "2. Account balance"
    # elif text == "2*1":
    #     account_number = "1243324376742"
    #     response = "END Your account number is {}".format(account_number)
    # elif text == "2*2":
    #     account_balance = "100,000"
    #     response = "END Your account balance is USD {}".format(account_balance)
    else:
        response = "END Invalid input. Please try again."

    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(port=8000, debug=True)
