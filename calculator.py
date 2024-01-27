def add(nums):
  sum = 0
  for i in nums:
    sum += i
  return sum

def subt(nums):
  diff = nums[0]
  for i in range(1, len(nums)):
    diff = diff - nums[i]
  return diff

def mult(nums):
  prod = 1
  for i in nums:
    prod *= i
  return prod

def div(nums):
  ans = nums[0]
  for i in range(0, len(nums) - 1):
    ans = ans / nums[i+1]
  return ans

def calc(operation, numbers):
  match operation:
    case 'add':
      return add(numbers)
    case 'subtract':
      return subt(numbers)
    case 'multiply':
      return mult(numbers)
    case 'divide':
      return div(numbers)
    case _:
      return "Enter add, subtract, multiply or divide only"
