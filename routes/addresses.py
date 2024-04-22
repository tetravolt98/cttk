import sqlite3

from flask import Blueprint, jsonify

from db import get_db

addresses_bp = Blueprint('addresses', __name__)


@addresses_bp.route("", methods=["GET"])
def get_addresses():
    """
    Get list of all addresses owned by the user
    :return:
    """
    # TODO - pagination if time
    db = get_db()
    cur = db.execute("""SELECT address FROM addresses""")
    addresses = [row[0] for row in cur.fetchall()]
    return jsonify({"addresses": addresses}), 200


@addresses_bp.route("/<address>", methods=["POST"])
def add_address(address):
    """
    Add a new address to users list of addresses
    :return:
    """
    db = get_db()
    try:
        db.execute("""INSERT INTO addresses (address) VALUES (?)""", (address,))
        db.commit()
        return jsonify({"message": "success"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Address already exists", "address": address}), 200


@addresses_bp.route("/<address>", methods=["DELETE"])
def remove_address(address):
    """
    Remove an address from users list of addresses
    :return:
    """
    db = get_db()
    db.execute("""DELETE FROM addresses WHERE address = ?""", (address,))
    db.commit()
    return jsonify({"message": "success"})
