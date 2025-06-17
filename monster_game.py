import argparse
from player_management import create_player, view_profile
from game_logic import explore, catch_monster, battle_wild, battle_player
from trading_system import trade_monster
from achievements import unlock_achievement

def main():
    parser = argparse.ArgumentParser(description="Monster Collector Game")
    parser.add_argument('command', choices=['start', 'explore', 'catch', 'battle', 'profile', 'trade'], help="Game command")
    parser.add_argument('--username', type=str, help="Player's username")
    parser.add_argument('--opponent', type=str, help="Opponent's username for PvP battle")
    
    args = parser.parse_args()

    if args.command == 'start':
        if args.username:
            create_player(args.username)
        else:
            print("Please provide a username to start the game.")
    
    elif args.command == 'explore':
        explore(args.username)
    
    elif args.command == 'catch':
        catch_monster(args.username)
    
    elif args.command == 'battle':
        if args.opponent:
            battle_player(args.username, args.opponent)
        else:
            battle_wild(args.username)
    
    elif args.command == 'profile':
        view_profile(args.username)
    
    elif args.command == 'trade':
        trade_monster(args.username)
        
if __name__ == "__main__":
    main()
