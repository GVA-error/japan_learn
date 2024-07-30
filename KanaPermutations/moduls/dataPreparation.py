from .kangi_words import KANGI_SET
from functools import partial


def get_allKeys():
    return list(KANGI_SET.keys())


def get_ansAsKanas(key):
    kn, kg, tr = get3Text(key)
    return get3DataFormat(kn, kg, tr)


def get_ansAsKangi(key):
    kn, kg, tr = get3Text(key)
    return get3DataFormat(kg, kn, tr)


def get_ansAsTranslate(key):
    kn, kg, tr = get3Text(key)
    return get3DataFormat(tr, kg, kn)

def get3DataFormat(q1, q2, q3):
    return f"{q1}", f"{q2} | {q3}"

def get3Text(key):
    get_kangi = partial(__getKangi, KANGI_SET)
    get_kanas = partial(__getKanas, KANGI_SET)
    get_trans = partial(__getTranslate, KANGI_SET)
    return get_kanas(key), get_kangi(key), get_trans(key)


def __getKanas(dataSet, key):
    return dataSet[key][0]


def __getKangi(dataSet, key):
    return key


def __getTranslate(dataSet, key):
    return dataSet[key][1]

