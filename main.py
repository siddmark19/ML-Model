def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)

    return False

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(containsDuplicate(nums))