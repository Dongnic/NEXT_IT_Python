import random
inputnum = int(input("숫자를 입력해주세요 : "))
print("===============로또 번호 생성기 "+inputnum+"개=============")
for i in range(inputnum) :
    lotto = set()
    while len(lotto) <= 5 :
        lotto.add(random.randint(1,45))
    lotto = list(lotto)
    lotto.sort()
    print(lotto)
print("===============로또 번호 생성기=============")
