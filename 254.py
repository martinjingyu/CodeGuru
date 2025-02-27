import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context
import urllib3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sslv3_enabled_http_adapter():
    """Create an HTTPAdapter that forces SSLv3."""
    # Create an SSL context
    ssl_context = create_urllib3_context()
    ssl_context.set_ciphers('SSLv3')  # Force SSLv3 cipher

    class SSLSv3Adapter(HTTPAdapter):
        def init_poolmanager(self, *args, **kwargs):
            kwargs['ssl_context'] = ssl_context
            return super(SSLSv3Adapter, self).init_poolmanager(*args, **kwargs)

    return SSLSv3Adapter()

def test_sslv3_connection(url):
    """Test SSL connection using SSLv3."""
    try:
        # Create a session and mount the SSLv3 adapter
        session = requests.Session()
        session.mount('https://', sslv3_enabled_http_adapter())

        # Attempt to connect
        response = session.get(url)
        logger.info(f"Connection successful with status code: {response.status_code}")
        return response.status_code == 200

    except requests.exceptions.SSLError as ssl_err:
        logger.error(f"SSL error encountered: {ssl_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error encountered: {req_err}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

    return False

# Example usage
url = "https://example.com"
if test_sslv3_connection(url):
    print("SSLv3 connection successful.")
else:
    print("SSLv3 connection failed.")