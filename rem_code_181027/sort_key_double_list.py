# -*- coding:utf-8 -*-
__date__ = '2018/3/26 17:21'

import functools


def init_cmp(arg, reverses = None):
    if isinstance(arg, int):
        positions = range(arg)
    elif isinstance(arg, (tuple, list)):
        positions = arg
    else:
        raise ValueError("First argument must be integer or list")

    reverses = reverses or [False]*len(positions)
    if len(positions) != len(reverses):
        raise ValueError("reverses length must fit the first argument")
    reverses = list(map(lambda x: 1 if x is False else -1, reverses))
    def my_cmp(x, y):
        for ipos, idatapos in enumerate(positions):
            if x[idatapos] > y[idatapos]:
                return reverses[ipos]           #降序
            elif  x[idatapos] < y[idatapos]:
                return -reverses[ipos]
            else:
                pass
        return 0
    return my_cmp

def cmp_temp_list(templist):
    # 生成比较后的list
    new_templist = sorted(templist, key=functools.cmp_to_key(init_cmp([0,1,2],
                                                 [False, False, False])))
    print("templist:",templist)
    print("new_templist:",new_templist)

test_list =  [
                [2,2,3],
                [2,1,4],
                [2,2,1],
                [1,2,1]
            ]

cmp_temp_list(test_list)

        # *        *
# [[2, 2, 3], [2, 1, 4], [2, 2, 1], [1, 2, 1]]    key:[2, 2, 3]
#      *                     *
# [[2, 1, 4], [2, 2, 3], [2, 2, 1], [1, 2, 1]]      key:[2, 1, 4]  过
#                 *          *
# [[2, 1, 4], [2, 2, 3], [2, 2, 1], [1, 2, 1]]      key:[2, 2, 3]
#                 *          *
# [[2, 1, 4], [2, 2, 1], [2, 2, 3],  [1, 2, 1]]      key:[2, 2, 1]
