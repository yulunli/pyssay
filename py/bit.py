'''
Implement binary indexed trees (Fenwick trees)
'''

import random

class BIT:
    def __init__(self):
        self.bit = [0]
        self.backup = [0]

    def size(self):
        return len(self.bit) - 1

    def get_sum(self, i):
        if i >= self.size():
            raise ValueError('index {} exceeds tree size {}'.format(i, self.size))
        res = 0
        i += 1
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def update(self, i, delta):
        if i > self.size():
            raise ValueError('index {} exceeds tree size {}'.format(i, self.size))
        i += 1
        if i == self.size() + 1:
            self.backup.append(delta)
            i_parent = i - (i & -i)
            # compare node (i-1) and node's parent. If node is first child of parent, delta is the val in BIT
            self.bit[-1] += self.get_sum(i-2) - self.get_sum(i_parent - 1) + delta
            return
        self.backup[i] += delta
        while i <= self.size():
            self.bit[i] += delta
            i += i & -i

if __name__ == '__main__':
    bit = BIT()
    for _ in range(300):
        bit.update(random.randint(0, bit.size()), random.randint(-10, 10))
        for i in range(bit.size()):
            assert sum(bit.backup[:i+2]) == bit.get_sum(i)
    print('all tests pass')
