class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get("ignore_case", False)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            key = item.casefold() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item
        raise StopIteration


if __name__ == "__main__":
    print("Числа:", list(Unique([1, 1, 2, 2, 3, 1])))
    print("Генератор:", list(Unique(number for number in [2, 2, 1, 3, 1])))
    letters = ["a", "A", "b", "B", "a"]
    print("С учетом регистра:", list(Unique(letters)))
    print("Без учета регистра:", list(Unique(letters, ignore_case=True)))
