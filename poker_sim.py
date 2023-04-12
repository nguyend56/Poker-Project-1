

import check_hand as ch
import deck as d
import hand as h
import print_format as pr


def round_output(each_round):
    """
    This function counts number of cards in each category for one round of 10000 hands dealt
    :param each_round: rounds of every 10000 hands dealt to player.
    :return: a list containing numbers of cards in each category for one round of 10000 hands dealt
    """
    deck_of_card = d.shuffle_deck(d.create_deck())
    number_of_pairs = 0
    number_of_two_pairs = 0
    number_of_flushes = 0
    number_of_high_card = 0
    number_of_hand = 0
    while number_of_hand < each_round:
        if len(deck_of_card) < 5:
            deck_of_card = d.shuffle_deck(d.create_deck())
        else:
            the_hand = h.create_hand(deck_of_card)
            if ch.check_pair(the_hand):
                number_of_pairs += 1
            elif ch.check_2pairs(the_hand):
                number_of_two_pairs += 1
            elif ch.check_flush(the_hand):
                number_of_flushes += 1
            else:
                number_of_high_card += 1
            number_of_hand += 1
    output = [number_of_pairs, number_of_two_pairs, number_of_flushes, number_of_high_card]
    return output


def play_rounds():
    """
    This function executes the game, print outs the numbers and percentage of
    all categories for every round of 10000 hands dealt.
    :return: a table displaying the numbers and percentage of
    all categories for every round of 10000 hands dealt.
    """
    number_of_card_each_round = 10000
    pr.print_col()
    for i in range(0, 100000, 10000):
        pr.print_row(round_output(number_of_card_each_round), number_of_card_each_round)
        print()
        number_of_card_each_round += 10000


if __name__ == "__main__":
    play_rounds()

