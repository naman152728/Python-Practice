a = 12
b = 1.2
c = "Naman"
d1 = True
d2 = False

print("The value of a is: ", a, "\n& the type is: ", type(a))
print("\n")

print("The value of b is: ", b, "\n& the type is: ", type(b))
print("\n")

print("The value of c is: ", c, "\n& the type is: ", type(c))
print("\n")

print("The value of d1 is: ", d1, "\n& the type is: ", type(d1))
print("The value of d2 is: ", d2, "\n& the type is: ", type(d2))
print("\n")

# Playing with Boolean
print("d1 + d2 = ", d1 + d2)
print("d1 - d2 = ", d1 - d2)
print("d1 * d2 = ", d1 * d2)

print("d2 + d1 = ", d2 + d1)
print("d2 - d1 = ", d2 - d1)
print("d2 * d1 = ", d2 * d1)

print("/n")

a += b

print("The Value of a after adding with b is: ", a,
      "\n& the current type is: ", type(a))
print("\n")
c = a

print("The value of c is now: ", c, "\n& the type is: ", type(c))

#Adding of int with bool
print(a)
print(a + (d1 + d1))

#complex num.
e = 4 - 2 * 9j
print("The value of e is: ", e, "\n& the type is: ", type(e))

print(e.real)
print(e.imag)
print(e.conjugate)
