#! /usr/bin/env python

def bubble_sort():
    nums = [2,3,7,5,1,4,9,7,8]
    print(nums)

    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print(nums)


if __name__ == "__main__":
    bubble_sort()
