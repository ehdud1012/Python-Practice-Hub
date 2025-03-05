
l = ["가", "나", "다"]

a = "라"

if a not in l:
    l.append(a)

print(l.index(a))
print(l)