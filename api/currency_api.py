from flask import Blueprint, jsonify, request
from db.database import connect_to_database

currency_api = Blueprint('currency_api', __name__)

@currency_api.route('/api/currencies', methods=['GET'])
def get_currencies():
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM currency;')
    currencies = cursor.fetchall()
    conn.close()
    return jsonify(currencies)

@currency_api.route('/api/currencies/<int:currency_id>', methods=['GET'])
def get_currency(currency_id):
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM currency WHERE id = %s;', (currency_id,))
    currency = cursor.fetchone()
    conn.close()
    if currency:
        return jsonify(currency)
    else:
        return jsonify({'error': 'Валюта не найдена'}), 404

@currency_api.route('/api/currencies', methods=['POST'])
def create_currency():
    data = request.json
    new_currency = {
        "currency_full": data['currency_full'],
        "currency_short": data['currency_short']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
        INSERT INTO currency (currency_full, currency_short)
        VALUES (%(currency_full)s, %(currency_short)s);
    """, new_currency)
    conn.commit()
    conn.close()
    return jsonify(new_currency), 201

@currency_api.route('/api/currencies/<int:currency_id>', methods=['PUT'])
def update_currency(currency_id):
    data = request.json
    updated_currency = {
        "id": currency_id,
        "currency_full": data['currency_full'],
        "currency_short": data['currency_short']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
        UPDATE currency SET currency_full = %(currency_full)s, currency_short = %(currency_short)s WHERE id = %(id)s;
    """, updated_currency)
    conn.commit()
    conn.close()
    return jsonify(updated_currency)

@currency_api.route('/api/currencies/<int:currency_id>', methods=['DELETE'])
def delete_currency(currency_id):
    conn, cursor = connect_to_database()
    cursor.execute('DELETE FROM currency WHERE id = %s;', (currency_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Валюта успешно удалена"}), 200
