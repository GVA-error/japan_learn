
from enum import Enum

from moduls.JEH import JEH
from moduls.youTubeDownloader import DOWNLOAD_FROM_YOUTUBE
from moduls.KARDS import showMeKards
from moduls.youDownloadTubeList import DOWNLOAD_LIST

class EDU(Enum):
    HIRAGANA_BY_HEART        = 0, # вывод рядов канн
    ROMANZY_GENERATE         = 1, # генерация рядов романдзи
    KANGI_SENTENCE_CARDS     = 20,# по канджи нужно узнать чтение и перевод
    KANA_SENTENCE_CARDS      = 21,# по чтению нужно узнать канджи и перевод
    TRANSLATE_SENTENCE_CARDS = 22,# по переводу нужно узнать канджи и чтение
    VIDEO_DOWNLOAD           = 3, # загрузка материалов с youtube

kangiTopBound = None # По умолчанию None. Верхняя граница номеров ключей для генерации карточек.
PATH_TO_STUDIED_KEYS = "studied.words"

# Какой EDU режим использовать.
CUR_REGIM = EDU.KANGI_SENTENCE_CARDS

# Какую тему я решаю сегодня по проге
import random
from datetime import datetime
random.seed(datetime.now().timestamp())

print(random.choice(["Array / String","Two Pointers","Sliding Window","Matrix","Hashmap","Intervals","Stack", \
                     "Linked List","Binary Tree General","Binary Tree BFS", "Binary Search Tree" ,"Graph General", \
                     "Graph BFS","Trie","Backtracking", "Divide & Conquer", "Kadane's Algorithm", "Binary Search", \
                     "Heap","Bit Manipulation","Math","1D DP","Multidimensional DP"]))

if CUR_REGIM == EDU.HIRAGANA_BY_HEART:
    JEH.EDU_HiraganaByHeart()
if CUR_REGIM == EDU.ROMANZY_GENERATE:
    JEH.EDU_romanziToHiragana()
if CUR_REGIM == EDU.VIDEO_DOWNLOAD:
    DOWNLOAD_FROM_YOUTUBE(DOWNLOAD_LIST)
if CUR_REGIM == EDU.KANGI_SENTENCE_CARDS:
    showMeKards(0, kangiTopBound, PATH_TO_STUDIED_KEYS)
if CUR_REGIM == EDU.KANA_SENTENCE_CARDS:
    showMeKards(1, kangiTopBound, PATH_TO_STUDIED_KEYS)
if CUR_REGIM == EDU.TRANSLATE_SENTENCE_CARDS:
    showMeKards(2, kangiTopBound, PATH_TO_STUDIED_KEYS)