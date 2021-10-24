import random
him_step=0
my_chislo=1.5
count_komp=0
count_my=0
who_winner_now=""
my_offer=100 #мои предложения ответов
user_sad="" #подсказки
step=0 #считать попытки
last_big=0 #вспомогательная для проверки на то нужно ли делать ср . арифмет или то то другое нужно
last_min=0#аналогично
my_answ=[] #массив для сверки положения какой то цифры относ-но нашей
help_for_me=0 #вообще говн-о код переменная счетчик зашел ли код в условие №2
end_step="" 
end_coin=""#окончания
coin=0
plays=int(input("Привет,до скольки очков играем?   "))
print("Что ж тогда начнемс")
while count_komp!=plays or count_my!=plays:
  while user_sad.lower()!="угадал":
    print("Прием юзер, загадай число от 1 до 100 ")
    step+=1
    print("может это %d" %my_offer)
    my_answ.append(my_offer)
    user_sad=str(input("дай подсказку-твое число: больше / меньше / угадал:::  "))
    if user_sad.lower()=="меньше":
      try: #нужен для того что видите ли если у меня есть ряд взаимозависимых условий и в одном проблема какая то(тут например поиск эл в массиве с инд-ом -2,которого еще нет) то он НЕ проверяет и не исполняет остальн условия,ЭТО ЖЕ НЕ ЛОГИЧНО ,ПОЧЕМУ ТАК??? из за этого пришлось ввести дурацкую ветвь против этой ошибки
        if my_answ[-2]<my_offer:
          last_min=my_answ[-2]
          my_offer=(last_min+my_answ[-1])//2  
        elif help_for_me>0 and my_answ[-2]>my_offer:
          my_offer==(my_answ[-2]+my_answ[-1])//2
        if step>3: print("жаль ,а я думал,что наконец то угадал")
      except:my_offer=my_offer//2 #иначе говоря если это цифры которые не заходили в условие №2,и не прибавлялись еще,я не мог придумать как это описать условием и пришлось  писать ветвь  else
      else: 
        if  my_answ[-2]<my_offer or (help_for_me>0 and my_answ[-2]>my_offer):
          None # для того что ошибок нет,все что нужно выполнилось в try ,тут не надо ничего
        else:my_offer=my_offer//2 #для того чтоб если ошибок нет ,но в ветвь усл №2 еще не заходили
  #усл №2
    if user_sad.lower()=="больше":
      help_for_me+=1 
      # для меня helpforme ,чтоб определять заходили ли в условие где больше
      if step>3:print("черт ,где же мои мозги,ведь наверно почти угадал")
      if my_answ[-2]>my_offer:
        last_big=my_answ[-2]                
        my_offer=(my_answ[-2]+my_answ[-1])//2
      else:my_offer=(last_big+my_answ[-1])//2
    if user_sad.lower()=="угадал":
      def ygadal(step,znatok,randomer,who_step):
        coin=10-step
        if coin<0:
          coin=0
        randomer+=coin
        if 21>step>=5 :
          end_step="ов"
        elif step==1 :
          end_step=""
        elif 5>step>=2:
          end_step="а"
        if coin==1 :
          end_coin="о"
        if 4<coin<11:
          end_coin="ов"
        elif 1<coin<5:
          end_coin="а"
        if randomer>znatok:
          who_winner_now="мою"
        elif randomer<znatok:
          who_winner_now="твою,блин"
        else:who_winner_now="ничью"
        print("Ну я ж говорил я мастер,всего %d ход%s" %(step, end_step))
        print("Ого,мне дается %d очк%s" %(10-step,end_coin))
        print("Итого у нас счет: %d : %d , в %s пользу" %(randomer,znatok, who_winner_now))
        step=0
    if count_komp>=plays or count_my>=plays:
          break    

  
  input("((Поздоровайся))   ")
  try:
    a=int(input("Привет!напиши ка откуда загадывать мое число(напиши число)   " ))
    b=int(input("Да ,и напиши еще верхнюю границу ( число)   "  ))
  except:
    print("Ну я же просил четко вводить числа")
    print("вы попуали с вводом,я сам определю диапазон")
    a=random.randint(-10,10)
    b=random.randrange(50,300,50)
    print("Гадай в диапазоне (%d, %d)" %(a,b))
  him_chislo= random.randint(a,b)
  print("Я загадал!Поехали))")
  while my_chislo!=him_chislo:
    him_step+=1
    my_chislo=int(input("Юзер(введи число)-  "))
    if my_chislo<him_chislo:
      print("Неа, Больше")
    elif my_chislo>him_chislo:
      print("Неа, Меньше")
    elif my_chislo==him_chislo:
      ygadal(step,count_komp,count_my,him_step)
      # coin=10-him_step
      # if coin<0:
      #   coin=0
      # count_my+=coin
      # if 21>him_step>=5 :
      #   end_step="ов"
      # elif him_step==1 :
      #   end_step=""
      # elif 5>him_step>=2:
      #   end_step="а"
      # if coin==1 :
      #   end_coin="о"
      # if 4<coin<11:
      #   end_coin="ов"
      # elif 1<coin<5:
      #   end_coin="а"
      #   break
      # if count_komp<count_my:
      #   who_winner_now="твою,блин"
      # elif count_komp>count_my:
      #   who_winner_now="мою"
      # else:who_winner_now="ничью"
      # print("Молодец!Ты угадал,всего %d ход%s" %(him_step, end_step))
      # print("ММ, тебе дается %d очк%s" %(10-him_step, end_coin))
      # print("Итого у нас счет: %d : %d , в %s пользу" %(count_komp,count_my, who_winner_now))
      # him_step=0
      print("Теперь моя очередь")
      break
  if count_komp>=plays or count_my>=plays:
    break
