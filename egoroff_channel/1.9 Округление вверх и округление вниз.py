
import math
L, W, H = map(int, input().split())
print(math.ceil((2*H*(L+W))/16))
