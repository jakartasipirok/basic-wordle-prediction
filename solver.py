test = open("sample.txt", "r")
list_of_lists = []
a_file = test.read()
data_into_list = a_file.split("\n")
test.close()

unique_list = []
possible_words = []

def is_exist(included, list):
      for words in list:
            found = True
            for letter in included:
                  if letter not in words:
                        found = False  
            if found == True:
                  possible_words.append(words)

def is_not_exist(letter, list1):
      for words in list(list1):
            if letter in words:
                  list1.remove(words)

def find_known(letter, loc, list1):
      for words in list(list1):
            if words[loc-1] != letter:
                  list1.remove(words)

def del_known(letter, loc, list1):
      for words in list(list1):
            if words[loc-1] == letter:
                  list1.remove(words)

while True:
      exist_letter = input("include: ")
      is_exist(exist_letter, data_into_list)
      not_exist_letter = input("exclude: ")
      for i in not_exist_letter:
            is_not_exist(i, possible_words)

      while True:
            done = input("any known location(y/n): ")
            if done == "n":
                  break
            elif done == "y":
                  letter = input("letter? ")
                  location = int(input("location? "))
                  find_known(letter, location, possible_words)

      while True:
            done = input("any known false location(y/n): ")
            if done == "n":
                  break
            elif done == "y":
                  letter1 = input("letter? ")
                  location1 = int(input("location? "))
                  del_known(letter1, location1, possible_words)

      print("Possible Words: ")
      print(possible_words)
      cont = input("continue(y/n): ")
      if cont == "n":
            break
      else:
            data_into_list = possible_words