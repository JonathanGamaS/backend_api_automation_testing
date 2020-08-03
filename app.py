

from woocommerce import API
import json
import os


wcapi = API(
    url="http://ecommerce.local",
    consumer_key= os.getenv("consumer_key"),
    consumer_secret= os.getenv("consumer_secret"),
    version="wc/v3"
)

response = wcapi.get("products").json()

print(response)