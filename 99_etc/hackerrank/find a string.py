'''
두번째줄 인풋이 첫번째줄 인풋에 몇번 등장하는지 카운트
'''


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string)+1):
        if string[i:i + len(sub_string)] == sub_string[:]:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

'''
list comprehension 으로 짜보기
print(sum([1 for i in range(len(string) - len(sub_string) +1) if string[i:i+len(sub_string)] == sub_string[:]]))
'''