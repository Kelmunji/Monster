from models import Trade
from database import session

def propose_trade(from_player, to_player, offered_monsters, requested_monsters):
    trade = Trade(from_player_id=from_player.id, to_player_id=to_player.id,
                  offered_monsters=offered_monsters, requested_monsters=requested_monsters)
    session.add(trade)
    session.commit()

def accept_trade(trade_id):
    trade = session.query(Trade).get(trade_id)
    # Logic for executing trade (moving monsters between players)
    session.commit()
