def two_sum(nums, target):
    seen = {}
    result = []
    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            result.append( [seen[need], i])

        seen[num] = i
    return result

num2 = [2, 7, 10, 11]
print(two_sum(num2, 9))