"""
    static_method:
        - We can call the static method without creating the object of a class. 
"""
class Sum:
    @staticmethod
    def get_sum(*args):
        total = 0
        for i in args:
            total += i
        return total
    
print(f"The sum is {Sum.get_sum(1, 2, 3, 4, 5)}") # Here we have not created a object of a class