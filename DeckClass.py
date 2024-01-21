from CardClass import Card
import random


class Deck:

    def __init__(self):
        self.arr_of_cards = []
        self.discard = []
        self.make_deck()

    def shuffle_deck(self):
        random.shuffle(self.arr_of_cards)

    def make_deck(self):
        i = 0
        while i < 10:
            red = Card("red", i)
            self.arr_of_cards.append(red)
            self.arr_of_cards.append(red)
            green = Card("green", i)
            self.arr_of_cards.append(green)
            self.arr_of_cards.append(green)
            blue = Card("blue", i)
            self.arr_of_cards.append(blue)
            self.arr_of_cards.append(blue)
            yellow = Card("yellow", i)
            self.arr_of_cards.append(yellow)
            self.arr_of_cards.append(yellow)
            i += 1

    def __str__(self):
        cards = ""
        c = Card
        for c in self.arr_of_cards:
            cards += f" {c}, "
        return cards

    def flip_card(self):
        card = self.arr_of_cards[0]
        self.arr_of_cards.remove(card)
        self.discard.append(card)
        return card

    def open_card(self):
        if len(self.discard) > 0:
            card = self.discard.pop()
            self.discard.append(card)
            return card
        else:
            return self.flip_card()

    def reshuffle(self):
        card = self.open_card()
        self.discard.remove(card)
        count = 0
        for c in self.discard:
            self.arr_of_cards.append(c)
            self.discard.remove(c)
        self.discard.append(card)

