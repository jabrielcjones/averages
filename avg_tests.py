#!/usr/bin/env python

import avg

SAMPLE_NUMS = [1, 2, 3, 4, 5]

COUNT = 5

SUM = 15


class TestGenerateNums:

    def test_size_and_type(self):
        '''
        list has one or more numbers

        all numbers are integers
        '''

        nums = avg.generate_nums()

        if len(nums) <= 0:
            print('num list is empty')
            assert False

        for num in nums:
            if type(num) != int:
                print(f'{num} is not an integer')
                print(f'num list: {nums}')
                assert False

        assert True


class TestCalculateSum:

    def test_sum(self):
        '''
        sum of numbers should be correct
        '''

        assert sum(SAMPLE_NUMS) == avg.calculate_sum(SAMPLE_NUMS)


class TestGetCount:

    def test_count(self):
        '''
        count of numbers should be correct
        '''

        assert len(SAMPLE_NUMS) == avg.get_count(SAMPLE_NUMS)


class TestCalculateAvg:

    def test_avg(self):
        '''
        avg of numbers should be correct
        '''

        assert SUM / COUNT == avg.calculate_avg(SUM, COUNT)
