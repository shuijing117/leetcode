# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
# 注意：如果对空文本输入退格字符，文本继续为空。
# 示例 1：
# 
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, S, T):
        skipS = 0
        skipT = 0
        i = len(S) - 1
        j = len(T) - 1

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >=0:
                return False

            i -= 1
            j -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare('ab#c', 'ad#c'))
    print(solution.backspaceCompare('ab##', 'c#d#'))
    print(solution.backspaceCompare('a##c', '#a#c'))
    print(solution.backspaceCompare('a#c', 'b'))
    print(solution.backspaceCompare('a#b', 'b'))
