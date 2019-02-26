#!/usr/bin/env python3
import numpy as np

def toss(n):
    # 1 - H, 0 - T
    total = dict()
    # results = np.random.choice([0, 1], size=(n, 2), p=(0.3, 0.7))
    results = np.random.choice([0, ] * 3 + [ 1, ] * 7, size=(n, 2))

    total['H'] = np.sum(results)
    total['T'] = (2 * n) - np.sum(results)

    # print(results)

    keep = (results[:, 0] ^ results[:, 1]) > 0
    balanced = results[keep]
    # print(balanced)

    balanced_count = np.sum(balanced, axis=0)
    # print(balanced_count)

    del balanced
    del keep
    del results
    total['HT'] = balanced_count[0]
    total['TH'] = balanced_count[1]
    return total


def toss1W(w):
    total = dict(T=0, H=0, TH=0, HT=0)
    for _ in range(w):
        subtotal = toss(10000)
        for k, v in subtotal.items():
            total[k] += v
    return total


if __name__ == '__main__':
    from pprint import pprint
    #total = toss(1000 * 10000)
    total = toss1W(10000)
    pprint(total)
    print('3 : 7 = %.4f : 1' % (3.0 / 7,))
    print('T : H = %.4f : 1' % (total['T'] / total['H'], ))
    print('T-H : H-T = %.2f : 1' % (total['TH'] / total['HT'], ))

