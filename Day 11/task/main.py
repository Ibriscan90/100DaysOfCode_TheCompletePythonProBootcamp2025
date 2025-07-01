from os import replace

from art import logo
import random

def play_blackJack():


    player_hand = []
    dealer_hand = []
    dealer_score = -1
    user_score = -1

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if len(cards) == 2 and sum(cards) == 21:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_scores(user_score, dealer_score):

        if user_score == dealer_score:
            return "It`s a draw!"
        elif dealer_score == 0:
            return "The dealer has won the game! You lost!"
        elif user_score == 0:
            return "The player has won the game!"
        elif user_score > 21:
            return "The player lost!"
        elif dealer_score > 21:
            return "The dealer lost!"
        elif user_score > dealer_score:
            return "The player has won the game"
        else:
            return "The dealer won the game"


    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    is_game_over = False
    while not is_game_over:

        user_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Player cards: {player_hand}, current score: {user_score}")
        print(f"Dealer card : {dealer_hand[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = str(input("Do you want to draw another card? Press Y for yes and N for no.")).lower()
            if user_should_deal == "y":
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append((deal_card()))
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {user_score}")
    print(f"Dealers final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare_scores(user_score, dealer_score))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n" * 20)
        play_blackJack()



play_blackJack()

