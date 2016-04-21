import random

class Card():
    def __init__(self, value, name, suit):
        self.value = value
        self.name = name
        self.suit = suit

def init():
    cards = []
    for i in range(2, 11):
        cards.append(Card(i, str(i), "hearts"))
    cards.append(Card(11, "jack", "hearts"))
    cards.append(Card(12, "queen", "hearts"))
    cards.append(Card(13, "king", "hearts"))
    cards.append(Card(14, "ace", "hearts"))
    for i in range(2, 11):
        cards.append(Card(i, str(i), "spades"))
    cards.append(Card(11, "jack", "spades"))
    cards.append(Card(12, "queen", "spades"))
    cards.append(Card(13, "king", "spades"))
    cards.append(Card(14, "ace", "spades"))
    for i in range(2, 11):
        cards.append(Card(i, str(i), "clubs"))
    cards.append(Card(11, "jack", "clubs"))
    cards.append(Card(12, "queen", "clubs"))
    cards.append(Card(13, "king", "clubs"))
    cards.append(Card(14, "ace", "clubs"))
    for i in range(2, 11):
        cards.append(Card(i, str(i), "diamonds"))
    cards.append(Card(11, "jack", "diamonds"))
    cards.append(Card(12, "queen", "diamonds"))
    cards.append(Card(13, "king", "diamonds"))
    cards.append(Card(14, "ace", "diamonds"))
    return cards

def War(p1, p2, cards):

    random.shuffle(cards)

    p1cards = cards[0:26]
    p2cards = cards[26:]


    War1(p1, p2, p1cards, p2cards)

def War1(p1, p2, p1cards, p2cards):

    print("Time for war!")
    p1cards = p1cards
    p2cards = p2cards
    p1pile = []
    p2pile = []

    while len(p1cards) != 0 and len(p2cards) != 0:

        card1 = p1cards[0]
        del p1cards[0]
        print(p1 + " plays: " + card1.name + " of " + card1.suit)
        card2 = p2cards[0]
        del p2cards[0]
        print(p2 + " plays: " + card2.name + " of " + card2.suit)

        if card1.value > card2.value:
            print (p1 + " wins this war!")
            p1pile.append(card1)
            p1pile.append(card2)

        if card2.value > card1.value:
            print (p2 + " wins this war!")
            p2pile.append(card1)
            p2pile.append(card2)

        if card1.value == card2.value:
            print("the cards are even! WAR!!!")
            p1card = card1
            p2card = card2
            safety = []
            forsurecard1 = None
            forsurecard2 = None
            pile1 = []
            pile2 = []
            while (p1card.value == p2card.value):

                while len(pile1) != 3:
                    if len(p1cards) == 0 and len(p1pile) == 0:
                        forsurecard1 = p1card
                        break
                    if len(p1cards) == 1 and len(p1pile) == 0:
                        forsurecard1 = p1cards[0]
                        del p1cards[0]
                        break
                    if len(p1cards) == 0 and len(p1pile) != 0:
                        print (p1 + " ran out of cards. Shuffling their pile")
                        random.shuffle(p1pile)
                        p1cards = p1pile
                        p1pile = []
                    if len(p1cards) == 2:
                        pile1.append(p1cards[0])
                        del p1cards[0]
                        forsurecard1 = p1cards[0]
                        del p1cards[0]
                        break
                    else:
                        pile1.append(p1cards[0])
                        del p1cards[0]
                if forsurecard1 == None:
                    forsurecard1 = p1cards[0]
                    del p1cards[0]

                while len(pile2) != 3:
                    if len(p2cards) == 0 and len(p2pile) == 0:
                        forsurecard2 = p2card
                        break
                    if len(p2cards) == 1 and len(p2pile) == 0:
                        forsurecard2 = p2cards[0]
                        del p2cards[0]
                        break
                    if len(p2cards) == 0 and len(p2pile) != 0:
                        print (p2 + " ran out of cards. Shuffling their pile")
                        random.shuffle(p2pile)
                        p2cards = p2pile
                        p2pile = []
                    if len(p2cards) == 2:
                        pile2.append(p2cards[0])
                        del p2cards[0]
                        forsurecard2 = p2cards[0]
                        del p2cards[0]
                        break
                    else:
                        pile2.append(p2cards[0])
                        del p2cards[0]
                if forsurecard2 == None:
                    forsurecard2 = p2cards[0]
                    del p2cards[0]

                print(p1 + " plays " + forsurecard1.name + " of " + forsurecard1.suit)
                print(p2 + " plays " + forsurecard2.name + " of " + forsurecard2.suit)

                if forsurecard2.value > forsurecard1.value:
                    print(p2 + " wins the war!")
                    if forsurecard1 not in safety:
                        p2pile.append(forsurecard1)
                    if forsurecard2 not in safety:
                        p2pile.append(forsurecard2)
                    if forsurecard1 != p1card and p1card not in safety:
                        p2pile.append(p1card)
                    if forsurecard2 != p2card and p2card not in safety:
                        p2pile.append(p2card)
                    for card in pile1:
                        print(p1 + " loses the " + card.name + " of " + card.suit)
                        p2pile.append(card)
                    for card in pile2:
                        p2pile.append(card)
                    for card in safety:
                        p2pile.append(card)
                    break
                if forsurecard1.value > forsurecard2.value:
                    print (p1 + " wins the war!")
                    if forsurecard1 not in safety:
                        p1pile.append(forsurecard1)
                    if forsurecard2 not in safety:
                        p1pile.append(forsurecard2)
                    if forsurecard1 != p1card and p1card not in safety:
                        p1pile.append(p1card)
                    if forsurecard2 != p2card and p2card not in safety:
                        p1pile.append(p2card)
                    for card in pile1:
                        print(p2 + " loses the " + card.name + " of " + card.suit)
                        p1pile.append(card)
                    for card in pile2:
                        p1pile.append(card)
                    for card in safety:
                        p1pile.append(card)
                    break
                else:
                    print("Another war!!!")
                    safety.append(p1card)
                    safety.append(p2card)
                    safety.extend(pile1)
                    safety.extend(pile2)
                    p1card = forsurecard1
                    p2card = forsurecard2
                    forsurecard1 = None
                    forsurecard2 = None
                    pile1 = []
                    pile2 = []

        if p1cards == []:
            print(p1 + " has no cards. Shuffling their pile")
            random.shuffle(p1pile)
            p1cards = p1pile
            p1pile = []
        if p2cards == []:
            print (p2 + " has no cards. Shuffling their pile")
            random.shuffle(p2pile)
            p2cards = p2pile
            p2pile = []

    if p1cards == []:
        print (p1 + " has no more cards.")
        print (p2 + " wins the war!")
        input()
        exit()
    else:
        print (p2 + " has no more cards.")
        print (p1 + " wins the war!")
        input("press ENTER")
        exit()


def main():
    p1 = input("Enter a name for player 1: ")
    p2 = input("Enter a name for player 2: ")
    cards = init()
    War(p1, p2, cards)

main()
