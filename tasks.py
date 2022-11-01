from sympy import isprime

# task 1
print([x for x in range(1, 1000) if x % 7 == 0])

# task 2
print([x if x % 3 == 0 else str(x) * 2 for x in range(1, 1000)])

# task 3
s = "  hel l o      world   "
spaces = [x for x in s if x == " "]
print(len(spaces))

# task 4
s = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
result = [x for x in s.split() if x.startswith("Y") or x.startswith("y")]
print(result)

# task 5
s = "hi, 3.44, 535  "
result = [(i, v) for i, v in enumerate(s)]
print(result)

# task 6
s = "In 1984 there were 13 instances of a protest with over 1000 people attending"
result = [x for x in s.split() if x.isdigit()]
print(result)

# task 7
result = ["чётное" if x % 2 == 0 else "нечётное" for x in range(1, 20)]
print(result)

# task 8
s ="The trickiest part of learning list comprehension for me was really understanding the syntax."
result = [x for x in s.split() if len(x) < 4]
print(result)

# task 9
result = [x for x in range(1, 50) if isprime(x)]
print(result)