class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drankBottles = 0
        emptyBottles = 0
        fullBottles = numBottles
        currentExchange = numExchange 

        while True: 
            drankBottles += fullBottles
            emptyBottles += fullBottles
            fullBottles = 0

            if emptyBottles >= currentExchange: 
                while emptyBottles >= currentExchange:
                    emptyBottles -= currentExchange 
                    fullBottles += 1
                    currentExchange += 1


            else:
                return drankBottles
