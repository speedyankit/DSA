Day 4: Sliding Window (Fixed Size) 🚀
📌 Topic

Fixed Size Sliding Window — an optimization technique used to process sequential data (arrays or strings) by maintaining a subset of elements of a specific length k. This technique converts nested loops (Brute Force) into a single loop, effectively reducing time complexity from O(n*k) to O(n).
🛠️ Core Concepts

    The Window: A range of elements defined by start and end indices.

    The Slide: Moving the window one step right by adding the new element and removing the old one.

    Constant Time Updates: Updating the result (sum, count, etc.) in O(1) instead of recalculating the whole window.

    Deque Utility: Using a Double Ended Queue for advanced constraints (like finding specific elements in a window).

🧪 Practice Problems
1️⃣ Max Sum Subarray of size K

    Goal: Find the maximum sum of any contiguous subarray of size K.

    Key Idea:

        Calculate the sum of the first K elements.

        Slide the window: Add the next element (arr[i]) and subtract the element leaving the window (arr[i-k]).

        Update the maximum sum at each step.

  📎 Problem Link: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

2️⃣ First negative integer in every window of size k

    Goal: Find the first negative integer for each window of size K. If a window has no negative number, output 0.

    Key Idea:

        Use a Deque to store indices of negative numbers.

        Remove Old: If the index at the front of the Deque is out of the current window, pop it.

        Add New: If the current element is negative, add its index to the back.

        Pick Result: The front of the Deque always holds the first negative number.

  📎 Problem Link: https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
