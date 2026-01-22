Topic: Sliding Window – Variable Size

  This technique is used when the window size is not fixed and depends on a condition (sum, length, count, etc.).

  Unlike fixed-size sliding window, here we expand and shrink the window dynamically.

🧠 Core Idea

We maintain:

  A left pointer (start)

  A right pointer (end)

  A running state (sum / count / condition)

We:

Expand the window by moving end
Shrink the window by moving start when the condition breaks
Track the best answer (length / count / etc.)

📌 Questions Covered
1️⃣ Longest Subarray with Sum K

🔗 Problem: Find the longest subarray whose sum equals K.

⚠️ Important Note:

If the array contains negative numbers, normal sliding window fails.

We must use Prefix Sum + HashMap.

2️⃣ Subarray with Given Sum

🔗 Problem: Check if there exists a subarray with a given sum K.

Approach depends on:

Only positive numbers → Sliding Window

Negative numbers present → Prefix Sum + HashMap

🧰 What You Need to Know Before Solving These
✅ 1. Prefix Sum Concept

Understand how cumulative sums work:

prefix[i] = sum of elements from index 0 to i


This helps in quickly finding subarray sums.

✅ 2. HashMap (Dictionary)

Used to:

Store prefix sums

Track first occurrence of a sum

Check if (current_sum - K) exists

This is mandatory when negatives are involved.

✅ 3. Difference Between Fixed & Variable Window
Fixed Window	Variable Window
Window size constant	Window size changes
Easy logic	Requires condition handling
Mostly positives	Negatives need hashmap
✅ 4. When Sliding Window FAILS

Sliding Window does NOT work when:

Array contains negative numbers

Sum can decrease even after expanding window

👉 Use Prefix Sum + HashMap instead.
