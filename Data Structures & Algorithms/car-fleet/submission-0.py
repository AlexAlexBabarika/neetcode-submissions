class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # brute force
        n = len(position)
        ps = list(zip(position, speed))
        ps.sort(key=lambda x: x[0], reverse=True)

        # time = [0] * n
        stack = [(target - ps[0][0]) / ps[0][1]]
        for i in range(1, n):
            time = (target - ps[i][0]) / ps[i][1]

            if stack and time > stack[-1]:
                stack.append(time)

        return len(stack)




        