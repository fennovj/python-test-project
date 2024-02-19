x = 1

print(f"run foo.foo at {__name__}")

from .bar import y
print(y)