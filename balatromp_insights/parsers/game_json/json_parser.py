from datetime import date
from typing import Any, Literal
from pydantic import BaseModel, AwareDatetime

from balatromp_insights.utils import raise_if_none

WinnerOption = Literal["logOwner", "opponent"]

class GameLog(BaseModel):
    id: int
    host: str | None
    guest: str | None
    lobby_code: str | None
    log_owner_name: str | None
    opponent_name: str | None
    host_mods: list[str]
    guest_mods: list[str]
    is_host: bool | None
    deck: str | None
    cocktail_decks: list[str] | None
    seed: str | None
    log_owner_deck_size: int
    opponent_deck_size: int
    money_gained: int
    money_spent: int
    opponent_money_spent: int
    start_date: AwareDatetime
    end_date: AwareDatetime | None
    duration_seconds: int | None
    opponent_last_lives: int
    opponent_last_skips: int
    money_spent_per_shop: list[int | None] 
    money_spent_per_shop_opponent: list[int | None]
    log_owner_final_jokers: list[str]
    opponent_final_jokers: list[str]
    rerolls: int
    reroll_cost_total: int
    log_owner_vouchers: list[str]
    opponent_rerolls: int
    opponent_reroll_cost_total: int
    opponent_vouchers: list[str]
    winner: WinnerOption | None
    current_pvp_blind: int | None


    @staticmethod
    def from_json(json_object: dict[str, Any]) -> "GameLog":

        _id = raise_if_none(json_object.get("id"))
        _host_mods = raise_if_none(json_object.get("hostMods"))
        _guest_mods = raise_if_none(json_object.get("guestMods"))
        _money_gained = raise_if_none(json_object.get("moneyGained"))
        _money_spent = raise_if_none(json_object.get("moneySpent"))
        _opponent_money_spent = raise_if_none(json_object.get("opponentMoneySpent"))
        _start_date = raise_if_none(json_object.get("startDate"))
        _opponent_last_lives = raise_if_none(json_object.get("opponentLastLives"))
        _opponent_last_skips = raise_if_none(json_object.get("opponentLastSkips"))
        _money_spent_per_shop = raise_if_none(json_object.get("moneySpentPerShop"))
        _money_spent_per_shop_opponent = raise_if_none(json_object.get("moneySpentPerShopOpponent"))
        _log_owner_final_jokers = raise_if_none(json_object.get("logOwnerFinalJokers"))
        _opponent_final_jokers = raise_if_none(json_object.get("opponentFinalJokers"))
        _rerolls = raise_if_none(json_object.get("rerolls"))
        _reroll_cost_total = raise_if_none(json_object.get("rerollCostTotal"))
        _log_owner_vouchers = raise_if_none(json_object.get("logOwnerVouchers"))
        _opponent_rerolls = raise_if_none(json_object.get("opponentRerolls"))
        _opponent_reroll_cost_total = raise_if_none(json_object.get("opponentRerollCostTotal"))
        _opponent_vouchers = raise_if_none(json_object.get("opponentVouchers"))

        _opponent_deck_size = len(raise_if_none(json_object.get("opponentDeck")))
        _log_owner_deck_size = len(raise_if_none(json_object.get("logOwnerDeck")))

        return GameLog(
            id = _id,
            host = json_object.get("host"),
            guest = json_object.get("guest"),
            lobby_code = json_object.get("lobbyCode"),
            log_owner_name = json_object.get("logOwnerName"),
            opponent_name = json_object.get("opponentName"),
            host_mods = _host_mods,
            guest_mods = _guest_mods,
            is_host = json_object.get("isHost"),
            deck = json_object.get("deck"),
            cocktail_decks = json_object.get("cocktailDecks"),
            seed = json_object.get("seed"),
            log_owner_deck_size = _opponent_deck_size,
            opponent_deck_size = _log_owner_deck_size,
            money_gained = _money_gained,
            money_spent = _money_spent,
            opponent_money_spent = _opponent_money_spent,
            start_date = _start_date,
            end_date = json_object.get("endDate"),
            duration_seconds = json_object.get("durationSeconds"),
            opponent_last_lives = _opponent_last_lives,
            opponent_last_skips = _opponent_last_skips,
            money_spent_per_shop = _money_spent_per_shop,
            money_spent_per_shop_opponent = _money_spent_per_shop_opponent,
            log_owner_final_jokers = _log_owner_final_jokers,
            opponent_final_jokers = _opponent_final_jokers,
            rerolls = _rerolls,
            reroll_cost_total = _reroll_cost_total,
            log_owner_vouchers = _log_owner_vouchers,
            opponent_rerolls = _opponent_rerolls,
            opponent_reroll_cost_total = _opponent_reroll_cost_total,
            opponent_vouchers = _opponent_vouchers,
            winner = json_object.get("winner"),
            current_pvp_blind = json_object.get("currentPvpBlind"),
        )




































