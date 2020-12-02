original_word = input("Enter your word: ")
modified_word = input("Enter missed letters word: ")
no_of_trails = int(input("Enter no.of trails: "))

missing_numbers = list()
for i in range(0, len(original_word)):
    if (original_word[i] != modified_word[i]):
        missing_numbers.append(original_word[i])
        print(modified_word)

for j in range(0, no_of_trails):
    if len(missing_numbers) != 0:
        enter_character = input("Enter character: ")
        if enter_character in missing_numbers:
            missing_numbers.remove(enter_character)
            print(modified_word)
            print("correct and continue")
        else:
            print("wrong Try again")
            print(modified_word)
    else:
        if len(missing_numbers) == 0:
            print("YOU WIN")
            break
