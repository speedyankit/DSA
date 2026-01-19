# Day 3: Two Pointer Technique 🚀

## 📌 Topic
**Two Pointer Technique** — a powerful method to process arrays (or strings) using two indices moving from different directions or at different speeds.

This technique helps optimize solutions from **O(n²)** to **O(n)** in many array problems and is **crucial for interviews**.

---

## 🛠️ Core Concepts
- Left & Right pointers
- Pointer movement based on conditions
- In-place array manipulation
- Sorting using pointers (without extra space)

---

## 🧪 Practice Problems

### 1️⃣ Key Pair (Two Sum)
**Goal:**  
Check whether there exists a pair of elements in the array whose sum equals a given target.

**Key Idea:**  
- Sort the array
- Use two pointers (`left`, `right`)
- Adjust pointers based on current sum

📎 Problem Link:  
https://www.geeksforgeeks.org/problems/key-pair5616/1

---

### 2️⃣ Sort an Array of 0s, 1s and 2s  
*(Dutch National Flag Algorithm)*

**Goal:**  
Sort the array containing only `0`, `1`, and `2` in **O(n)** time and **O(1)** space.

**Key Idea:**  
- Use three pointers: `low`, `mid`, `high`
- Place 0s to the left, 2s to the right, and 1s in the middle

📎 Problem Link:  
https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

## ⏱️ Time & Space Complexity
| Problem | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| Key Pair | O(n log n) | O(1) |
| Dutch National Flag | O(n) | O(1) |
