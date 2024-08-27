#로또 추첨
from random import randint

def lotto():
    lotto = []

    while len(lotto) < 6:
        lotto_input = randint(1, 45)
        if lotto_input not in lotto:
            lotto.append(lotto_input)

    lotto.sort()
    print(lotto)

lotto()