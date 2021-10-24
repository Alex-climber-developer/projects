# Разработать программу-анализатор чемпионата по шахматам (при желании можно взять другой вид спорта).
# Имеются следующие объекты:
# - команды (характеризуются статистикой игр игроков данной команды и набранными очками)
# - игроки (характеризуются принадлежностью к команде и личной статистикой)
# - шахматные партии (характеризуются участниками и результатом)

# Требуется разработать методы:
# - обновление статистики игроков и команд в зависимости от результата конкретной шахматной партии (партия(1));
# - сравнения двух игроков по набранным очкам (игрок1 < игрок2: True или False) ;
# - удаление игрока из команды с исключением его статистики (команда - игрок); усложение - дополнительно удалить связную статистику у тех игроков и команд, с которыми он играл;
# - вывода статистики игрока и команды (игрок(), команда())
# - любой дополнительный метод на выбор.

import random
import time
class comand:#команда-контейнер для игрока 
  def __init__(self,name):
    self.name=name
    self.statistic=0
    self.list_players=[]
    # self.num_pers=1 
  def add_to_list(self,score):
    # name_p=str(str(self.name)+"_player"+str(num_pers))
    # name_p=player(score,self.name)
    self.list_players.append(player(score,self.name))
    # self.num_pers+=1
  def statistic(self):
    for pl in list_players:
      self.statistic+=pl.ranking()

class player:
  def __init__(self,score,comand):
    self.comand=comand
    self.wins=0
    self.score=score
  def ranking(self,point):
    self.wins+=point
    return self.wins
  def __del__(self):
    for s in list_com: #поиск команды среди всех,в той где имеа ком и нашего игрока одиаковы
      if s.name==self.comand:s.statistic-=self.wins
    print("Статистика комады %s из-за него упала на %d очков" %(self.comand,self.wins))
    print("Игрок исключен из команды и игр!")
  def __lt__(self,other):#перегрузка оператора ,,меньше,,
    # for each in self.list_players:
    #   for every_each in self.list_players:
        print(self.wins < other.wins)
        if True:print(self,"<",other)
  def __gt__(self,other):#перегрузка оператора ,,больше,,
        print(self.wins > other.wins)
        if True:print(self,">",other)
  def __eq__(self,other):
        print(self.wins == other.wins)
        if True:print(self,"==",other)

class parties:
  def __init__(self):
    print("Партия началась\n Игроки ходят ")
  limit_minus=0
  def limit_down(self,pl1,pl2):
    while pl1.score>0 and pl1.score>0 :
      self.limit_minus=random.randint(1,5)
      pl1.score-=self.limit_minus
      time.sleep(1)
      print('1 игрок потерял %d XP' %self.limit_minus)
      self.limit_minus=random.randint(1,5)
      pl2.score-=self.limit_minus
      time.sleep(1.2)
      print('2 игрок потерял %d XP' %self.limit_minus)
    def update_rank(who_win, who_looz):
      time.sleep(1) # pl2 pl1
      print(f"Игрок {str(who_win)} выиграл ,счет %d-%d"%(pl1.score,pl1.score))
      who_win.ranking(self,1)
      who_looz.ranking(self,-1)
    if pl1.score<0:
      update_rank(pl2,pl1)
    elif pl2.score<0:
      update_rank(pl1,pl2)
      #как объединять однотипные записи типа ,,игрок 1 то-то то-то,и игрок 2 
      #тоже самое,,чтоб одним условием обоих разом...

print("1 стадия игры-<<ДОБАВЛЕНИЕ>> активна")
is_auto=str(input("вам зачислить опыт игрокам радомно?да/нет\n опыт копится с ходом партий и в обличии от очков(побеженных партий,личого и комадого рейтига)он определяет-\n сколько продержится игрок под актакой протвника(типа  хилка)"))
count_p=int(input("Сколько игроков в каждой команде   "))
time.sleep(7)
count_com=int(input("Сколько команд на этом турнире    "))
list_com=[]
for coms in range(1,count_com+1):
  name_com=input(f"Имя {coms} команды: ").lower()
  name_com=comand(name_com)
  list_com.append(name_com)
  for skill in range(1,count_p+1):
    if is_auto!="да" and is_auto!="нет": is_auto=str(input("Неккоректный ответ по поводу автомата скилла,повтори   ")).lower()
    if is_auto=="да":
      name_com.add_to_list(skill+10)#добавляем игрока (каждого)в массив со своим скиллом
    elif is_auto=="нет":
      name_com.add_to_list(input("Введите тогда сколько скилла игроку дать   "))
print("2ая стадия игры-<<БОРЬБА И МЕТОДЫ>> активна")
is_auto=str(input("Режим авто-распределения игроков на партии-да/нет")).lower()
if is_auto!="да" and is_auto!="нет": is_auto=str(input("Неккоректный ответ по поводу автомата скилла,повтори   "))
if is_auto=="да":
  for comm_first in list_com:
    comm_sec=list_com[(list_com.index(coms))+1]#тут отосительно кстати-с точки зрения питона я взял и в ячейку памяти пихнул строку,а потом выпинул ее ,и зафигачил в нее объект.Но вроде также я беру и создаю переменной строковое значение а потом создаю объект уже имеюбщийся pers и присваиваю его строке,чтобы смочь дальше его адекватно вызывать.а то пока у него вообще имени нет
    num_part=1
    for pers in comm_first.list_players:#для каждого игрока из1 команды берем
      for pers2 in comm_sec.list_players:#каждого игрока из след команды ииграем
        name_part="part"+str(num_part)
        print("Это %d партия::: %d игрока VS %d игрока(%d VS %d команда)"%(num_part,comm_first.list_players.index(pers),comm_sec.list_players.index(pers2),list_com.index(comm_first),list_com.index(comm_sec)))
        name_part=parties()
        name_part.limit_down(pers,pers2)
        num_part+=1
elif is_auto=="нет":
  stop_key=False
  num_part=1
  while stop_key==False:
    name_com1=str(input("Введите имя первой команды из %d команд "(count_com))).lower()
    name_com2=str(input("Введите имя второй команды из %d команд "%(count_com))).lower()
    for play_com in list_com:
      if play_com.name==name_com1:
        pl_com1=play_com
      if play_com.name==name_com2:
        pl_com2=play_com
      ind1=str(input("Введите индекс игрока первой команды от0 до %d "%(count_p-1)))
      ind2=str(input("Введите индекс игрока второй команды от0 до %d "%(count_p-1)))
    name_part="part"+str(num_part)
    print("Это %d партия::: %d игрока VS %d игрока(%s VS %s команда)"%(num_part,ind1,ind2,name_com1,name_com2))
    name_part=parties()
    name_part.limit_down(pl_com1.list_players[ind1],pl_com2.list_players[ind2])
    num_part+=1
    stop_answ=str(input("Если турнир завершился, то можете написать ,,стоп,, и партии закончатся   ")).lower()
    stop_key=(stop_answ=="стоп")
how_delit=str(input("Игры закончились,наверняка есть кто наложал-удалим лишних игроков\nКак удем удалять?\n1вар-Удалить у кого меньшие побед\n2вар-Всех кто проиграл в последнем  своем раунде\n3вар-Наконец удалить комманду с меньшей статистикой\n"))
if com1.list_players.index(pers)%3==0:
  print("Удаляем... ")
  name_p.__del__()
  
    
    # print(com1.list_players[pers-1]<com2.list_players[pers-1])
    # print(com1.list_players[pers-1]>com2.list_players[pers-1])
    # com1.list_players[i-1]
