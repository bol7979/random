import random

lotto = []

while len(lotto) < 6:
    lotto_input = random.randint(1, 45)
    if lotto_input not in lotto:
        lotto.append(lotto_input)

lotto.sort()
print(lotto)