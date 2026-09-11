# LeetCode 163 - Missing Ranges

## Problem

Given a sorted integer array `nums` where the elements are unique, and two integers `lower` and `upper`, return the smallest sorted list of ranges that contains all the numbers missing from the range `[lower, upper]`.

A single missing number should be represented as:

```text
"number"
```

A range of multiple missing numbers should be represented as:

```text
"start->end"
```

---

## Example

**Input:**

```text
nums = [0,1,3,50,75]
lower = 0
upper = 99
```

**Output:**

```text
["2","4->49","51->74","76->99"]
```

**Explanation:**

The numbers missing from the range `0` to `99` are:

* `2`
* `4` through `49`
* `51` through `74`
* `76` through `99`

---

## Approach

The main idea is to check the gap between consecutive numbers.

Instead of checking every number individually, keep track of the previous number and compare it with the current number.

We start with:

```text
prev = lower - 1
```

This allows us to check whether there are missing numbers before the first element.

We also add:

```text
upper + 1
```

at the end of the array.

This helps us check whether any numbers are missing between the last element and `upper`.

---

## How It Works

For every current number:

```text
num
```

we calculate:

```text
num - prev
```

### No missing number

If:

```text
num - prev == 1
```

the numbers are consecutive, so there is no missing range.

### One missing number

If:

```text
num - prev == 2
```

exactly one number is missing.

For example:

```text
prev = 3
num = 5
```

The missing number is:

```text
4
```

So we add:

```text
"4"
```

### Multiple missing numbers

If:

```text
num - prev > 2
```

more than one number is missing.

For example:

```text
prev = 3
num = 8
```

The missing numbers are:

```text
4,5,6,7
```

So we add:

```text
"4->7"
```

---

## Algorithm

1. Create an empty result list.
2. Set `prev = lower - 1`.
3. Add `upper + 1` after the last element of `nums`.
4. Traverse through the numbers.
5. Calculate the gap between `prev` and the current number.
6. If the gap is `2`, add one missing number.
7. If the gap is greater than `2`, add a missing range.
8. Update `prev`.
9. Return the result.

---

## Example Walkthrough

For:

```text
nums = [0,1,3,50,75]
lower = 0
upper = 99
```

We begin with:

```text
prev = -1
```

Compare with `0`:

```text
0 - (-1) = 1
```

No missing number.

Compare `1` with `0`:

```text
1 - 0 = 1
```

No missing number.

Compare `3` with `1`:

```text
3 - 1 = 2
```

One number is missing:

```text
2
```

Compare `50` with `3`:

```text
50 - 3 = 47
```

The missing range is:

```text
4->49
```

Compare `75` with `50`:

```text
75 - 50 = 25
```

The missing range is:

```text
51->74
```

Finally, compare `upper + 1 = 100` with `75`:

```text
100 - 75 = 25
```

The missing range is:

```text
76->99
```

Final result:

```text
["2","4->49","51->74","76->99"]
```

---

## Time Complexity

**O(n)**

The array is traversed once.

---

## Space Complexity

**O(k)**

Where `k` is the number of missing ranges stored in the result.

Apart from the output, the algorithm uses **O(1)** extra working space.

---

## Key Concepts

* Arrays
* Two-pointer style traversal
* Sorted arrays
* Range detection
* Gap calculation
* Boundary handling

---

## Important Edge Cases

### No numbers

```text
nums = []
lower = 1
upper = 5
```

Output:

```text
["1->5"]
```

### One missing number

```text
nums = [1,3]
lower = 1
upper = 3
```

Output:

```text
["2"]
```

### No missing numbers

```text
nums = [1,2,3,4,5]
lower = 1
upper = 5
```

Output:

```text
[]
```

### Missing range at the beginning

```text
nums = [3,4,5]
lower = 1
upper = 5
```

Output:

```text
["1->2"]
```

### Missing range at the end

```text
nums = [1,2,3]
lower = 1
upper = 5
```

Output:

```text
["4->5"]
```

---

## What I Learned

This problem helped me understand how to find missing values efficiently in a sorted array.

Instead of checking every number between `lower` and `upper`, I can compare consecutive elements and identify the gaps directly.

The use of `lower - 1` and `upper + 1` also makes it easier to handle missing ranges at the beginning and end of the array.

---

## LeetCode Details

* **Problem Number:** 163
* **Problem Name:** Missing Ranges
* **Difficulty:** Medium
* **Topics:** Array
* **Language:** Python

---

## Author

T.Nandhini
