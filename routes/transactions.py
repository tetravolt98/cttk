from flask import Blueprint

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/<address>', methods=['GET'])
def get_transactions(address):
    """
    Get list of transactions for a given address
    """
    return "get_transactions"


@transactions_bp.route('/<address>/balance', methods=['GET'])
def get_balance(address):
    """
    Get current balance for a given address
    """
    return "get_balance"


@transactions_bp.route('/sync', methods=['POST'])
def sync_transactions():
    """
    Synchronize the transaction history for all addresses
    """
    return "sync_transactions"
