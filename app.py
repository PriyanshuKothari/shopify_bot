from flask import Flask, request, jsonify
from shopify_api import generate_coupon, get_sale_items, get_wishlist
import os

app = Flask(__name__)

# === Routes ===
@app.route('/generate-coupon', methods=['POST'])
def handle_coupon():
    return generate_coupon()

@app.route('/sale-items', methods=['GET'])
def handle_sale_items():
    return get_sale_items()

@app.route('/wishlist', methods=['POST'])
def handle_wishlist():
    user_id = request.json.get('user_id')
    return get_wishlist(user_id)

if __name__ == '__main__':
    app.run(debug=True)
