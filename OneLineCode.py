# _*_ coding: utf-8 _*_
# 打印心形
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+
(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30,
30)]) for y in range(30, -30, -1)]))
# 打印一个奇怪的形状
print('\n'.join([''.join(['*'if abs((lambda a: lambda z, c, n: a(a, z, c,
n))(lambda s, z, c, n: z if n == 0 else s(s, z*z+c, c, n-1))(0,
0.02*x+0.05j*y, 40)) < 2 else ' ' for x in range(-80, 20)]) for y in
range(-20, 20)]))
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1,
x+1)]) for x in range(1, 10)]))
# 打印100以内的所有素数
print(' '.join([str(item) for item in filter(lambda x: not [x % i for i in
range(2, x) if x % i == 0], range(2, 101))]))
print(' '.join([str(item) for item in filter(lambda x: all(map(lambda p: x
% p != 0, range(2, x))), range(2, 101))]))
# 输出2的1000次方
print(sum(map(int,str(2**1000))))
