# 직사각형의 경계선
# 단, 직사각형 자체는 x축(y=0), y축(x=0)를 벗어나서 음수 좌표로는 못간다고 보면 된다.

def solve(x,y,w,h):

    return min((w-x), (h-y), x, y)


x, y, w, h = map(int,input().split())
print(solve(x, y, w, h))
