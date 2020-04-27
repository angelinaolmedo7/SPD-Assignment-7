def singleNumber(nums):
    """
    In a list where every number but one is repeated three times, return the
    solitary number.
    """
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for val in counts:
        if counts[val] == 1:
            return val
    return None


print(singleNumber([2, 2, 3, 2]))  # 3
print(singleNumber([0, 1, 0, 1, 0, 1, 99]))  # 99
