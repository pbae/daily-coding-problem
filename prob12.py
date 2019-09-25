# There exists a staircase with N steps, and you can climb up either 1 or 2
# steps at a time. Given N, write a function that returns the number of unique
# ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
#    1, 1, 1, 1
#    2, 1, 1
#    1, 2, 1
#    1, 1, 2
#    2, 2
#
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if X = {1,
# 3, 5}, you could climb 1, 3, or 5 steps at a time.

def ways_up_stairs(num_steps, step_sizes):
    ways = [0] * (num_steps+1)
    ways[-1] = 1
    for step in range(num_steps, 0, -1):
        for delta in step_sizes:
            if step - delta >= 0:
                ways[step - delta] += ways[step]
    return ways[0]

assert 1 == ways_up_stairs(4, [1])
assert 1 == ways_up_stairs(4, [2])
assert 0 == ways_up_stairs(4, [3])
assert 5 == ways_up_stairs(4, [1,2])
assert 47 == ways_up_stairs(10, [1,3,5])
