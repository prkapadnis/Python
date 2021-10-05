class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        ind = self.index
        self.index += 1
        return self.words[ind]


# my_sentence = Sentence("Pratik Rajendra Kapadnis")
# # words = my_sentence.split()
# for word in my_sentence:
#     print(word)

# Generator
def Sentence(sentence):
    for word in sentence.split():
        yield word

my_sentence = Sentence("Pratik Rajendra Kapadnis")
# for value in my_sentence:
#     print(value)
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
# print(next(my_sentence))