# -*- coding:utf-8 -*-
__date__ = '2018/10/21 13:01'


class Company(object):
    def __init__(self, em_list):
        self.em_list = em_list

    def __getitem__(self, item):
        return self.em_list[item]



company = Company(["tom", "bob", "jane"])

# for em in company:
#     print(em)


a = ["a"]

a.extend(company)
print(a)

print(company[:2])


class A:
    pass

class B(A):
    pass

b=B()
print(isinstance(b, B))
print(isinstance(b, A))

