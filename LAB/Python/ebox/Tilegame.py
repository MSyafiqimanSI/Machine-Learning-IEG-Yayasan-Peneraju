print("Enter the side in cm of a square tile")
sidesValue = int (input())
areaSq = sidesValue * sidesValue

print("Enter the number of square tiles available")
Numtiles = int(input())
x = int(Numtiles ** 1/2)

posbArea = str(x * areaSq)
print(f"Area of the largest possible square is {posbArea}sqcm")