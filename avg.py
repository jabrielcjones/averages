#!/usr/bin/env python

import random
import requests


'''
Generate a list a numbers

Print the average

1. High-level solution/algo

2. Single Responsibility Principle - Modularity
'''


def generate_nums():
    '''
    Generate a list of integers

    * Random module
    * Random.org (external API)
    '''

    url = 'https://www.random.org/integers/?num=10&min=1&max=100&col=1&base=10&format=plain&rnd=new'

    try:
        response = requests.get(url)

    except Exception as err:
        print(f'Error: {err}')
        exit()

    nums = [int(num) for num in response.text.strip('\n').split('\n')]

    # nums = []

    # size = random.randint(1, 10)
    # print(f'List Size: {size}')

    # for i in range(size):
    #     nums.append(random.randint(1, 100))

    # print(f'List: {nums}')
    return nums


def calculate_sum(nums):
    '''
    Calculate the sum of a list of integers
    '''

    sum = 0

    for num in nums:
        sum += num

    return sum


def get_count(nums):
    '''
    Count a list of nums
    '''

    count = 0

    for num in nums:
        count += 1

    return count


def calculate_avg(sum, count):
    '''
    Calculate the average
    '''

    return round(sum / count, 3)


if __name__ == '__main__':

    # Read a list of numbers
    nums = generate_nums()

    # Compute average
    sum = calculate_sum(nums)

    count = get_count(nums)

    avg = calculate_avg(sum, count)

    # Print average
    print(nums)
    print(avg)
