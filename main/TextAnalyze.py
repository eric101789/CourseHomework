import pandas as pd

infile = open('python_example_001.txt')
lines = (infile.read()).split("\n")

line_count = len(lines)
word_count = 0
char_count = 0

# 計算字數、行數、字元數
for line in lines:
    words = line.split()
    word_count += len(words)
    char_count += len(line)

# 計算單字出現次數
lines = list(lines)
# print("lines = ", lines)
string = " ".join(lines)
# print("string = " + string)
word = string.split()
# print("word = ", word)

# 列印結果
print(f"File has {line_count} lines, {word_count} \
words, {char_count} characters")
print(pd.Series(lines).value_counts())
