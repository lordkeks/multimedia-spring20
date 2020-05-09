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


def main() -> None:
    buf: txt = txt("midsummer.txt")
    print(len(buf))
    d1, d2 = buf.count_char_occurrences()
    print(d1)
    print(d2)
    return


if __name__ == "__main__":
    main()
