test = open("sample.txt", "r")
list_of_lists = []
a_file = test.read()
data_into_list = a_file.split("\n")
test.close()

unique_list = []
possible_words = []

def is_exist(letter, list):
      for words in list:
            for letters in words:
                  if letters == letter:
                        possible_words.append(words)
                        break

def is_not_exist(letter, list):
      for words in list:
            for letters in words:
                  if letters == letter:
                        list.remove(words)
                        break

def make_unique(list):
      for x in list:
          if x not in unique_list:
              unique_list.append(x)

def find_known(letter, loc, list):
      for words in list:
            if words[loc-1] != letter:
                  list.remove(words)
            break

def del_known(letter, loc, list):
      for words in list:
            if words[loc-1] == letter:
                  list.remove(words)
            break

exist_letter = input("include: ")
for i in exist_letter:
      is_exist(i, data_into_list)
not_exist_letter = input("exclude: ")
for i in not_exist_letter:
      is_not_exist(i, possible_words)

while True:
      done = input("any known location(Y/N): ")
      if done == "N":
            break
      elif done == "Y":
            letter = input("letter? ")
            location = int(input("location? "))
            find_known(letter, location, possible_words)

while True:
      done = input("any known false location(Y/N): ")
      if done == "N":
            break
      elif done == "Y":
            letter1 = input("letter? ")
            location1 = int(input("location? "))
            del_known(letter1, location1, possible_words)

print("Possible Words: ")
print(possible_words)