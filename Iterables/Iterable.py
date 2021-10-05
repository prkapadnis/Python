"""
    Iterable : Iterable are objects that are capable of returning their member one at a time
                means in short anything we can liip over is an iterable.
    
    Iterator : Iterable are objects which are representing the stream of data that is iterable.
                iterator creates something iterator pool which allows us to loop over an item in
                iterable using thetwo methods that is __iter__() and __next__().
                __iter__(): The __iter__() method returns the iterator of an iterable.
                __next__():The __next__() method returns the next element of an iterator
    Key points:
        - The difference between Iterable and Iterator is that the __next__() method is only 
         accessible to the Iterator. The Iterable only have __iter__() method.
        - Iterator also have __iter__() method because iterators are also iterables but not vice
          versa.

"""
sample = [1, 2, 3]
it = iter(sample)
print(next(it))
print(next(it))
print(next(it))
# If overshoot the limit the number of times we call  the next() method. then an exception
# is occur which is called StopIteration Exception.
# print(next(it))