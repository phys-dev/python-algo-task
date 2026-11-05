class HashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(8)]
        self.size = 0

    def _bucket(self, key):
        return self.buckets[hash(key) % len(self.buckets)]

    def _grow(self):
        old = self.buckets
        self.buckets = [[] for _ in range(2 * len(old))]
        for bucket in old:
            for key, value in bucket:
                self._bucket(key).append((key, value))

    def __setitem__(self, key, value):
        bucket = self._bucket(key)
        for i, (other, _) in enumerate(bucket):
            if other == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size > len(self.buckets):
            self._grow()

    def __getitem__(self, key):
        for other, value in self._bucket(key):
            if other == key:
                return value
        raise KeyError(key)

    def __contains__(self, key):
        return any(other == key for other, _ in self._bucket(key))

    def __iter__(self):
        for bucket in self.buckets:
            for key, _ in bucket:
                yield key

    def __len__(self):
        return self.size


class HashSet:
    def __init__(self, values=()):
        self.table = HashMap()
        for value in values:
            self.add(value)

    def add(self, value):
        self.table[value] = True

    def __contains__(self, value):
        return value in self.table

    def __iter__(self):
        return iter(self.table)

    def __len__(self):
        return len(self.table)
