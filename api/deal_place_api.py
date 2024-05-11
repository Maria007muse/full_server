from flask import Blueprint, jsonify, request
from db.database import connect_to_database

deal_place_api = Blueprint('deal_place_api', __name__)

@deal_place_api.route('/api/deal_places', methods=['GET'])
def get_deal_places():
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM deal_place;')
    deal_places = cursor.fetchall()
    conn.close()
    return jsonify(deal_places)

@deal_place_api.route('/api/deal_places/<int:deal_place_id>', methods=['GET'])
def get_deal_place(deal_place_id):
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM deal_place WHERE id = %s;', (deal_place_id,))
    deal_place = cursor.fetchone()
    conn.close()
    if deal_place:
        return jsonify(deal_place)
    else:
        return jsonify({'error': 'Место проведения сделки не найдено'}), 404

@deal_place_api.route('/api/deal_places', methods=['POST'])
def create_deal_place():
    data = request.json
    new_deal_place = {
        "deal_place_full": data['deal_place_full'],
        "deal_place_short": data['deal_place_short']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
        INSERT INTO deal_place (deal_place_full, deal_place_short)
        VALUES (%(deal_place_full)s, %(deal_place_short)s);
    """, new_deal_place)
    conn.commit()
    conn.close()
    return jsonify(new_deal_place), 201

@deal_place_api.route('/api/deal_places/<int:deal_place_id>', methods=['PUT'])
def update_deal_place(deal_place_id):
    data = request.json
    updated_deal_place = {
        "id": deal_place_id,
        "deal_place_full": data['deal_place_full'],
        "deal_place_short": data['deal_place_short']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
        UPDATE deal_place SET deal_place_full = %(deal_place_full)s, deal_place_short = %(deal_place_short)s WHERE id = %(id)s;
    """, updated_deal_place)
    conn.commit()
    conn.close()
    return jsonify(updated_deal_place)

@deal_place_api.route('/api/deal_places/<int:deal_place_id>', methods=['DELETE'])
def delete_deal_place(deal_place_id):
    conn, cursor = connect_to_database()
    cursor.execute('DELETE FROM deal_place WHERE id = %s;', (deal_place_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Место проведения сделки успешно удалено"}), 200
