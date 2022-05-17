import itertools
from argparse import ArgumentParser
from time import perf_counter

# all the combinations of number_of_words words from the words list


def find_words(
    n_words=5, words="AEIOU", mask="", permutations=True, combinations=False
):
    """
    Encontra todas as combinações de n_words palavras de words
    com a máscara mask

    Args:
    - n_words: número de palavras a serem usadas (default: 5)
    - words: lista de palavras (string)
    - mask: máscara para preencher as palavras (ex: 'S_L')
    """

    if permutations is False and combinations is False:
        permutations = True

    list_of_words = []
    if mask:  # mask not empty
        if permutations and not combinations:
            for i in itertools.permutations(words, int(n_words)):
                count = sum(mask[j] in [i[j], "_"] for j in range(len(i)))

                if count == len(mask):
                    list_of_words.append("".join(i))

        if combinations and not permutations:
            for i in itertools.combinations(words, int(n_words)):
                count = sum(mask[j] in [i[j], "_"] for j in range(len(i)))

                if count == len(mask):
                    list_of_words.append("".join(i))

    else:  # mask is empty
        list_of_words.extend(
            "".join(permutation)
            for permutation in itertools.permutations(words, int(n_words))
        )

    return list(dict.fromkeys(list_of_words))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)

    parser.add_argument("-w", "--words", type=str, dest="words", required=True)
    parser.add_argument("-n", "--number", dest="number", required=False, default=5)
    parser.add_argument(
        "-m", "--mask", type=str, dest="mask", required=False, default=""
    )

    # choose between permutation and combination
    parser.add_argument("-p", "--permutation", dest="permutation", action="store_true")
    parser.add_argument("-c", "--combination", dest="combination", action="store_true")

    args = parser.parse_args()
    print(
        " ".join(
            find_words(
                args.number, args.words, args.mask, args.permutation, args.combination
            )
        )
    )
