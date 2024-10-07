# [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) 🧑🧑

## Problem Description 📖

You are given an array of integers and are required to return a boolean value, whether or not the array contains a duplicate.

## Inputs 📥

1. Integer array

## Output 📤

1. Whether or not the array contains a duplicate

## Approach 💡

1. **Step-by-step explanation 🧠**

We will iterate through the array and will keep track of what numbers we passed so far (using a set). Each iteration we will check if the number of the current iteration is in the set. If it is, then there is a duplicate in the array, thus we return true. If we reached the end of the array without finding a duplicate, then the array doesn't contain a duplicate, thus we return false.

2. **Time Complexity ⏳** `O(n)`
3. **Space Complexity 🚀** `O(n)`

## Solution Code 🧩

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ymset = set()
        for i in nums:
            if i in ymset:
                return True
            ymset.add(i)
        return False
```

---

Whenever you are bored, check out my [LinkedIn profile](https://www.linkedin.com/in/tawfic-kobtan/), [my LeetCode profile](https://leetcode.com/u/tofuegy/), or my [GitHub profile](https://github.com/tawfickobtan), I would appreciate that alot.

Other than that, Enjoy. 😁
