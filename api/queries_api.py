from flask import Blueprint, jsonify
from db.database import connect_to_database

queries_api = Blueprint('queries_api', __name__)


#-----ЗАПРОСЫ-----
#1. Получение всех сделок для конкретного типа сделки

@queries_api.route('/api/deals_by_type/<string:deal_type>', methods=['GET'])
def get_deals_by_type(deal_type):
    conn, cursor = connect_to_database()
    cursor.execute("""
        SELECT deals.*
        FROM deals
        INNER JOIN deal_type ON deals.type_id = deal_type.id
        WHERE deal_type.type = %s;
    """, (deal_type,))
    deals_by_type = cursor.fetchall()
    conn.close()
    return jsonify(deals_by_type)

#2. Получение всех сделок, совершенных на определенной биржевой площадке

@queries_api.route('/api/deals_by_place/<string:place>', methods=['GET'])
def get_deals_by_place(place):
    conn, cursor = connect_to_database()
    cursor.execute("""
        SELECT deals.*
        FROM deals
        INNER JOIN deal_place ON deals.place_id = deal_place.id
        WHERE deal_place.deal_place_full = %s;
    """, (place,))
    deals_by_place = cursor.fetchall()
    conn.close()
    return jsonify(deals_by_place)

#3. Получение всех сделок с суммой больше определенной

@queries_api.route('/api/deals_cost_above/<float:amount>', methods=['GET'])
def get_deals_with_total_cost_above(amount):
    conn, cursor = connect_to_database()
    cursor.execute("""
        SELECT deals.*
        FROM deals
        WHERE deals.deal_total_cost > %s;
    """, (amount,))
    deals_with_total_cost_above = cursor.fetchall()
    conn.close()
    return jsonify(deals_with_total_cost_above)

#4. сделки с деталями о типе сделки и валюте, совершенных на определенной биржевой площадке

@queries_api.route('/api/deals_with_type_and_currency_by_place/<string:place>', methods=['GET'])
def get_deals_with_type_and_currency_by_place(place):
    conn, cursor = connect_to_database()
    cursor.execute("""
        SELECT deals.id, deal_type.type AS deal_type, currency.currency_full AS currency
        FROM deals
        INNER JOIN deal_type ON deals.type_id = deal_type.id
        INNER JOIN currency ON deals.currency_id = currency.id
        WHERE deals.place_id = (
            SELECT id FROM deal_place WHERE deal_place_full = %s
        );
    """, (place,))
    deals_with_type_and_currency_by_place = cursor.fetchall()
    conn.close()
    return jsonify(deals_with_type_and_currency_by_place)

#5. Получение суммарной стоимости всех сделок для каждого типа сделки

@queries_api.route('/api/total_cost_by_deal_type', methods=['GET'])
def get_total_cost_by_deal_type():
    conn, cursor = connect_to_database()
    cursor.execute("""
        SELECT deal_type.type AS deal_type, SUM(deals.deal_total_cost) AS total_cost
        FROM deals
        INNER JOIN deal_type ON deals.type_id = deal_type.id
        GROUP BY deal_type.type;
    """)
    total_cost_by_deal_type = cursor.fetchall()
    conn.close()
    return jsonify(total_cost_by_deal_type)

#6. Получение средней цены сделок для каждой валюты

@queries_api.route('/api/average_price_by_currency', methods=['GET'])
def get_average_price_by_currency():
    conn, cursor = connect_to_database()
    cursor.execute("""
        SELECT currency.currency_full AS currency, AVG(deals.deal_price) AS average_price
        FROM deals
        INNER JOIN currency ON deals.currency_id = currency.id
        GROUP BY currency.currency_full;
    """)
    average_price_by_currency = cursor.fetchall()
    conn.close()
    return jsonify(average_price_by_currency)

#7. Получение кол-ва сделок, совершенных каждым трейдером

@queries_api.route('/api/deals_count_by_trader', methods=['GET'])
def get_deals_count_by_trader():
    conn, cursor = connect_to_database()
    cursor.execute("""
        SELECT deals.deal_trader AS trader, COUNT(*) AS deals_count
        FROM deals
        GROUP BY deals.deal_trader;
    """)
    deals_count_by_trader = cursor.fetchall()
    conn.close()
    return jsonify(deals_count_by_trader)

