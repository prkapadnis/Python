class Range:
    def __init__(self, start, end, index= 1):
        self.value = start
        self.end = end
        self.index = index
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += self.index
        return current

nums = Range(1, 10, 2)
for num in nums:
    print(num)
