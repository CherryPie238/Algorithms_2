def remove_duplicates(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

#slow указывает на последний уникальный элемент, а fast находит следующий. просто сдвигаем массив,
#заменяя дубликаты на следующий уникальный жлемент, не выделяя больше памяти