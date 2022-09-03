n = (int(input))
gab= (input)
resp= (input)

acerto = 0

i = 0

while i < n:
    if gab [i] == resp [i]:
        acerto += 1
    i += 1
print(acerto)