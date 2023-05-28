h = (lambda x, y, z: (x + y + z))(int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: ")))
print(h)

i = (lambda *args:sum(args)) (int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: ")))
print(i)