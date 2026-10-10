from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_to_name = {}
        graph = defaultdict(list)

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                emails_to_name[email] = name
                graph[first_email].append(email)
                graph[email].append(first_email)

        print(emails_to_name)
        print(graph)

        visited = set()
        res = []
        for email in emails_to_name:
            if email not in visited: 
                current_emails = []
                stack = [email]
                visited.add(email)

                while stack:
                    curr = stack.pop()
                    current_emails.append(curr)

                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                res.append([emails_to_name[email]] + sorted(current_emails))
        return res

        