import base64

def generate_tracking_link(email, base_url):
    encoded_email = base64.urlsafe_b64encode(email.encode()).decode()
    return f"{base_url}/r/{encoded_email}"

# Example usage
email = "employee33@gmail.com"
base_url = " https://7133-103-48-197-9.ngrok-free.app"  # Replace with your ngrok URL
tracking_link = generate_tracking_link(email, base_url)
print(tracking_link)
