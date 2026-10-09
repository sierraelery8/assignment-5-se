# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3


def most_frequent(numbers):
    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    most_common = None
    highest_count = 0

    for number, count in counts.items():
        if count > highest_count:
            most_common = number
            highest_count = count

    return most_common


# Tests for Problem 1
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5, 5, 5, 2, 2]) == 5
assert most_frequent([7]) == 7
assert most_frequent([1, 2, 1, 2]) in [1, 2]
assert most_frequent([]) is None

print("Problem 1 tests passed!")


"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because the function has to go through the numbers to count them and find which one appears the most.
- Worst-case: O(n), because it goes through the list to count the numbers and then checks the counts to find the most frequent one.
- Average-case: O(n), because the function uses two passes to get the counts and find the highest one.
- Space complexity: O(n), because the dictionary may need to store every number if they are all different.
- Why this approach? I used a dictionary to keep track of how many times each number appears.
This makes it easier to compare the counts without having to count the same numbers over and over.
- Could it be optimized? This approach is already efficient because it runs in O(n) time.
It does use extra memory for the dictionary, but that helps the function find the answer faster.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    unique_nums = []
    seen = set()

    for num in nums:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)

    return unique_nums


# Tests for Problem 2
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []
assert remove_duplicates([8]) == [8]

print("Problem 2 tests passed!")


"""
Time and Space Analysis for problem 2:
- Best-case: O(n), because the function still needs to check each number in the list, even if there are no duplicates.
- Worst-case: O(n), because it checks each number once, and using a set makes it quick to tell if a number has already appeared.
- Average-case: O(n), because checking the set and adding numbers to it usually take constant time for each number.
- Space complexity: O(n), because the set and the new list may need to store all the numbers if there are no duplicates.
- Why this approach? I used a set to keep track of numbers I've already seen and a list to save the numbers in their original order.
This removes duplicates without changing the order.
- Could it be optimized? This approach is already efficient because it runs in O(n) time.
The set uses extra memory, but it helps avoid checking the list repeatedly.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    seen = set()

    for num in nums:
        needed = target - num

        if needed in seen:
            pairs.append((needed, num))

        seen.add(num)

    return pairs


# Tests for Problem 3
assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
assert find_pairs([1, 2, 3], 10) == []
assert find_pairs([1, 2, 3, 4], 7) == [(3, 4)]
assert find_pairs([] , 5) == []
assert find_pairs([2, 4, 6], 8) == [(2, 6)]

print("Problem 3 tests passed!")


"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because the function still needs to check each number in the list to see if it has a matching pair.
- Worst-case: O(n), because it goes through the list once and uses a set to quickly check whether the number it needs has already appeared.
- Average-case: O(n), because checking the set and adding numbers to it usually take constant time for each number.
- Space complexity: O(n), because the set can store the numbers we've checked, and the pairs list may also grow as matching pairs are found.
- Why this approach? I used a set to keep track of numbers I've already checked. This makes it easier
to find matching pairs without comparing every number with every other number.
- Could it be optimized? This approach is already efficient because it runs in O(n) time on average. It also
avoids creating a separate list of every possible pair, which would take more time and memory.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.


def add_n_items(n):
    capacity = 2
    items = []
    resize_count = 0

    for i in range(n):
        if len(items) == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")

            new_items = [None] * new_capacity

            for j in range(len(items)):
                new_items[j] = items[j]

            items = new_items[:len(items)]
            capacity = new_capacity
            resize_count += 1

        items.append(i)

    print(f"Final number of items: {len(items)}")
    print(f"Final capacity: {capacity}")
    print(f"Number of resizes: {resize_count}")

    return items



# Tests for Problem 4
assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(2) == [0, 1]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

print("Problem 4 tests passed!")


"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizing happens whenever the number of items reaches the current capacity.
The capacity starts at 2 and doubles each time, so it grows from 2 to 4, then 8, and so on.
- What is the worst-case for a single append? A single append can take O(n) time when the list needs to resize
because the existing items have to be copied into a bigger list.
- What is the amortized time per append overall? O(1) amortized, because the list doubles its capacity when it fills up.
Although resizing takes extra time, it doesn't happen on every append.
- Space complexity: O(n), because the list needs enough space to hold all the items, and resizing temporarily requires extra space for the new list.
- Why does doubling reduce the cost overall? Doubling gives the list more room to grow before it needs to resize again.
This means copying happens less often, making the average cost per append much lower.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]


def running_total(nums):
    totals = []
    current_sum = 0

    for num in nums:
        current_sum += num
        totals.append(current_sum)

    return totals


# Tests for Problem 5
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([5, -2, 3]) == [5, 3, 6]
assert running_total([]) == []
assert running_total([7]) == [7]
assert running_total([0, 0, 0]) == [0, 0, 0]

print("Problem 5 tests passed!")


"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because the function needs to go through each number in the list to calculate the running totals.
- Worst-case: O(n), because it processes every number once, no matter what values are in the list.
- Average-case: O(n), because the function does the same amount of work for each number.
- Space complexity: O(n), because it creates a new list to store the running totals.
- Why this approach? I used a running sum to keep track of the total as I go through the list
This way, I don't have to add up all the previous numbers again each time.
- Could it be optimized? The function already runs in O(n) time because it only goes through the list once.
Since the assignment requires returning a new list of totals, the extra space is necessary for the result.
"""


# Optimization Comparison - Problem 2
#
# An unoptimized approach could check whether each number is
# already in the result list. Since list membership checks can
# take O(n) time, the overall time complexity could be O(n^2).
#
# My optimized approach uses a set to track numbers already seen.
# Set lookups take O(1) time on average, so the overall time
# complexity improves to O(n).
#
# Space comparison:
# Both approaches use O(n) extra space in the worst case.
# The optimized approach uses a set in addition to the result
# list, but it avoids repeatedly searching through the result list.