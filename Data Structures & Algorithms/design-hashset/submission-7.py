class MyHashSet:

    def __init__(self):
        self.hashset = [False] * 1000000

    def add(self, key: int) -> None:
        index = key % 1000000 
        self.hashset[index] = key

    def remove(self, key: int) -> None:
        index = key % 1000000
        self.hashset[index] = False

    def contains(self, key: int) -> bool:
        return self.hashset[key % 1000000] is not False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)