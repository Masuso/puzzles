# Puzzle:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 6456 ms, 14.9 mb, o(n^2)
    # brute force, basic attempt
    for i in range(len(nums)):
        sum1 = target - nums[i]
        for j in range(i, len(nums)):
            sum0 = sum1 - nums[j]
            if sum0 == 0 and i != j:
                return [i, j]

def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
    # 81 ms, 15.1, o(n)
    # very happy with this attempt, no trouble implementing after getting the hint to use hashmap
    checked = {}
    for i in range(len(nums)):
        sum1 = target - nums[i]
        if sum1 in checked:
            return [i, checked[sum1]]
        checked[nums[i]] = i

# Puzzle:
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific target number.

def twoSum_sorted(self, numbers: List[int], target: int) -> List[int]:
    # 243 ms, 14.9 mb, o(n)
    # got an error for using two if loops instead of if and elif
    l, r = 0, len(numbers) - 1
    while l < r:
        current_sum = numbers[l] + numbers[r]
        if current_sum < target:
            l += 1
        elif current_sum > target:
            r -= 1
        else:
            return [l + 1, r + 1]

# Puzzle:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

def threeSum(self, nums: List[int]) -> List[List[int]]:
    # 18.2 mb, O(nlogn) + O(n^2) = O(n^2)
    # lots of trouble getting this one to work. I got reminded of how to use continue
    # important to remember to increment the pointers when we find a set so as not get duplicates.
    sets = []
    nums.sort()
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threesum = nums[i] + nums[l] + nums[r]
            if threesum < 0:
                l += 1
            elif threesum > 0:
                r -= 1
            else:
                sets.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return sets