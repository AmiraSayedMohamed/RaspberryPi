import requests

# Your bot token
TOKEN = "7886188626:AAHIODPwbO8PXBFRr10VIwP2fQUCzsNgv90"
PHOTO_PATH = "your_image.jpg"  # 🔁 Replace with your actual image path

# List of chat IDs to send the image to
chat_ids = [955629733, 11111111]

# Function to send photo
def send_photo(chat_id, photo_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        response = requests.post(
            url,
            data={'chat_id': chat_id},
            files={'photo': photo}
        )
        print(f"Sent to {chat_id}:")
        print(response.json())

# Send the photo to each chat ID
for chat_id in chat_ids:
    send_photo(chat_id, PHOTO_PATH)
