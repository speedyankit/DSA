Day 5: Sliding Window (Variable Size) 🚀
📌 Topic

Variable Size Sliding Window — a dynamic technique where the window grows and shrinks like a caterpillar to satisfy a specific condition. Unlike fixed windows, the size k is not given; instead, we often look for the "longest" or "smallest" subarray that meets a criteria.

This topic introduces two distinct approaches based on the input data:

    Standard Expansion/Shrinking: Best for arrays with positive numbers only.

    Prefix Sum (Hash Map): Required when arrays contain negative numbers.

🛠️ Core Concepts

    The Caterpillar Method (Expand & Shrink):

        Expand: Move right pointer to include elements until the condition breaks.

        Shrink: Move left pointer to restore the condition.

    Prefix Sum Logic:

        Using the math property CurrentSum - Target = PreviousSum to find subarrays in O(N) time when simple sliding fails (due to negative numbers).

    Zero-Based Indexing: Careful handling of array indices when calculating length (right - left + 1).

🧪 Practice Problems
1️⃣ Subarray with Given Sum (Non-negative)

    Goal: Find the starting and ending indices of a contiguous subarray that adds up to a specific sum S (assuming non-negative numbers).

    Key Idea:

        Use two pointers (left, right).

        Add elements at right to current_sum.

        While current_sum > S, subtract arr[left] and move left forward.

        If current_sum == S, return the indices.

  📎 Problem Link: https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

2️⃣ Longest Sub-Array with Sum K (Handles Negatives)

    Goal: Find the length of the longest subarray with a sum equal to K. This array contains negative numbers, so the standard sliding window approach will fail.

    Key Idea:

        Use a Hash Map to store the first occurrence of every Prefix Sum.

        Calculate Rem = CurrentSum - K.

        If Rem exists in the map, the subarray between the old index and the current index has sum K.

        Update MaxLen accordingly.

  📎 Problem Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

