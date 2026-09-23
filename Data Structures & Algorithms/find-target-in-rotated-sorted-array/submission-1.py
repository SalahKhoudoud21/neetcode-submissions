class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mini = 0
        while left <= right:
            middle = left + (right - left)//2
            if target == nums[middle]:
                    return middle
            
            if nums[left] <= nums[right]:
                if target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target == nums[left]:
                        return left
                
                if nums[middle] >= nums[left]:
                    if target > nums[middle] or target < nums[left]:
                        left = middle + 1
                    else:
                        right = middle - 1
                else:
                    if nums[middle] < target:
                        if nums[left] < target:
                            right = middle - 1
                        else:
                            left = middle + 1
                    else:
                        right = middle - 1
        return -1 

                    
                
        # 1, 2, 3, 4, 5, 6 left < right and k > mid look right of mid
        # 6, 1, 2, 3, 4, 5 left > right and k > mid look right of mid
        # 5, 6, 1, 2, 3, 4 left > right and k > mid look right of mid
        # 4, 5, 6, 1, 2, 3 left > right and k < mid look left of mid
        # 3, 4, 5, 6, 1, 2 left > right and k < mid look left of mid
        # 2, 3, 4, 5, 6, 1 left > right and k == mid done

        k = 2
        # 1, 2, 3, 4, 5, 6 left < right and k < mid look left of mid
        # 6, 1, 2, 3, 4, 5 left > right and k == done
        # 5, 6, 1, 2, 3, 4 left > right and k > mid look right of mid
        # 4, 5, 6, 1, 2, 3 left > right and k < mid look right of mid, k < right
        # 3, 4, 5, 6, 1, 2 left > right and k < mid look left of mid
        # 2, 3, 4, 5, 6, 1 left > right and k == mid done

