from flask import Flask, request, jsonify
from shopify_api import generate_coupon, get_sale_items, get_wishlist
import os

from flask_cors import CORS # type: ignore
app = Flask(__name__)
CORS(app)

# === Routes ===
# @app.route('/generate-coupon', methods=['POST'])
# def handle_coupon():
#     return generate_coupon()

@app.route('/generate-coupon', methods=['GET', 'POST'])
def generate_coupon():
    if request.method == 'GET':
        return jsonify({"success": True, "code": "LYVNTESTGET"})
    if request.method == 'POST':
        return jsonify({"success": True, "code": "LYVNDEBUG"})
    
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"pong": True})

@app.route('/sale-items', methods=['GET'])
def handle_sale_items():
    return get_sale_items()

@app.route('/wishlist', methods=['POST'])
def handle_wishlist():
    user_id = request.json.get('user_id')
    return get_wishlist(user_id)

if __name__ == '__main__':
    app.run(debug=True)
