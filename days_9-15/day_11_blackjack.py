import random

game = True
while game:
    if input("Want to play a game of Black Jack - 'Y' or 'N': ").lower() != "y":
        game = False
        print("Bye!")
    else:
        def deal():
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            return random.choice(cards)

        def calculate(hand):
            if sum(hand) == 21:
                return 0
            else:
                return sum(hand)

        def evaluate(score1, score2):
            if calculate(score1) == calculate(score2):
                return "Draw"
            elif calculate(score2) == 0:
                return "Dealer has BlackJack. You lose!"
            elif calculate(score1) == 0:
                return "Nailed it. Blackjack!!"
            elif calculate(player_hand) > 21:
                return "Way over. Lose.."
            elif calculate(dealer_hand) > 21:
                return "Dealer went over. You win!"
            elif calculate(player_hand) > calculate(dealer_hand):
                return "You win!"
            else:
                return "You lose.."

        player_hand = [deal(), deal()]
        dealer_hand = [deal(), deal()]

        game_on = True
        while game_on:
            if calculate(player_hand) == 0 or calculate(dealer_hand) == 0 or sum(player_hand) > 21:
                if sum(player_hand) > 21 and 11 in player_hand:
                    player_hand.remove(11)
                    player_hand.append(1)
                else:
                    game_on = False
            else:
                print(" ", f"Your cards: {player_hand}, current score: {sum(player_hand)}")
                print(" ", f"Dealer has '{dealer_hand[0]}'.")
                if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
                    player_hand.append(deal())
                else:
                    game_on = False
                    while sum(dealer_hand) < 17:
                        dealer_hand.append(deal())

        print(f"  Your final cards: {player_hand}, final score: {sum(player_hand)}")
        print(f"  Dealer's final cards: {dealer_hand}, final score: {sum(dealer_hand)}")
        print(evaluate(player_hand, dealer_hand))
