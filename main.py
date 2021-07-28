import random
select=int(input("select 1 for ROCK, 2 for SCISSOR, 3 for PAPER: "))
random=random.randint(1,3)
if select==random:
    print("you selected")
    print("rock"'''\n    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    print("computer selected\nrock")
    print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''"\ngame is draw ")
elif select==1 and random==2:
    print("you selected")
    print("rock"'''\n    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    print("computer selected\nscissors")
    print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''"\nyou win")
elif select==1 and random==3:
    print("you selected\nrock")
    print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    print("computer selected\npaper")
    print('''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''"\ncomputer win")
elif select==2 and random==1:
    print("you selected\nscissors")
    print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
    print("system selected\nrock")
    print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''"\n system wins")
elif select==2 and random==3:
    print("you selected\nscissors")
    print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
    print("system selected\npaper")
    print('''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''"\nyou win")
elif select==3 and random==1:
    print("you selected\npaper")
    print('''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')
    print("system selected\nrock")
    print('''  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''"\nyou win")
elif select==3 and random==2:
    print("you selected\npaper")
    print('''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')
    print("system selected\nscissors")
    print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''"\nsystem wins")
else:
    print("select a option")
        