from time import sleep
import time
import sys

def ft_progress(lst):
    # i have to do it like this to find the max cause the prototype doesn't allow me other variables
    listprogress = list(lst)
    max = int(listprogress[-1]) + 1
    t0 = time.time()
    for i in lst:
        percent = i / max * 100
        donebar = round(10 * (percent/100))
        notdonebar = 10 - donebar - 1
        t1 = time.time()
        estimatedtime = (t1 - t0) * max/(i+1) - (t1 - t0)
        print('\r' + f'ETA: {estimatedtime:4.2f}s [{percent:3.0f}%][{"=":=<{donebar}}{">" if donebar != 10 else ""}{"":<{notdonebar if notdonebar > 0 else 0}}] {i+1:<4}/{max}'
        f' | elasped time {t1 - t0:.2f}s', end = '')
        yield i

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print("\n...")
print(ret)
