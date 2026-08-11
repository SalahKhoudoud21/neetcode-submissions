class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = []
        result = []
        for pos, speed in zip(position, speed):
            stack.append((pos,speed))
        
        stack.sort(key=lambda tup: tup[0])
        for pos, speed in stack:
            fleet.append((target - pos)/speed)

        for time in fleet:
            while result and time >= result[-1]:
                result.pop()
            result.append(time)
        return len(result)
