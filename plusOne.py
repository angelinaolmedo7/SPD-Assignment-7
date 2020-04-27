def plusOne(digits):
    """
    Given a non-empty array meant to represent an integer (ex. [2,0,1] == 201),
    return the array + 1.
    """
    i = len(digits) - 1
    while i >= 0:
        digits[i] += 1
        if digits[i] >= 10:
            digits[i] = 0
        else:
            return digits
        i -= 1
    digits.insert(0, 1)
    return digits


print(plusOne([1, 2, 3]))  # [1, 2, 4]
print(plusOne([1, 2, 9]))  # [1, 3, 0]
print(plusOne([1, 2, 9, 9]))  # [1, 3, 0, 0]
print(plusOne([1]))  # [2]
print(plusOne([9]))  # [1, 0]
