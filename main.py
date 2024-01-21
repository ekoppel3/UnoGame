from DeckClass import Deck
from PlayerClass import ComputerPlayer
from PlayerClass import HumanPlayer

#deck = Deck()

computer = ComputerPlayer()
you = HumanPlayer()
you.deck.shuffle_deck()
computer.deck.flip_card()
print("Welcome to Py-Uno")
print("See if you can beat artificial intelligence and prevail!")
print("On your turn, enter the number card you want to play.")
print("If you don't have anything tell it that by typing 'none' or 'take'")
print("Good Luck!")
print()
while len(computer.hand) != 0 and len(you.hand) != 0:
    print(f"The open card is: {you.deck.open_card()}")
    you.print_hand()
    you.turn()
    if len(you.hand) == 0:
        print("Wow! You won!")
        print("Doesn't it feel good?")
        break
    computer.play_card()
    if len(computer.hand) == 0:
        print("Game over, sorry the computer won")
        print("Go artificial intelligence!!!")
        break
    if len(computer.deck.arr_of_cards) == 0:
        you.deck.reshuffle()

