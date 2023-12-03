import gvt

def print_players(player, opponent):
    print(repr(opponent))
    print()
    print(repr(player))

def take_turn(player, opponent):
    player.start_turn()
    print_players(player, opponent)

    while True:
        command = input(str(player) + " >> ")  # "P 2"
        tokens = command.split()  # ["P", "2"]
        if tokens[0].upper() == "Q":
            break
        elif tokens[0].upper() == "H":
            player.card_info(int(tokens[1]))
        elif tokens[0].upper() == "B":
            player.bat_info()
        elif tokens[0].upper() == "E":
            opponent.bat_info()
        elif tokens[0].upper() == "P":
            number = int(tokens[1])
            if player.play_card(number):
                print_players(player, opponent)
            else:
                print("Invalid card.")
        elif tokens[0].upper() == "I":
            print("H - Print hand\nB - Print own Battalion\nE - Print enemy Battalion\nP - play card\nQ - Quit turn")
        else:
            print("Invalid command.")

    opponent.attack(player.get_totalap())


def main():
    p1_name = input("Enter player 1 name: ")
    player1 = gvt.Player(p1_name, gvt.make_deck(gvt.GOATS))

    p2_name = input("Enter player 2 name: ")
    player2 = gvt.Player(p2_name, gvt.make_deck(gvt.TROLLS))

    player = player1
    opponent = player2

    while True:
        take_turn(player, opponent)
        if opponent.get_score() <= 0:
            print(player,"Wins")
            break
        elif player.get_deck_len() <= 0:
            print(opponent,"Wins")
            break
        player, opponent = opponent, player


    print(player,"Wins")

if __name__ == "__main__":
    main()
