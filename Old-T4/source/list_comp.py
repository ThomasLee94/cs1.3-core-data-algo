nums = [number for number in range(100)]
nums2 = (number for number in range(100))

nums = list()
for number in range(100):
  nums.append(number)

for num in nums:
  print(num)

for num in nums2:
  print(num)

print(nums)
print(nums2)

def numsfn():
  lst = []
  for i in range(100):
    lst.append(i)
  return lst

def numsGen():
  for i in range(100):
    yield i

generator = range(100)

print(generator)
print(next(generator))
print(next(generator))