import requests

TOKEN = "7886188626:AAHIODPwbO8PXBFRr10VIwP2fQUCzsNgv90"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"


#  955629733   my chatId
# Make the GET request and print the JSON response
response = requests.get(url)

try:
    data = response.json()
    print(data)

    # Extract chat ID if available
    if data['result']:
        chat_id = data['result'][0]['message']['chat']['id']
        print(f"Chat ID: {chat_id}")
    else:
        print("No messages found. Send a message to your bot and try again.")
except requests.exceptions.JSONDecodeError:
    print("Error decoding JSON response")
    print(response.text)
