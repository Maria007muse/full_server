from flask import Blueprint, jsonify, request
from db.database import connect_to_database

deals_api = Blueprint('deals_api', __name__)

@deals_api.route('/api/deals', methods=['GET'])
def get_deals():
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM deals;')
    deals = cursor.fetchall()
    conn.close()
    return jsonify(deals)

@deals_api.route('/api/deals/<int:deal_id>', methods=['GET'])
def get_deal(deal_id):
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM deals WHERE id = %s;', (deal_id,))
    deal = cursor.fetchone()
    conn.close()
    if deal:
        return jsonify(deal)
    else:
        return jsonify({'error': 'Сделка не найдена'}), 404

@deals_api.route('/api/deals', methods=['POST'])
def create_deal():
    data = request.json
    new_deal = {
        "type_id": data['type_id'],
        "place_id": data['place_id'],
        "currency_id": data['currency_id'],
        "ticker": data['ticker'],
        "order_number": data['order_number'],
        "deal_number": data['deal_number'],
        "deal_quantity": data['deal_quantity'],
        "deal_price": data['deal_price'],
        "deal_total_cost": data['deal_total_cost'],
        "deal_trader": data['deal_trader'],
        "deal_commission": data['deal_commission']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
        INSERT INTO deals (type_id, place_id, currency_id, ticker, order_number, deal_number, deal_quantity, deal_price, deal_total_cost, deal_trader, deal_commission)
        VALUES (%(type_id)s, %(place_id)s, %(currency_id)s, %(ticker)s, %(order_number)s, %(deal_number)s, %(deal_quantity)s, %(deal_price)s, %(deal_total_cost)s, %(deal_trader)s, %(deal_commission)s);
    """, new_deal)
    conn.commit()
    conn.close()
    return jsonify(new_deal), 201

@deals_api.route('/api/deals/<int:deal_id>', methods=['PUT'])
def update_deal(deal_id):
    data = request.json
    updated_deal = {
        "id": deal_id,
        "type_id": data['type_id'],
        "place_id": data['place_id'],
        "currency_id": data['currency_id'],
        "ticker": data['ticker'],
        "order_number": data['order_number'],
        "deal_number": data['deal_number'],
        "deal_quantity": data['deal_quantity'],
        "deal_price": data['deal_price'],
        "deal_total_cost": data['deal_total_cost'],
        "deal_trader": data['deal_trader'],
        "deal_commission": data['deal_commission']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
    UPDATE deals SET type_id = %(type_id)s, place_id = %(place_id)s, currency_id = %(currency_id)s, ticker = %(ticker)s,
    order_number = %(order_number)s, deal_number = %(deal_number)s, deal_quantity = %(deal_quantity)s, deal_price = %(deal_price)s,
    deal_total_cost = %(deal_total_cost)s, deal_trader = %(deal_trader)s, deal_commission = %(deal_commission)s WHERE id = %(id)s;
""", updated_deal)
    conn.commit()
    conn.close()
    return jsonify(updated_deal)

@deals_api.route('/api/deals/<int:deal_id>', methods=['DELETE'])
def delete_deal(deal_id):
    conn, cursor = connect_to_database()
    cursor.execute('DELETE FROM deals WHERE id = %s;', (deal_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Сделка успешно удалена"}), 200
