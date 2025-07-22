def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {}  # {val -> index}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

print(twoSum([15, 11, 7, 2], 9)) 