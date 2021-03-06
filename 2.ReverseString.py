'''
    题目：单词翻转。输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变，
    句子中单词以空格符隔开。为简单起见，标点符号和普通字母一样处理。例如，
    输入“I am a student.”，则输出“student. a am I”。
'''

import sys

def ReverseString(string, start, end):
    s = list(string)
    while(start < end):
        t = s[start]
        s[start] = s[end]
        s[end] = t
        start = start + 1
        end = end - 1
    str1 = ''.join(s)
    return str1


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(line.split())
        results = ''
        s = ''
        for i in range(len(values)):
            string = values[i]
            values[i] = ReverseString(string, 0, len(string)-1)
        results = ' '.join(values)
        results = ReverseString(results, 0, len(results)-1)
        print(results)