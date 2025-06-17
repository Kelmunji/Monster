from models import Player
from database import session

def create_player(username):
    player = Player(username=username)
    session.add(player)
    session.commit()

def view_profile(username):
    player = session.query(Player).filter_by(username=username).first()
    return {
        "username": player.username,
        "level": player.level,
        "experience": player.experience,
        "money": player.money
    }
