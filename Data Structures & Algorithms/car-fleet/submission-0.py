class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse = True)

        for pos, s in cars:
            currTime = (target - pos) / s

            if stack and not(currTime > stack[-1]):
                continue
            else:
                stack.append(currTime)
        return len(stack)

                
                
        
        