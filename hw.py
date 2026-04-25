data=[1, 2, 3, 4, 5, 6]

squared=[x**2 for x in data]
even=[x for x in data if x %2==0]
labeled=["even" if x % 2==0 else "odd" for x in data]

print("squared",squared)
print("even",even)
print("labeled",labeled)