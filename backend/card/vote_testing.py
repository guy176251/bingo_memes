def modulo(up: int, down: int, incoming: int):
    adj = 1 if incoming else -1
    # result = 2 * -adj * up + 2 * -adj * down + adj
    result = adj + (up * adj + up)  # + (down * adj - down)
    print(result)
    return result


def if_cancelled(up, down, incoming):
    return int((not up and incoming) or (not down and not incoming))


def if_truthy(up, down, incoming):
    return int(incoming)


def if_downvoted(up, down, incoming):
    return int(not down and not incoming)


def if_other_shit(up, down, incoming):
    return int(not up and incoming)


"""

assert modulo(up=0, down=0, incoming=0) == -1  # downvote
assert modulo(up=1, down=0, incoming=0) == -1  # up negation
assert modulo(up=0, down=0, incoming=1) == 1  # upvote
assert modulo(up=0, down=1, incoming=1) == 1  # down negation
assert modulo(up=0, down=1, incoming=0) == 0  # double down
assert modulo(up=1, down=0, incoming=1) == 0  # double up
"""

"""
break down into 2 functions to have bool states instead of 3 states
"""

"(not up and incoming) or (not down and not incoming)"
assert if_cancelled(0, 0, 0) == 1  # downvote
assert if_cancelled(0, 0, 1) == 1  # upvote
assert if_cancelled(0, 1, 0) == 0  # double down
assert if_cancelled(0, 1, 1) == 1  # down negation
assert if_cancelled(1, 0, 0) == 1  # up negation
assert if_cancelled(1, 0, 1) == 0  # double up

"(incoming)"
assert if_truthy(0, 0, 0) == 0  # downvote
assert if_truthy(0, 0, 1) == 1  # upvote
assert if_truthy(0, 1, 1) == 1  # down negation
assert if_truthy(1, 0, 0) == 0  # up negation

"(not down and not incoming)"
assert if_downvoted(0, 0, 0) == 1  # downvote
assert if_downvoted(0, 0, 1) == 0  # upvote
assert if_downvoted(0, 1, 0) == 0  # double down
assert if_downvoted(0, 1, 1) == 0  # down negation
assert if_downvoted(1, 0, 0) == 1  # up negation
assert if_downvoted(1, 0, 1) == 0  # double up

"(not up and incoming)"
assert if_other_shit(0, 0, 1) == 1  # upvote
assert if_other_shit(0, 1, 1) == 1  # down negation
assert if_other_shit(0, 1, 0) == 0  # double down
assert if_other_shit(1, 0, 1) == 0  # double up
