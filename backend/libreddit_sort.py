# Rewritten code from /r2/r2/lib/db/_sorts.pyx

from datetime import datetime
from math import log, sqrt

epoch = datetime(1970, 1, 1)


def epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


def score(ups, downs):
    return ups - downs


def hot_old(up, total, date):
    s = total - (total - up)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)


def hot_score(up, total, datesec):
    s = total - (total - up)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = datesec - 1134028003
    return round(sign * order + seconds / 45000, 7)


def best_score(up, total):
    if total == 0:
        return 0

    z = 1.96
    phat = up / total

    a = phat + z * z / (2 * total)
    s = (phat * (1 - phat) + z * z / (4 * total)) / total
    b = z * sqrt(s)
    c = 1 + z * z / total

    result = (a - b) / c
    return result


# if __name__ == '__main__':
#    now = datetime.now()
#    print(hot(123, 6, now))
#    print(epoch_seconds(now))
#    print(now.timestamp())
