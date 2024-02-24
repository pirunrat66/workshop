def f(x):
    return x**2-4

def df(x):
    return 2*x

from newton import NewtonMethod


x = 10
f_x = f(x)
df_x = df(x)

aaa = NewtonMethod(f,df)
aaa.solve(x,1e-10,100)

