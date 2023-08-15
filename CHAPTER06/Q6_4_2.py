import math


def gen_prime1(x=2):
    while True:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                break
        else:
            yield x
        x += 1


i = gen_prime()
for c in range(10):
    print(next(i), end=" ")
print("")

% % time
# (1)愚直な方法
i = gen_prime(100000)
for c in range(10):
    print(next(i), end=" ")
print("")


% % time
# (2)sqrt(x)以下だけ調べる方法
i = gen_prime1(100000)
for c in range(10):
    print(next(i), end=" ")
print("")
