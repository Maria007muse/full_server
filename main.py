from flask import Flask

from api.queries_api import queries_api
from api.deals_api import deals_api
from api.deal_types_api import deal_types_api
from api.deal_place_api import deal_place_api
from api.currency_api import currency_api
from db.database_setup import create_tables, insert_data

app = Flask(__name__)

app.register_blueprint(deals_api)
app.register_blueprint(deal_types_api)
app.register_blueprint(deal_place_api)
app.register_blueprint(currency_api)
app.register_blueprint(queries_api)

create_tables()
insert_data()

if __name__ == '__main__':
    app.run(debug=True, port=8000)


