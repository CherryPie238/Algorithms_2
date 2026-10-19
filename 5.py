def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

#свдигаем указатель правый, если сумма слишком большая и левый - если слишком маленькая
#в итоге проходим один раз по массиву максимум