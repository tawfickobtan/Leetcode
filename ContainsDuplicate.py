class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

## Explanation:
## Since a hashset can only contain unique values,
## when converting the array nums into a hashet,
## any duplicates will be discarded,
## which decreases the length of the hashset.
## If the array had any duplicates,
## the set will discard the duplicates
## and will have a shorter length
## so the function will return true.
## Otherwise, the function will return false.