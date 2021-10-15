# -*- coding: utf8


from collections import Counter # RECOMENDADO!


def conta_um_arquivo(fpath):
    with open(fpath) as input_file:
        l = []
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split()
                l += palavras
        counter_dict = Counter(l)
        return counter_dict


def reduz(contagens_1, contagens_2):
    dict1 = contagens_1 + contagens_2
    reduce_dict = Counter(dict1)
    return reduce_dict
