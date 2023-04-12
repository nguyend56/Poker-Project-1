
import random
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["S", "C", "D", "H"]


def create_deck():
    """
    This function create a deck of 52 cards.
    :return: a list containing all the cards in one deck, each card is a tuple containing 2 elements: rank and suit
    """
    deck = []
    for rank in ranks:
        for suit in suits:
            card = (rank, suit)
            deck.append(card)
    return deck


def shuffle_deck(deck):
    """
    This function shuffles the cards in the deck.
    :param deck: a list containing all the cards in one deck.
    :return: a shuffled list of cards.
    """
    random.shuffle(deck)
    return deck


if __name__ == "__main__":
    create_deck()
