phrase = input("Enter a phrase: ")
phrase = phrase.upper()
dict={}
for i in phrase:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
for i in sorted(dict):
    if i == " ":
        continue
    else:
        print(i, end=" ")
        for l in range(dict[i]):
            print("*", end=" ")
        print("")
    