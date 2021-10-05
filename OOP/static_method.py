"""
    Static method:
        The static method is much like class method, are methods that bound with the class
        rather than it's objects
        - The difference between static method and class method
            - The static knows nothing about the class It just work on it's parameter.
            - The class method works with the class since it's parameter is always the class
              itself.
            -  We can call the static method without creating the object of a class.
"""
class Date:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def format(date):           # This is a static method 
        return date.replace("-", "/")   
    
    def getDate(self):
        return self.date

currentDate = Date("15-05-2021")
print(currentDate.format(currentDate.getDate()))