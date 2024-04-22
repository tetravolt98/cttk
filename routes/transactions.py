import requests
from flask import Blueprint, jsonify, request

from db import get_db

transactions_bp = Blueprint('transactions', __name__)

URI = "https://blockchain.info/"


@transactions_bp.route('/<address_id>', methods=['GET'])
def get_transactions(address_id):
    """
    Get list of transactions for a given address
    """

    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * 50
    limit = 50

    try:
        response = requests.get(f"https://blockchain.info/rawaddr/{address_id}?offset={offset}&limit={limit}")
    except Exception as e:
        print(e)  # local debug
        return jsonify({'error': "Could not get transactions at this time"}), 500

    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': "Could not get transactions at this time"}), 500

    return jsonify({'transactions': data['txs']})


@transactions_bp.route('/<address_id>/balance', methods=['GET'])
def get_balance(address_id):
    """
    Get current balance for a given address in BTC
    """
    try:
        response = requests.get(f"{URI}/balance?active={address_id}")
    except Exception as e:
        print(e)  # local debug
        return jsonify({'error': "Could not get balance at this time"}), 500

    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': "Invalid address"}), 500

    db = get_db()
    cur = db.execute("""SELECT * FROM balances WHERE address_id = ?""", (address_id,))
    existing_balance = cur.fetchone()

    balance = data[address_id]['final_balance']

    if existing_balance:
        db.execute("""UPDATE balances SET balance = ? WHERE address_id = ?""", (balance, address_id))
    else:
        db.execute("""INSERT INTO balances (address_id, balance) VALUES (?, ?)""", (address_id, balance))

    db.commit()

    return jsonify({"balance": balance / 1e8})


@transactions_bp.route('/sync', methods=['POST'])
def sync_transactions():
    """
    Synchronize the transaction history for all addresses
    """
    return "sync_transactions"
