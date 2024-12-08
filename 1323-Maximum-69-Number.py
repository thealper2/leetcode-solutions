class Solution:
    def maximum69Number(self, num: int) -> int:
        s_num = str(num)
        found = False
        temp = 0
        idx = len(s_num) - 1

        for i in range(len(s_num)):
            if s_num[i] == "6" and found == False:
                temp += 9 * (10 ** idx)
                found = True
            else:
                temp += int(s_num[i]) * (10 ** idx)

            idx -= 1

        return temp