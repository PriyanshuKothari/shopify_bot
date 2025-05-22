import os
import requests
import random
import string
from flask import Flask, request, jsonify

# === Shopify Config ===
SHOP = os.getenv('SHOPIFY_STORE')
TOKEN = os.getenv('SHOPIFY_TOKEN')
PRICE_RULE_ID = os.getenv('PRICE_RULE_ID')

# === Helper Functions ===
def generate_code():
    return "LYVN" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# === API Handlers ===
def generate_coupon():
    try:
        discount_code = generate_code()
        url = f"https://{SHOP}/admin/api/2024-04/price_rules/{PRICE_RULE_ID}/discount_codes.json"
        headers = {"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN}
        data = {"discount_code": {"code": discount_code}}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return jsonify({"success": True, "code": discount_code})
        else:
            return jsonify({"error": response.text}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_sale_items():
    try:
        url = f"https://{SHOP}/admin/api/2024-04/products.json?tag=trending"
        headers = {"X-Shopify-Access-Token": TOKEN}
        response = requests.get(url, headers=headers)
        products = response.json().get('products', [])
        return jsonify(products[:5])  # Return top 5 trending items
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_wishlist(user_id):
    # Your wishlist logic here (e.g., fetch from Shopify Metafields)
    return jsonify({"items": []})
