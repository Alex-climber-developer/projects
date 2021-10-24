import time
parties=int(input("колво партий ,игр "))
from random import randint
tasks_dict={}
all_stics=0
for i in range(0,parties):
  task=("%d * %d +%d - %d * %d"%(randint(3,10),randint(11,25),randint(5,126),randint(3,10),randint(11,21)))
  tasks_dict[task]=eval(task)
class player:
  is_win = 0
  def who_first():
    global all_stics
    all_stics=int(input("кол-во палочек в игре  "))
    time.sleep(1)
    print("У тебя есть 30s что бы дать ответ.Успеешь-твой ход.\n Иначе ответ не засчитан и хожу 1ый Я. \nГотовься")
    time.sleep(3)
    for sec in range(1,4):
      print(sec)
      time.sleep(1)
    timer1 = time.time()
    try:
      resh=int(input("реши: "+list(tasks_dict.items())[part-1][0] + "=  "))
      if time.time() - timer1 <= 30:
        return resh == list(tasks_dict.items())[part-1][1]
      elif time.time() - timer1 > 30:
        print("Looz. Ты считал.. %d секунд..." % (round(time.time() - timer1, 1)))
        return False
    except:
      print("Тип данных вывода не верный у тебя")
      return False

  def step(self,count):
    global all_stics
    self.count=count
    all_stics-=self.count
    if self == user:
      time.sleep(1.5)
      print("ВЫ взяли %d ,осталось (%d шт)вот они" %(self.count,all_stics))
      time.sleep(0.5)
      print("I " * all_stics)
    if self == komp:
      time.sleep(1.5)
      print("Я беру %d , остаток-  %s (%d шт)" %(self.count,("I "* all_stics),all_stics))
    if all_stics == 1:
      time.sleep(1.5)
      print("Ну вот кто-то и продул..\nКонец игры")
      self.is_win+=1

  def knowns(self):
    global all_stics
    global is_win
    if self==user:
      if all_stics!=1:
        time.sleep(1.5)
        self.step(int(input("Сколько берете-   ")))
    elif all_stics%4-1 == 0:
      time.sleep(1)
      print("Эх,сложно дело")
      return self.step(1)
    elif all_stics!=1:
      if 1<all_stics<5:
        time.sleep(1.5)
        return self.step(all_stics-1)
      elif all_stics%4==0:
        time.sleep(1.5)
        return self.step(3)
      elif all_stics == 1:
        time.sleep(1.5)
        print("Ну вот кто-то и продул..\nКонец игры")
        self.is_win+=1
      else:
        time.sleep(1.5)
        return self.step(all_stics%4-1)

komp= player()
user=player()
for part in range(1,parties+1):
  if player.who_first() == True:
    user.knowns()
  else:print("Ахах,ошибочка,хожу я.Верный ответ- %d"%(int(list(tasks_dict.items())[part-1][1])))
  while komp.is_win!=part or user.is_win!=part:
    if komp.is_win == part:
      print("Я ВЫИГРАЛ,я молодец!")
      break
    if user.is_win == part:
      print("Юзер, Поздравляю С победой!")
      break
    komp.knowns()
    user.knowns()
  if part<parties:
    print("следующий,%d кон!"%(part+1))
    if part==parties-1:print("Настройся,ПОСЛЕДНИЙ кон")
  elif part==parties:print("приятно было побороться! Наш счет итого-YOU %d : %d (My)"%(user.is_win, komp.is_win ))