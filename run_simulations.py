import os
import multiprocessing

def exec_martingale():
    for sb in xrange(5, 55, 5):
        for a in xrange(100, 2001, 100):
            for g in xrange(25, 201, 25):
                os.system("python roulette.py -s martingale -sb {} -a {} -g {} -n 1000 >/dev/null 2>&1".format(sb, a, g))

def exec_fibonacci():
    sb =1
    for a in xrange(100, 2001, 100):
        for g in xrange(25, 201, 25):
            os.system("python roulette.py -s fibonacci -sb {} -a {} -g {} -n 1000 >/dev/null 2>&1".format(sb, a, g))

def exec_paroli():
    for ws in xrange(2, 5, 1):
        for sb in xrange(5, 55, 5):
            for a in xrange(100, 2001, 100):
                for g in xrange(25, 201, 25):
                    os.system("python roulette.py -s paroli -ws {} -sb {} -a {} -g {} -n 1000 >/dev/null 2>&1".format(ws, sb, a, g))

def exec_alembert():
    for sb in xrange(1, 6, 1):
        for a in xrange(100, 2001, 100):
            for g in xrange(25, 201, 25):
                os.system("python roulette.py -s alembert -sb {} -a {} -g {} -n 1000 >/dev/null 2>&1".format(sb, a, g))


if __name__ == "__main__":
    m = multiprocessing.Process(target=exec_martingale)
    m.start()

    '''f = multiprocessing.Process(target=exec_fibonacci)
    f.start()

    p = multiprocessing.Process(target=exec_paroli)
    p.start()

    a = multiprocessing.Process(target=exec_alembert)
    a.start()'''

