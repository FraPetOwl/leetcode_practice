#[][][][]Sliding Window[][][][] - quite hard compared to twoSum
# doesnt have self as not in a Class here

def threeSum(nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = v + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([v, nums[left], nums[right]])
                    #[-2, -2, 0, 0, 2, 2]
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result

print(threeSum([-1,0,1,2,-1,-4]))
