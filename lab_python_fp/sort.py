data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]


if __name__ == "__main__":
    print("Без lambda:", sorted(data, key=abs, reverse=True))
    print("С lambda:", sorted(data, key=lambda number: abs(number), reverse=True))
