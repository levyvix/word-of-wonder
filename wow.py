import itertools
from argparse import ArgumentParser

# all the combinations of number_of_words words from the words list


def find_words(n_words=5, words='AEIOU', mask = ""):
    """
    Encontra todas as combinações de n_words palavras de words
    com a máscara mask

    Args:
    - n_words: número de palavras a serem usadas (default: 5)
    - words: lista de palavras (string)
    - mask: máscara para preencher as palavras (ex: 'S_L')
    """

    list_of_words = []
    if mask:  # mask not empty

        for i in itertools.combinations(words, int(n_words)):
            count = sum(mask[j] in [i[j], '_'] for j in range(len(i)))

            if count == len(mask):
                # print(''.join(i))
                list_of_words.append(''.join(i))

    else:  # mask is empty
        list_of_words.extend(''.join(permutation) for permutation in itertools.combinations(words, int(n_words)))

    return list(dict.fromkeys(list_of_words))


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)

    parser.add_argument(
        '-w', '--words', type=str, dest='words', required=True)
    parser.add_argument(
        "-n", "--number", dest="number", required=False, default=5)
    parser.add_argument(
        '-m', '--mask', type=str, dest='mask', required=False, default='')

    args = parser.parse_args()
    print(' '.join(find_words(args.number, args.words, args.mask)))
