import requests
TOKEN = "6436678943:AAHYfEqwJ0MRV6J74TZEjAAqdKNQeO9kurU"
chat_id = "6264510964"
message = "hello from your telegram bot"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json()) # this sends the message

