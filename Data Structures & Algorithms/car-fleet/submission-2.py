class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        times = []
        fleet = []
        for pos, speed in zip(position, speed):
            pos_speed.append((pos,speed))
        
        pos_speed.sort(key=lambda tup: tup[0]) # sort based on position
        for pos, speed in pos_speed:
            times.append((target - pos)/speed)

        for time in times:
            while fleet and time >= fleet[-1]:
                fleet.pop()
            fleet.append(time)
        return len(fleet)
