# Copyright (c) 2020 App Annie Inc. All rights reserved.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(i):
            if parents[i] != i:
                return find(parents[i])
            return i

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            parents[root_j] = root_i

        n = len(accounts)
        parents = list(range(n))
        emails = [set(i[1:]) for i in accounts]
        for i in range(n):
            for j in range(i + 1, n):
                if emails[i] & emails[j]:
                    union(i, j)
        res = {}
        for i, parent in enumerate(parents):
            root = find(parent)
            if root in res:
                res[root][1].update(accounts[i][1:])
            else:
                res[root] = accounts[i][0], set(accounts[i][1:])
        ret = [[name, *sorted(emails)] for name, emails in res.values()]
        return ret


