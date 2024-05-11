CREATE TABLE IF NOT EXISTS deal_type (
                                         id SERIAL PRIMARY KEY,
                                         type VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS deal_place (
                                          id SERIAL PRIMARY KEY,
                                          deal_place_full VARCHAR(255) NOT NULL,
                                          deal_place_short VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS currency (
                                        id SERIAL PRIMARY KEY,
                                        currency_full VARCHAR(255) NOT NULL,
                                        currency_short VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS deals (
                                     id SERIAL PRIMARY KEY,
                                     type_id BIGINT NOT NULL,
                                     place_id BIGINT NOT NULL,
                                     currency_id BIGINT NOT NULL,
                                     ticker VARCHAR(255) NOT NULL,
                                     order_number VARCHAR(255) NOT NULL,
                                     deal_number VARCHAR(255) NOT NULL,
                                     deal_quantity INTEGER NOT NULL,
                                     deal_price NUMERIC(20, 2) NOT NULL,
                                     deal_total_cost NUMERIC(20, 2) NOT NULL,
                                     deal_trader VARCHAR(255) NOT NULL,
                                     deal_commission NUMERIC(20, 2) NOT NULL,
                                     FOREIGN KEY (type_id) REFERENCES deal_type(id),
                                     FOREIGN KEY (place_id) REFERENCES deal_place(id),
                                     FOREIGN KEY (currency_id) REFERENCES currency(id)
);
