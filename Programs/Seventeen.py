"""
    kids with greatest number of candies
"""

def kidsWithCandies(candies, extraCandies):
    def checkCandies(candy):
        candy+=extraCandies
        if candy >= max(candies):
            return True
        return False

    candies = list(map(checkCandies, candies))
    return candies

candies = [4,2,1,1,2]
extraCandies = 1
candies = kidsWithCandies(candies, extraCandies)
print(candies)