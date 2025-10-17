def two_sum(nums, target):
    assert isinstance(nums, list), "nums must be a list"
    assert all(isinstance(x, int) for x in nums), "all elements of nums must be integers"
    assert isinstance(target, int), "target must be an integer"

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []