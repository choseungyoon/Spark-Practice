# This is a sample Python script.
from collections import defaultdict

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# Text가 크지 않을 경우는 Spark를 사용하는 것보다 간단한 Python Code로 작성해도 괜찮다
# 그러다 Text가 커지고 File이 많아지는 경우엔 Python code는 하나의 Thread로 동작하기 때문에 한계가 있다.
# 그런 환경에서는 본격적으로 Spark가 용이할 수 있다.

if __name__ == '__main__':
    print_hi('PyCharm')
    words_count : dict[str,int] = defaultdict(int) # defaultdict를 사용하면 초기값이 항상 0으로 Setting

    with open('data/words.txt', 'r') as file:
        for _,line in enumerate(file):
            words_each_line = line.strip().split(" ")

            for _,word in enumerate(words_each_line):
                words_count[word] += 1


    for word, count in words_count.items():
        print(f'{word}: {count}')