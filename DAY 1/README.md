Day 1: Time & Space Complexity (The Interview Language) 🚀
📌 Topic

Time & Space Complexity (Big O Notation) — The language of performance. In a MAANG interview, solving the problem is only half the battle. You must be able to explain why your solution is efficient and compare it to other approaches (e.g., "I optimized this from O(N2) to O(N)").
🛠️ Core Concepts

    Big O Notation (O): Describes the Worst-Case scenario (Upper Bound). It tells us how the execution time grows as the input size (N) increases.

    Common Complexities (Best to Worst):

        O(1) - Constant (Direct access, e.g., Hash Map lookup).

        O(logN) - Logarithmic (Binary Search).

        O(N) - Linear (Simple loop).

        O(NlogN) - Linearithmic (Sorting like Merge Sort).

        O(N2) - Quadratic (Nested loops).

    Space Complexity: How much extra memory (RAM) your algorithm needs (Auxiliary Space).

        Creating a new array of size N = O(N) space.

        Using variables (sum, count) = O(1) space.

🧪 Practice Problems
1️⃣ Analysis of Algorithms (Theory)

    Goal: Understand how to calculate complexity by looking at code structure (loops, recursion).

    Key Takeaway:

        Single Loop = O(N)

        Nested Loop = O(N2)

        Halving the input (loop i = i * 2) = O(logN)

    📎 Resource Link: Analysis of Algorithms | GeeksforGeeks

2️⃣ Missing Number in Array

    Goal: Given an array of size N−1 containing distinct integers in the range of 1 to N, find the missing element.

    Key Idea (Optimization):

        Brute Force: Sort (O(NlogN)) or check every number (O(N2)). Too slow.

        Math Approach: Use the Sum Formula.
        Sum=2N×(N+1)​
        Missing=Sum(Expected)−Sum(Actual)

        XOR Approach: XOR all numbers from 1 to N, then XOR with array elements. The result is the missing number.

  📎 Problem Link: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
