import random
def initial():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])
  rnd = random.randint(0, last)

if __name__== "__main__":
  initial()
