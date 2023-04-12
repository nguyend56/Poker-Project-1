import deck as d


def create_hand(deck):
    """
    This function deals a hand to player.
    :param deck: a list containing all the cards in the deck
    :return: a list containing all the cards in a hand dealt to player, specifically 5 cards.
    """
    hand = []
    while len(hand) < 5:
        hand.append(deck[0])
        deck.pop(0)
    hand.sort()
    return hand


if __name__ == "__main__":
    create_hand(d.create_deck())

