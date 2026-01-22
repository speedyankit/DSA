Day 6: Kadane’s Algorithm (Must Know) 🚀
📌 Topic

Kadane’s Algorithm — an optimized Dynamic Programming approach used to find the maximum sum of a contiguous subarray in O(N) time.

The brute force approach checks every possible subarray (O(N2)), but Kadane’s algorithm does it in a single pass by deciding at each step: "Should I start a new subarray here, or extend the existing one?"
🛠️ Core Concepts

    Carry vs. Restart: As you iterate, you keep adding numbers to a current_sum.

    The "Baggage" Check: If current_sum becomes negative, it is "bad baggage" (it will only decrease the sum of any future subarray). So, you throw it away and reset current_sum to 0.

    Global Maximum: You constantly update a max_so_far variable to record the highest sum encountered.

    Handling Products: For the "Maximum Product" variation, negative numbers are useful (because negative * negative = positive), so we must track both the maximum AND minimum product.

🧪 Practice Problems
1️⃣ Kadane's Algorithm (Max Subarray Sum)

    Goal: Find the contiguous subarray with the largest sum.

    Key Idea:

        Iterate through the array adding to current_sum.

        Update max_sum if current_sum is higher.

        Crucial Step: If current_sum drops below 0, reset it to 0 (start fresh).

        Edge Case: If all numbers are negative, return the single largest element (don't return 0).

  📎 Problem Link: https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

2️⃣ Maximum Product Subarray

    Goal: Find the contiguous subarray with the largest product.

    Key Idea:

        A negative number can turn a small product into a huge positive one (e.g., −10×−10=100).

        Therefore, maintain two running variables: current_max and current_min.

        Swap: When you see a negative number, swap current_max and current_min before multiplying.

  📎 Problem Link: https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1
