#!/usr/bin/env python3
import random


candidates = 'T' * 3 + 'H' * 7

def toss(n):
    total = {
        'H': 0,
        'T': 0,
        'HT': 0,
        'TH': 0,
    }
    for _ in range(n):
        # c1, c2 = random.choices('TH', weights=(3, 7), k=2)
        c1, c2 = random.choices(candidates, k=2)
        total[c1] += 1
        total[c2] += 1
        if c1 != c2:
            total[c1 + c2] += 1
    return total


if __name__ == '__main__':
    import pprint
    total = toss(1000 * 10000)
    pprint.pprint(total)
    print('3 : 7 = %.4f : 1' % (3.0 / 7,))
    print('T : H = %.4f : 1' % (total['T'] / total['H'], ))
    print('T-H : H-T = %.2f : 1' % (total['TH'] / total['HT'], ))
