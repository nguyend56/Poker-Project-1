import hand as h
import deck as d


def check_flush(hand):
    """
    This function checks if the player's hand is a flush or not.
    :param hand: a list containing all the cards in a hand dealt to player.
    :return: a boolean - True if the hand is a flush, otherwise return None.
    """
    root = hand[0][1]
    a = 0
    for i in range(len(hand)):
        if root == hand[i][1]:
            a += 1
    if a == 5:
        return True


def check_2pairs(hand):
    """
    This function checks if the player's hand is a two pair or not.
    :param hand: a list containing all the cards in a hand dealt to player.
    :return: a boolean - True if the hand is a two pair, otherwise return None.
    """
    pair_count = 0
    for i in range(0, len(hand)):
        for j in range(i):                   # this nested loop checks how many single pairs in player's hand.
            if hand[i][0] == hand[j][0]:
                pair_count += 1
    if pair_count == 2 or pair_count == 4 or pair_count == 6:
        # in 2 pairs category, there will be 2 separated pairs, thus if number of pair_count equals 2, this hand is
        # a two pair. Similarly, full house category has 4 single pairs (3 single pairs from 3 cards with the same rank
        # and 1 single pair from the 2 other cards left), four of a kind category has 6 single pairs from 4 cards with
        # the same rank.
        return True


def check_pair(hand):
    """
    This function checks if the player's hand is a pair or not.
    :param hand: a list containing all the cards in a hand dealt to player.
    :return: a boolean - True if the hand is a pair, otherwise return None.
    """
    pair_count = 0
    for i in range(0, len(hand)):
        for j in range(i):                   # this nested loop checks how many single pairs in player's hand.
            if hand[i][0] == hand[j][0]:
                pair_count += 1
    if pair_count == 1 or pair_count == 3:
        # in pair category, there will be 1 single pair, thus if number of pair_count equals 1, this hand is a pair.
        # in three of a kind category, 3 cards of a same rank have 3 single pairs, thus if number of pair_count equals
        # 3, this hand is a three of a kind.
        return True


if __name__ == "__main__":
    check_flush(h.create_hand(d.create_deck()))
    check_2pairs(h.create_hand(d.create_deck()))
    check_pair(h.create_hand(d.create_deck()))
