#Step 1 
import random
from logo import logo
from word import word_list
from image import stages

print(logo)
word_to_find=random.choice(word_list)
found=[]
life=6
for x in range(0,len(word_to_find)):
  found.append('_')
done=True  
while done:
  letter=input("enter a letter ").lower()
  if letter in word_to_find:
    for x in range(0,len(word_to_find)):
      letter1=word_to_find[x]
      if letter == word_to_find[x]:
        found[x]=letter
    print(found)
    print(stages[life])
    print("You guessed right, guess more..!")
    if "_" not in found:
      done=False
      print("You Won")
   
  else:
    print(f"You guessed wrong. {letter} is not in the word and you lost a life")
    life-=1
    print(stages[life])
  if life==0:
    done=False
    print(f"you lost the word is {word_to_find}")