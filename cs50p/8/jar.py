class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        new_size = self._size + n
        if new_size > self._capacity:
            raise ValueError
        else:
            self._size = new_size

    def withdraw(self, n):
        new_size = self._size - n
        if new_size < 0:
            raise ValueError
        else:
            self._size = new_size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
