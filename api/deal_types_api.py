from flask import Blueprint, jsonify, request
from db.database import connect_to_database

deal_types_api = Blueprint('deal_types_api', __name__)

@deal_types_api.route('/api/deal_types', methods=['GET'])
def get_deal_types():
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM deal_type;')
    deal_types = cursor.fetchall()
    conn.close()
    return jsonify(deal_types)

@deal_types_api.route('/api/deal_types/<int:deal_type_id>', methods=['GET'])
def get_deal_type(deal_type_id):
    conn, cursor = connect_to_database()
    cursor.execute('SELECT * FROM deal_type WHERE id = %s;', (deal_type_id,))
    deal_type = cursor.fetchone()
    conn.close()
    if deal_type:
        return jsonify(deal_type)
    else:
        return jsonify({'error': 'Тип сделки не найден'}), 404

@deal_types_api.route('/api/deal_types', methods=['POST'])
def create_deal_type():
    data = request.json
    new_deal_type = {
        "type": data['type']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
        INSERT INTO deal_type (type)
        VALUES (%(type)s);
    """, new_deal_type)
    conn.commit()
    conn.close()
    return jsonify(new_deal_type), 201

@deal_types_api.route('/api/deal_types/<int:deal_type_id>', methods=['PUT'])
def update_deal_type(deal_type_id):
    data = request.json
    updated_deal_type = {
        "id": deal_type_id,
        "type": data['type']
    }
    conn, cursor = connect_to_database()
    cursor.execute("""
        UPDATE deal_type SET type = %(type)s WHERE id = %(id)s;
    """, updated_deal_type)
    conn.commit()
    conn.close()
    return jsonify(updated_deal_type)

@deal_types_api.route('/api/deal_types/<int:deal_type_id>', methods=['DELETE'])
def delete_deal_type(deal_type_id):
    conn, cursor = connect_to_database()
    cursor.execute('DELETE FROM deal_type WHERE id = %s;', (deal_type_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Тип сделки успешно удален"}), 200
