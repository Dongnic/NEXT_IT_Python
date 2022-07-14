f = open('delay.txt', 'a')
f.write('오늘 지각자 \n')
while 1:
    n = input("오늘 지각한 사람(종료: q) ")
    if 'q' == n:
        break
    f.write(n)
    f.writelines('\n')
f.close()