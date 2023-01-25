class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack
        # pos1  < pos2 speed1 > speed2
        # car1 = 2 car2 = 3 pos2 > pos1
        0    
        1   
        # stack[1,7,12]
        cars = [] * len(position)
        for i , j in enumerate(position):
            cars.append((j,speed[i]))
        cars.sort(reverse = True) # olog(n)
        stack = []
        for i in cars:
            stack.append((target - i[0])/i[1])
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
