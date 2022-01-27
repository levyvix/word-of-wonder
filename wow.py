import itertools
from argparse import ArgumentParser

"""
Gera opções para preencher palavras no jogo Word of Wonders

- n: número de palavras
- words: lista de palavras
- mask: máscara para preencher as palavras
"""

# # words = input("Enter the words: ").split()
# argv = sys.argv[1:]

# words = argv[:5]
# number_of_words = argv[5]  # number of words to be printed
# mask = argv[6]  # mask to be used


# all the combinations of number_of_words words from the words list
def find_words(n_words=5, words='AEIOU', mask=str("")):
    # sourcery skip: de-morgan
    """
    Encontra todas as combinações de n_words palavras de words com a máscara mask

    Args:
    - n_words: número de palavras a serem usadas (default: 5)
    - words: lista de palavras (string)
    - mask: máscara para preencher as palavras (ex: 'S_L')
    """

    if mask:  # not empty mask
        for i in itertools.permutations(words, int(n_words)):
            count = sum(mask[j] in [i[j], '_'] for j in range(len(i)))

            if count == len(mask):
                print(''.join(i))

    else:  # mask is not empty
        for permutation in itertools.permutations(words, int(n_words)):
            print(''.join(permutation))


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    # Add your arguments here
    parser.add_argument(
        '-w', '--words', type=str, dest='words', required=True, default='AEIOU')
    parser.add_argument(
        "-n", "--number", dest="number", required=False, default=5)
    parser.add_argument(
        '-m', '--mask', type=str, dest='mask', required=False, default='')

    args = parser.parse_args()
    find_words(args.number, args.words, args.mask)
