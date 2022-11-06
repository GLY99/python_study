class Solution:
    def interpret(self, command: str) -> str:
        """
        请你设计一个可以解释字符串 command 的 Goal 解析器 。
        command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。
        Goal 解析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。
        然后，按原顺序将经解释得到的字符串连接成一个字符串。
        给你字符串 command ，返回 Goal 解析器 对 command 的解释结果。
        :param command:
        :return:
        """
        return command.replace('G', 'G').replace("()", 'o').replace("(al)", "al")

    def interpret(self, command: str) -> str:
        """
        请你设计一个可以解释字符串 command 的 Goal 解析器 。
        command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。
        Goal 解析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。
        然后，按原顺序将经解释得到的字符串连接成一个字符串。
        给你字符串 command ，返回 Goal 解析器 对 command 的解释结果。
        :param command:
        :return:
        """
        ans = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                ans += 'G'
                i += 1
            elif command[i] == '(' and command[i + 1] == ')':
                ans += 'o'
                i += 2
            else:
                ans += "al"
                i += 3
        return ans
