INSERT INTO deal_type (type) VALUES
                                 ('Брокерская'),
                                 ('Дилерская');

INSERT INTO deal_place (deal_place_full, deal_place_short) VALUES
                                                               ('Биржевая площадка 1', 'БП1'),
                                                               ('Биржевая площадка 2', 'БП2');

INSERT INTO currency (currency_full, currency_short) VALUES
                                                         ('Доллар США', 'USD'),
                                                         ('Евро', 'EUR');

INSERT INTO deals (type_id, place_id, currency_id, ticker, order_number, deal_number, deal_quantity, deal_price, deal_total_cost, deal_trader, deal_commission) VALUES
                                                                                                                                                                    (1, 1, 1, 'AAPL', '123456', '7890', 100, 150.25, 15025.00, 'John Doe', 10.00),
                                                                                                                                                                    (2, 2, 2, 'GOOG', '987654', '3210', 50, 250.75, 12537.50, 'Jane Smith', 8.50),
                                                                                                                                                                    (1, 1, 2, 'MSFT', '456789', '0987', 75, 175.50, 13162.50, 'Alice Johnson', 12.00);
