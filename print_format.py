import poker_sim as p


def print_col():
    """
    This function prints 9 headings for 9 columns in the output table.
    :return: print out all the headings in order.
    """
    print('{:>10} {:>12} {:^7} {:>11} {:^7} {:>11} {:^7} {:>11} {:^7}'.format(
        '# of hands', 'pairs', '%', '2 pairs', '%', 'flushes', '%', 'high card', '%'))


def print_row(output, each_round):
    """
    This function prints 10 rows displaying number and percentage of each category in every 10000 hands dealt.
    :param output: a list containing number of cards in each category.
    :param each_round: rounds of every 10000 hands dealt to player.
    :return: prints 10 rows in order displaying number and percentage of each category in every 10000 hands dealt.
    """
    print('{:>10,}'.format(each_round), end='')
    for category in output:
        print('{:>13}'.format(category), " ", end='')
        print('{:.2f}'.format((100 * (category/each_round))).zfill(5), end='')


if __name__ == "__main__":
    print_col()
    print_row(p.round_output(10000), 10000)
