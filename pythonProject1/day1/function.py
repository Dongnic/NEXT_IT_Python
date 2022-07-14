import random
def fn_name(param):
    """
    10을 곱하는 함수
    :param param: anything
    :return: *10
    """
    return param * 10

print(fn_name('h1'))

def fn_name2(param):
    nm = param.split()
    return nm[0], nm[1]

first, last = fn_name2('함 수')
print('1', first,'2', last)

def fn_total(*num):
    tot = 0
    for n in num:
        tot += n
    return tot
print(fn_total(1,2,3))
print(fn_total(1))
print(fn_total(1,2,3,4,5,6,7,8,9,10))

def fn_sum_mul(flag, *args):
    if flag == 'sum':
        result= 0
        for i in args:
            result = result + i
    elif flag == 'mul':
        result= 1
        for i in args:
            result = result * i
    return result
print(fn_sum_mul('sum',1,2,3,4,5))
print(fn_sum_mul('mul',1,2,3,4,5))

# 로또 생성기를 함수로 만들어보기

def fn_lotto(param):
    result = []
    for i in range(param):
        lotto = set()
        while len(lotto) < 6:
            lotto.add(format(random.randint(1, 45), '02'))
        lotto = list(lotto)
        lotto.sort()
        result.append(lotto)
    return result
a = int(input("숫자를 입력해주세요 : "))
print(a)
b = fn_lotto(a)
print("로또번호 생성기",a,"개 생성")
for i in b:
    print(i)