import random

# 生成一个10以内数字不重复的4位数
digits = list(range(10))
random.shuffle(digits)
number = digits[:4]

print("我想到了一个由不重复数字组成的4位数。")

# 循环猜测，直到猜对为止
while True:
    # 获取用户猜测的数字
    guess = input("请猜一猜这个数字是多少（4位数字，不重复）：")

    # 判断用户猜测的数字是否合法
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        print("无效的猜测，请输入4位数字且每个数字不重复。")
        continue

    # 计算数字和位置都猜对的个数
    correct = sum(1 for i in range(4) if guess[i] == str(number[i]))

    # 计算数字正确但位置不对的个数
    misplaced = sum(1 for i in range(4) if guess[i] in str(number) and guess[i] != str(number[i]))

    # 输出结果
    print(f"{correct}A{misplaced}B")

    # 判断是否猜对了
    if correct == 4:
        print("恭喜你，猜对了！")
        break
