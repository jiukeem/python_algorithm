# my solution
def solution(numbers, hand):
    left, right = '*', '#'
    point = {1: (1, 1), 2: (1, 2), 3: (1, 3),
             4: (2, 1), 5: (2, 2), 6: (2, 3),
             7: (3, 1), 8: (3, 2), 9: (3, 3),
             '*': (4, 1), 0: (4, 2), '#': (4, 3)}

    def dist(pt1, pt2):
        return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

    ans = ''
    for n in numbers:
        if n in [1, 4, 7]:
            left = n
            ans += 'L'
        elif n in [3, 6, 9]:
            right = n
            ans += 'R'
        elif n in [2, 5, 8, 0]:
            left_dist, right_dist = dist(point[n], point[left]), dist(point[n], point[right])
            if left_dist < right_dist:
                left = n
                ans += 'L'
            elif right_dist < left_dist:
                right = n
                ans += 'R'
            else:
                if hand == 'right':
                    right = n
                    ans += 'R'
                else:
                    left = n
                    ans += 'L'

    return ans
# Status: Accepted
# Note: 좀 더 깔끔하게 짤 수는 없을까 고민했는데 다른 사람들 풀이를 봐도 비슷비슷하다.
#       내 코드가 제일 잘 읽히는 것 같당ㅎ.ㅎ