print("Ну вот,игра закончена со счетом %d : %d , в %s пользу. Ура!!" %(count_komp,count_my, who_winner_now))
    


# him_offer=100 #мои предложения ответов
# komp_sad="" #подсказки
# him_step=0 #считать попытки
# him_last_big=0 #вспомогательная для проверки на то нужно ли делать ср . арифмет или то то другое нужно
# him_last_min=0#аналогично
# him_answ=[] #массив для сверки положения какой то цифры относ-но нашей
# help_for_him=0 #вообще говн-о код переменная счетчик зашел ли код в условие №2
# input("((Поздоровайся))   ")
# print("Привет! Что ж начнемс,я загадал   ")
# while komp_sad.lower()!="угадал":
#   him_step+=1
#   print("может это %d ?" %him_offer)
#   him_answ.append(him_offer)
#     try:
#       if my_answ[-2]<him_offer:
#         him_last_min=my_answ[-2]
#         him_offer=(him_last_min+my_answ[-1])//2  
#       elif help_for_him>0 and my_answ[-2]>him_offer:
#         him_offer==(my_answ[-2]+my_answ[-1])//2
#       if him_step>3: print("жаль ,а я думал,что наконец то угадал")
#     except:him_offer=him_offer//2 #иначе говоря если это цифры которые не заходили в условие №2,и не прибавлялись еще,я не мог придумать как это описать условием и пришлось  писать ветвь  else
#     else: 
#       if  my_answ[-2]<him_offer or (help_for_him>0 and my_answ[-2]>him_offer):
#         None # для того что ошибок нет,все что нужно выполнилось в try ,тут не надо ничего
#       else:him_offer=him_offer//2 #для того чтоб если ошибок нет ,но в ветвь усл №2 еще не заходили
#       komp_sad.lower()=="меньше":
# #усл №2
#   if komp_sad.lower()=="больше":
#     help_for_him+=1 
#     # для меня helpforme ,чтоб определять заходили ли в условие где больше
#     if him_step>3:print("черт ,где же мои мозги,ведь наверно почти угадал")
#     if my_answ[-2]>him_offer:
#       him_last_big=my_answ[-2]                
#       him_offer=(my_answ[-2]+my_answ[-1])//2
#     else:my_offer=(him_last_big+my_answ[-1])//2
#   if komp_sad.lower()=="угадал":
#     print("Ну я ж говорил я мастер,всего %d ходов" %him_step)




#  угадайка юзера кратко

import random
him_step=0
my_chislo=1.5
input("((Поздоровайся))   ")
try:
  a=int(input("Привет!напиши ка откуда загадывать мое число(напиши число)   " ))
  b=int(input("Да ,и напиши еще верхнюю границу ( число)   "  ))
except:
  print("Ну я же просил четуо вводить числа")
  print("вы попуали с вводом,я сам определю диапазон")
  a=random.randint(-10,10)
  b=random.randrange(50,300,50)
  print("Гадай в диапазоне (%d, %d)" %(a,b))

him_chislo= random.randint(a,b)
print("Я загадал!Поехали))")
while my_chislo!=him_chislo:
  him_step+=1
  my_chislo=int(input("Юзер(введи число)-  "))
  if my_chislo<him_chislo:
    print("Неа, Больше")
  elif my_chislo>him_chislo:
    print("Неа, Меньше")
  else:print("Молодец!Ты угадал,всего %d ходов" %him_step)

