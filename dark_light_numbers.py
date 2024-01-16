# Time importation
import time

# Greetings
print("=" * 35)
print("Velcome")
print("=" * 35)

# Counter / Loading
for i in range(1,4):
    print(i)
    time.sleep(1)
    continue
# Title
print("_" * 25)
print("Dark_Light_Numbers")
print("_" * 25)

# insert Positive or Negative numbers
user = int(input("Insert number: "))
print()

# Validation, Positive or Negative numbers
print("=" * 25)
if user < 0:
    print("Dark numbers")
else:
    print("Light number")
print("=" * 25)
