import random
from functools import partial

class JEH:
    HIRAGANA_SET = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
    KANJI_SET = ""
    ALL_KANAS_SET = "".join([HIRAGANA_SET, KANJI_SET])
    STR_LENGTH = 5
    STR_NUMBER = 5
    KATAKANA_TRANSFORM_PROPABILITY = 0.65
    RAMANZI_DICT = {
        ###########　romanzi #########
        "あ" : "a", "か" : "ka", "さ" : "sa", "た" : "ta", "な" : "na", "は" : "ha", "ま" : "ma", "や" : "ya", "ら" : "ra", "わ" : "wa", "ん" : "n",
        "い" : "i", "き" : "ki", "し" : "si", "ち" : "ti", "に" : "ni", "ひ" : "hi", "み" : "mi",              "り" : "ri",
        "う" : "u", "く" : "ku", "す" : "su", "つ" : "tu", "ぬ" : "nu", "ふ" : "hu", "む" : "mu", "ゆ" : "yu", "る" : "ru",
        "え" : "e", "け" : "ke", "せ" : "se", "て" : "te", "ね" : "ne", "へ" : "he", "め" : "me",              "れ" : "re",
        "お" : "o", "こ" : "ko", "そ" : "so", "と" : "to", "の" : "no", "ほ" : "ho", "も" : "mo", "よ" : "yo", "ろ" : "ro", "を" : "wo",
    }
    KATAKANA_DICT = {
        ########### katakana #########
        "あ" : "ア", "か" : "カ", "さ" : "サ", "た" : "タ", "な" : "ナ", "は" : "ハ", "ま" : "マ", "や" : "ヤ", "ら" : "ラ",  "わ" : "ワ",  "ん" : "ン",
        "い" : "イ", "き" : "キ", "し" : "シ", "ち" : "チ", "に" : "ニ", "ひ" : "ヒ", "み" : "ミ",              "り" : "リ",
        "う" : "ウ", "く" : "ク", "す" : "ス", "つ" : "ツ", "ぬ" : "ヌ", "ふ" : "フ", "む" : "ム", "ゆ" : "ユ", "る" : "ル",
        "え" : "エ", "け" : "ケ", "せ" : "セ", "て" : "テ", "ね" : "ネ", "へ" : "ヘ", "め" : "メ",              "れ" : "レ",
        "お" : "オ", "こ" : "コ", "そ" : "ソ", "と" : "ト", "の" : "ノ", "ほ" : "ホ", "も" : "モ", "よ" : "ヨ", "ろ" : "ロ",  "を" : "ヲ",
    }


    @staticmethod
    def ramanzi_transform(string):
        resString = list(string)
        for i, c in enumerate(string):
            if c in JEH.RAMANZI_DICT:
                resString[i] = JEH.RAMANZI_DICT[c]
        return ''.join(resString)

    @staticmethod
    def generate_random_permutation(string):
        nextShufle = list(range(len(string)))
        random.shuffle(nextShufle)
        nextShufle = nextShufle[:JEH.STR_LENGTH]
        res = [ str(string[i]) for i in nextShufle ]
        res = "".join(res)
        return res

    @staticmethod
    def generate_permutations(string):
        genNext = partial(JEH.generate_random_permutation, string)
        perm_set = set([ genNext() for i in range(JEH.STR_NUMBER)])
        perm_list = [''.join(perm) for perm in perm_set]
        return perm_list

    @staticmethod
    def randomKatakanaFromHiragana(stringData):
        kanas = list(stringData)
        resString = []
        for k in kanas:
            if random.random() < JEH.KATAKANA_TRANSFORM_PROPABILITY:
                if k in JEH.KATAKANA_DICT:
                    k = JEH.KATAKANA_DICT[k]
            resString.append(k)
        return ''.join(resString)

    @staticmethod
    def printPermuntations(stringData):
        permutations_list = JEH.generate_permutations(stringData)
        random.shuffle(permutations_list)
        for i, perm in enumerate(permutations_list):
            perm = JEH.randomKatakanaFromHiragana(perm)
            print(f"{i+1}: {perm}")

    @staticmethod
    def EDU_HiraganaByHeart():
        # Цель: напечатать тоже самое в блокноте.
        JEH.printPermuntations(JEH.ALL_KANAS_SET)

    @staticmethod
    def EDU_romanziToHiragana():
        # Цель: записать в тетради в хирагане/катакане.
        permutations_list = JEH.generate_permutations(JEH.ALL_KANAS_SET)
        for i, perm in enumerate(permutations_list):
            perm = JEH.ramanzi_transform(perm)
            print(f"{i+1}: {perm}")