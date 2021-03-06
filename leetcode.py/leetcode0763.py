# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
#
#  
#
# 示例 1：
#
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-labels
class Solution:
    def partitionLabels(self, S: str):
        # last = [0] * 26
        # for i, ch in enumerate(S):
        #     last[ord(ch) - ord("a")] = i
        #
        # partition = list()
        # start = end = 0
        # for i, ch in enumerate(S):
        #     end = max(end, last[ord(ch) - ord("a")])
        #     if i == end:
        #         partition.append(end - start + 1)
        #         start = end + 1
        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, S.rindex(ch))
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition


if __name__ == '__main__':
    solution = Solution()
    print(solution.partitionLabels('ababcbacadefegdehijhklij'))
