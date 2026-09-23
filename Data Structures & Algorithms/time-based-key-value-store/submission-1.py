from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        array = self.hash_map[key]
        
        if not array:
            return ""
        
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = left + ((right - left)//2)
            if array[middle][1] == timestamp:
                return array[middle][0]

            if array[middle][1] < timestamp:
                left = middle + 1

            else:
                right = middle - 1
        # nothing was found of that timestamp
        if timestamp > array[right][1]:
            return array[right][0]
        else:
            return ""
