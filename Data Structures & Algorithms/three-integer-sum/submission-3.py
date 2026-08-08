class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summa = -(
                nums[left] + nums[right]
                )  # since num1 + num2 + num3 = 0 => num3 = -(num1 + num2)
                if nums[i] < summa:
                    left += 1
                elif nums[i] > summa:
                    right -= 1
                else:
                    lista = [nums[i], nums[left], nums[right]]
                    if lista not in results:
                        results.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
        return results
            
            
