BASE_URL = "https://p-app.onrender.com/track"

def generate_tracking_url(email):
    if not email:
        raise ValueError("Email cannot be empty")
    
    # Append the email as a query parameter
    tracking_url = f"{BASE_URL}?email={email}"
    return tracking_url

if __name__ == "__main__":
    # Example usage
    test_email = "user@example.com"
    tracking_url = generate_tracking_url(test_email)
    print(f"Tracking URL: {tracking_url}")
