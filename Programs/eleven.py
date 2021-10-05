"""
    Can plant flower:
        You have a long flowered in which some of the plots are planted nad some are not 
        flowers cannot be planted in adjacent plots
        Give an intger array flowerbed contaning 0's and 1's where 0 means empty and 1 means
        not empty and an integer n, return if n new flowers can be planted in the flowerbed 
        whothout violeting the non-adjancent flowers rule
"""
def can_plant_flower(flowerbed, n):
    i, count = 0, 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and ((i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) -1 or flowerbed[i+1] == 0)):
            count += 1
        i =+ 1
    return count >= i


flowerbed = [1,0,0,0,1]
print(can_plant_flower(flowerbed, 1))