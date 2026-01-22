# DSA
This repository contains my DSA journey starting Jan 17, 2026 — daily notes and Python solutions for common interview problems (Day 1 → Day 6).

## Overview
A concise summary of Days 1 through 6 with links to each day's folder, key problems, and sample solution files included in the repo.

## Days 1 — 6

### Day 1 — Time & Space Complexity
- Topic: Big O notation and common time/space complexities (O(1), O(log N), O(N), O(N log N), O(N^2)).
- Key problem: Missing Number in an array (math/XOR approaches).
- Files: `DAY 1/missing_in_array.py`
- Resource: [Missing Number in Array (GeeksforGeeks)](https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1)
- Folder: [DAY 1](https://github.com/speedyankit/DSA/tree/e2cc4c8a58f0da38429439e65fee43a5586dc96c/DAY%201)

### Day 2 — Array Rotations & Moving Zeros
- Topics: Rotating arrays (slicing/circular behavior), moving zeros to the end in-place.
- Key problems: Rotate array by N elements; Move zeros to end.
- Files: `DAY 2/rotate_array.py`, `DAY 2/move_zeros_to_end.py`
- Resource: [Rotate Array by N Elements (GeeksforGeeks)](https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1)
- Folder: [DAY 2](https://github.com/speedyankit/DSA/tree/e2cc4c8a58f0da38429439e65fee43a5586dc96c/DAY%202)

### Day 3 — Two Pointer Technique
- Topic: Two-pointer strategies (left/right), in-place manipulation, and pointer adjustments for sorted arrays.
- Key problems: Key Pair (Two Sum using two pointers), Dutch National Flag (sort 0s, 1s, 2s).
- Files: `DAY 3/README.md`, `DAY 3/Sort 0s, 1s and 2s.py`
- Resources:
  - [Key Pair / Two Sum (GeeksforGeeks)](https://www.geeksforgeeks.org/problems/key-pair5616/1)
  - [Sort 0s,1s,2s (Dutch National Flag)](https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1)
- Folder: [DAY 3](https://github.com/speedyankit/DSA/tree/e2cc4c8a58f0da38429439e65fee43a5586dc96c/DAY%203)

### Day 4 — (See folder)
- Summary: Day 4 folder contains that day's problems and solutions — check `DAY 4` for specifics and code.
- Folder: [DAY 4](https://github.com/speedyankit/DSA/tree/e2cc4c8a58f0da38429439e65fee43a5586dc96c/DAY%204)

### Day 5 — Subarray Sums
- Topic: Subarray problems and cumulative-sum / prefix-sum approaches.
- Key problem: Longest subarray with sum K.
- Files: `DAY 5/README.md`
- Resource: [Longest Subarray with Sum K (GeeksforGeeks)](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)
- Folder: [DAY 5](https://github.com/speedyankit/DSA/tree/e2cc4c8a58f0da38429439e65fee43a5586dc96c/DAY%205)

### Day 6 — Kadane's Algorithm & Maximum Product Subarray
- Topics:
  - Kadane's Algorithm — max contiguous subarray sum in O(N).
  - Maximum Product Subarray — track both current max and current min products to handle negatives.
- Files: `DAY 6/README.md`, `DAY 6/kadane's algorithm.py`, `DAY 6/Maximum_Product_Subarray.py`
- Resources:
  - [Kadane's Algorithm (GeeksforGeeks)](https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1)
  - [Maximum Product Subarray (GeeksforGeeks)](https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1)
- Folder: [DAY 6](https://github.com/speedyankit/DSA/tree/e2cc4c8a58f0da38429439e65fee43a5586dc96c/DAY%206)

## How to run
- Each solution is a small Python class with a function that can be called directly.
- Example (local):
```python
from DAY_6.Maximum_Product_Subarray import Solution
res = Solution().maxProduct([2,3,-2,4])
print(res)
```
(Adjust import paths to match your local environment or run the .py files directly.)

## Contributing
- Add more problems, improved explanations, or optimized variants.
- Follow naming: `DAY <n>/` for notes and `<problem>.py` for solutions.
- Open a PR or create an issue if you want me to add tests, examples, or CI.

---

If you want, I can:
- Provide a minimal test harness for each day, or
- Create the commit and push this README update for you (I cannot push from here unless you instruct me to proceed).
