class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Must be non negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceeds capacity")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Exceeds amount")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Must be non-negative")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Exceeds capacity")
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
