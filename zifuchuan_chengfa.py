class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        for i in range(m-1, -1, -1):
            digt1 = int(num1[i])
            add = 0
            str_list = []
            for j in range(n-1, -1, -1):
                digt2 = int(num2[j])
                res1 = (digt1*digt2+add)%10
                add = (digt1*digt2+add)//10



fun = Solution()
print(fun.multiply(num1 = "123", num2 = "456"))