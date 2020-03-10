def square(x):
  return x * x

# FOR PYTHON 3.6 OR LOWER
# FOR LOOP => FIRST BRACKETS REFERS TO i, SECOND BRACKETS REFERS TO square(i)
# the brackets is just a placeholders
# for i in range(5):
#   print("{} squared is {}".format(i, square(i)))

# FOR PYTHON 3.6 OR HIGHER
# FOR LOOP => FIRST BRACKETS REFERS TO i, SECOND BRACKETS REFERS TO square(i)
# the brackets is just a placeholders
def main():
  for i in range(10):
    print(f"{i} squared is {square(i)}")

if __name__ == "__main__":
  main()