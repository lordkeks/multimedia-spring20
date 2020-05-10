from math import log2
from functools import reduce


class txt:
    def __init__(self, path: str):
        self.__data: list = self.__load_txt(path)

    def __len__(self) -> int:
        return len(self.__data)

    @staticmethod
    def __load_txt(path: str) -> list:
        buf: list = []
        with open(path) as f:
            buf = list(map(lambda c: c, f.read()))
        return buf

    def count_char_occurrences(self) -> (dict, dict):
        keys: set = set(self.__data)
        d1: dict = {}
        d2: dict = {}
        for k in keys:
            d1[k] = self.__data.count(k)
            d2[k] = self.__data.count(k) / len(self)
        d1 = dict(sorted(d1.items(), key=lambda x: x[1], reverse=True))
        d2 = dict(sorted(d2.items(), key=lambda x: x[1], reverse=True))
        return d1, d2


def huffman(p: dict, inverted=False) -> (dict, float, float):
    temp: dict = p
    code: dict = dict(map(lambda k: (k, ''), temp))

    # assemble huffman tree and generate code
    tree = ()
    while len(p) > 1:
        p = {k: v for k, v in sorted(p.items(), key=lambda item: item[1])}

        def get_min_val_item(d: dict) -> (int, str):
            return min(d, key=lambda x: d[x]), d[min(d, key=lambda x: d[x])]

        left = get_min_val_item(p)
        p.pop(left[0])
        right = get_min_val_item(p)
        p.pop(right[0])
        p[left[0] + right[0]] = left[1] + right[1]
        tree = (tree, (left[0], right[0]))
        for k in temp:
            if k in left[0]:
                if not inverted:
                    code[k] += '0'
                else:
                    code[k] += '1'
            if k in right[0]:
                if not inverted:
                    code[k] += '1'
                else:
                    code[k] += '0'

    # compute the entropy & the mean length
    entropy: float = reduce(lambda x, y: x + y, map(lambda x: (-1) * log2(temp[x]) * temp[x], temp))
    mean_length: float = reduce(lambda x, y: x + y, map(lambda x: len(code[x]) * temp[x], temp))
    return code, entropy, mean_length


def main() -> None:
    print("Test:")
    list(map(print, huffman({"A": 0.05, "B": 0.03, "C": 0.17, "D": 0.23, "E": 0.01, "F": 0.32, "G": 0.19})))
    print("Midsummer:")
    buf: txt = txt("midsummer.txt")
    print(len(buf))
    d1, d2 = buf.count_char_occurrences()
    print(d1)
    print(d2)
    list(map(print, huffman(d2)))
    return


if __name__ == "__main__":
    main()
