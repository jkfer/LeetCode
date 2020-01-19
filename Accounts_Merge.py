# https://leetcode.com/problems/accounts-merge/
# 721
# Medium - Failed

"""
Refered solution:
Must spend more time to understand DFS solution.
"""

import collections


class Solution:
    def accountsMerge(self, accounts):
        email_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                # add all other emails of a person to the first email
                # graph of one email to every other
                graph[acc[1]].add(email)

                # add the first email to every other email
                # graph of every other email to one email
                graph[email].add(acc[1])

                # map every email to name
                email_to_name[email] = name

        seen = set()
        ans = []

        # go through the graph keys(emails):
        for email in graph:

            # if email is not seen, add it to seen and:
            if email not in seen:
                seen.add(email)

                # create the stack
                stack = [email]

                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([email_to_name[email]] + sorted(component))
        return ans


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]

S = Solution()
print(S.accountsMerge(accounts))
