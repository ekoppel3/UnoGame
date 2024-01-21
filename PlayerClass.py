from DeckClass import Deck
from CardClass import Card
import random


class Player:
    deck = Deck()

    def __init__(self):
        self.hand = []
        self.initialize_hand()

    def initialize_hand(self):
        count = 0
        while count < 7:
            card = random.choice(self.deck.arr_of_cards)
            self.deck.arr_of_cards.remove(card)
            self.hand.append(card)
            count += 1


class ComputerPlayer(Player):

    def play_card(self):
        played_card = False
        card = self.deck.open_card()
        for c in self.hand:
            if c.number == card.number or c.color == card.color:
                self.deck.discard.append(c)
                self.hand.remove(c)
                print(f"Computer played {c}")
                played_card = True
                break
        if not played_card:
            new_card = random.choice(self.deck.arr_of_cards)
            self.deck.arr_of_cards.remove(new_card)
            self.hand.append(new_card)
            print(f"Computer drew a card")


class HumanPlayer(Player):

    def turn(self):
        card = self.deck.open_card()
        choice = input("which card do you want to play?")
        try:
            if self.hand[int(choice)].number == card.number or self.hand[int(choice)].color == card.color:
                self.deck.discard.append(self.hand[int(choice)])
                self.hand.remove(self.hand[int(choice)])
            else:
                print("Nice try but that's not an option, take a card from the deck")
                c = self.deck.arr_of_cards[0]
                self.deck.arr_of_cards.remove(c)
                self.hand.append(c)
                print(f"You have picked card: {c}")
        except IndexError:
            print("Not a valid card. Try again.")
            self.turn()
        except ValueError:
            print("Take a card from the deck")
            c = self.deck.arr_of_cards[0]
            self.deck.arr_of_cards.remove(c)
            self.hand.append(c)
            print(f"You have picked card: {c}")

    def print_hand(self):
        s = "You have the following cards:  "
        count = 0
        for c in self.hand:
            s += f" Card {count}: {c} "
            count += 1
        print(s)
