CREATE TABLE IF NOT EXISTS jokers (
    joker_id INT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS joker_sets (
    joker_set_id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS joker_set_items (
    joker_set_id INTEGER NOT NULL,
    joker_id INTEGER NOT NULL,
    position INTEGER NOT NULL,

    PRIMARY KEY (joker_set_id, position),

    FOREIGN KEY(joker_set_id) REFERENCES joker_sets(joker_set_id),
    FOREIGN KEY(joker_id) REFERENCES jokers(joker_id)
);

CREATE TABLE IF NOT EXISTS vouchers (
    voucher_id INT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS voucher_sets (
    voucher_set_id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS voucher_set_items (
    voucher_set_id INTEGER NOT NULL,
    voucher_id INTEGER NOT NULL,
    position INTEGER NOT NULL,

    PRIMARY KEY (voucher_set_id, position),

    FOREIGN KEY(voucher_set_id) REFERENCES voucher_sets(voucher_set_id),
    FOREIGN KEY(voucher_id) REFERENCES vouchers(voucher_id)
);

CREATE TABLE IF NOT EXISTS mods (
    mod_id INT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS mod_lists (
    mod_list_id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS mod_list_items (
    mod_list_id INTEGER NOT NULL,
    mod_id INTEGER NOT NULL,

    PRIMARY KEY (mod_id, mod_list_id),

    FOREIGN KEY(mod_list_id) REFERENCES mod_lists(mod_list_id),
    FOREIGN KEY(mod_id) REFERENCES mods(mod_id)
);

CREATE TABLE IF NOT EXISTS games (
    game_id INT PRIMARY KEY,
    host TEXT,
    guest TEXT,
    lobby_code TEXT,
    log_owner_name TEXT,
    opponent_name TEXT,
    host_mod_list_id INTEGER NOT NULL,
    guest_mod_list_id INTEGER NOT NULL,
    is_host INTEGER,
    deck TEXT,
    cocktail_decks TEXT,
    seed TEXT,
    log_owner_deck_size INTEGER NOT NULL,
    opponent_deck_size INTEGER NOT NULL,
    money_gained INTEGER NOT NULL,
    money_spent INTEGER NOT NULL,
    opponent_money_spent INTEGER NOT NULL,
    start_date INTEGER NOT NULL,  
    end_date INTEGER,
    duration_seconds INTEGER,
    opponent_last_lives INTEGER NOT NULL,
    opponent_last_skips INTEGER NOT NULL,
    log_owner_final_jokers INTEGER NOT NULL,
    opponent_final_jokers INTEGER NOT NULL,
    rerolls INTEGER NOT NULL,
    reroll_cost_total INTEGER NOT NULL,
    log_owner_vouchers INTEGER NOT NULL,
    opponent_rerolls INTEGER NOT NULL,
    opponent_reroll_cost_total INTEGER NOT NULL,
    opponent_vouchers INTEGER NOT NULL,
    winner: WinnerOption | None,
    current_pvp_blind INTEGER
)

CREATE TABLE IF NOT EXISTS shop_spending (
    game_id  INTEGER NOT NULL,
    side INTEGER NOT NULL,
    shop_index INTEGER NOT NULL,
    amount INTEGER

    FOREIGN KEY(game_id) REFERENCES games(game_id)
)