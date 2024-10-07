# [Two Sum](https://leetcode.com/problems/two-sum/) ➕

## Problem Description 📖

You are given an array of integers and a target, and are required to find two integers from the array that sum up to the target and return their indicies.

## Inputs 📥

1. Integer array
2. Target

## Output 📤

1. Array with two indicies of the integers that sum up to the target

## Approach 💡

1. **Step-by-step explanation 🧠**

   We will iterate through the array and store each number in a hashmap in the form:
   | Key | Value |
   | ----------- | ----------- |
   | Value1 | Index1 |
   | Value2 | Index2 |

   and for each iteration we will check if we passed an integer which matches the integer of the current iteration using the expression `if target - nums[i] in mymap`, and if we passed it, we return the index of the integer of the current iteration, and the index of the matching number in the map using `mymap[target - nums[i]]`. Otherwise, we keep iterating and store each value-index pair. If we didn't find a valid pair, then we return [-1,-1](but since we are guaranteed a pair we don't need to).

2. **Time Complexity ⏳** `O(n)`
3. **Space Complexity 🚀** `O(n)`

## Solution Code 🧩

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i in range(len(nums)):
            if target - nums[i] in mymap:
                return [i, mymap[target - nums[i]]]
            mymap[nums[i]] = i

        return [-1,-1]
```

---

Whenever you are bored, check out my [LinkedIn profile](https://www.linkedin.com/in/tawfic-kobtan/), [my LeetCode profile](https://leetcode.com/u/tofuegy/), or my [GitHub profile](https://github.com/tawfickobtan), I would appreciate that alot.

Other than that, Enjoy. 😁
