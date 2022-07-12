def find_duplicate(nums):
    for number in nums:
        if not type(number) == int or not number >= 1:
            return False
        elif nums.count(number) > 1:
            return number

    return False
