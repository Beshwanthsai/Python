from itertools import count

nums = [12,25,37,49,58,69,72,84,1,100]
print(nums)

print(type(nums))

print(len(nums))

print(nums[0])

print(nums[-1])

print(nums[-2])

print(nums[-5]) #print from the end

print(nums[2:8]) #print from index 2 to index 7
print(nums[5:]) #prints from index 5 to end
print(nums[:4]) #prints from start to index 3

print(nums[::3]) #print every third element
print(nums[::-1]) #prints the list in reverse order

print(nums[:]) #print the whole list
print(nums[1:10:2]) #print from index 1 to index 8 with a step of 2

# modifications of list

nums[0]=  99
print(nums)

nums[-1]=  101
print(nums)
print(nums[::-1])
nums[2:5] = [33,44,55]
print(nums)

nums[3:6] = []
print(nums)
values = [2.4,'Beshwanth Sai Katari',True]
print(values)
print(type(values))

mix = [nums, values]
print(mix)
print(mix[0])

nums.append(5656)
print(nums)
nums.append(7777)
print(nums)
nums.insert(2,888)
print(nums)
nums.remove(888)
print(nums)
nums.pop()
print(nums)
nums.pop(0)


print(nums.index(5656))

print(nums.count(84))
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums2 = nums.copy()
print(nums2)
nums.clear()
print(nums)
print(nums2)

print(min(nums2))
print(max(nums2))
print(sum(nums2))
print(nums2)
print (nums2)

animals = ["rabbit", "cat", "dog", "hamster", "parrot"]
print(animals.pop(3))
print(animals.append("bear"))
print(animals.pop(0))
print(animals)
print(animals[0:3])