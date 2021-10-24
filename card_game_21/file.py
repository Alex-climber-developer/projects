from  random import randint
card=[0,"Туз",["Валет",2],["Дама",3],["Король",4],5,6,7,8,9]
my_answ=""
my_skill=0
new_card=""
new_card_img=""
my_cards=[]

him_answ=""
him_skill=0
him_new_card=""
him_new_card_img=""
him_cards=[]
def get_card(num, who_new,cards,who_img ):
  print("Держи %d карту" %num)
  who_new=randint(0,10)
  if who_new==2 or who_new==3 or who_new==4:
    who_img=randint(0,1)
    cards.append(card[who_new][who_img])
  else:cards.append(card[who_new])
  print("Надо еще?")
  my_answ=str(input("Да/Нет,ваша очередь:   "))
  if my_answ=="Да":
    get_card(num+1, new_card, my_cards, new_card_img)
    def add_skill():
      my_skill+=new_card

  if my_answ.find("Нет")==True:
    get_card()




    print("Вскрываетесь?")
    if my_answ=="Да":
      print("Какие у вас карты?")
      my_cards=input("(через пробел,с большой буквы)  ")

get_card(1)




class player:
  take_round():
    


  give_round():









