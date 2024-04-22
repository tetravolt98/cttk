from flask import Blueprint

addresses_bp = Blueprint('addresses', __name__)


@addresses_bp.route("", methods=["GET"])
def get_addresses():
    """
    Get list of all addresses owned by the user
    :return:
    """
    return "get_addresses"


@addresses_bp.route("/<address>", methods=["POST"])
def add_address(address):
    """
    Add a new address to users list of addresses
    :return:
    """
    return "add_address"



@addresses_bp.route("/<address>", methods=["DELETE"])
def remove_address(address):
    """
    Remove an address from users list of addresses
    :return:
    """
    return "remove_address"
