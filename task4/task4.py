name_file = input("Введите имя файла: ")

file = open(name_file)
nums = []
for i in file:
    nums.append(int(i))
file.close()

nums.sort()

length = len(nums)
centre = nums[length // 2]

step = 0

for num in nums:
    step = step + abs(num - centre)

print("Минимальное количество ходов:", step)