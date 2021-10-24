import random

MAGIC_KEY= 89290404535
words=[]
ind_let=[]
step1= step2= step3= step4= step5= step6= " "
sekretw=''
space_letters = ''
hard= 1
count=0

f = open("projects/viselutsa/data.txt",'r')
f=f.read()
strs=f.split('\r\n')

for s in strs :
  words.append(s.split(' ')[1])
print(words)


grid =[['+', '_', '_', '_', '_', '+'],
       ['|', ' ', ' ', ' ', '|', ' '],
       ['|', ' ', ' ', ' ', step1, ' '],
       ['|', ' ', ' ', step3, step2, step4],
       ['|', ' ', ' ', ' ', step5, step6],
       ['|', ' ', ' ', ' ', ' ', ' '],
       ['|', ' ', ' ', ' ', ' ', ' '],
       ['|', ' ', ' ', ' ', ' ', ' '],
       ['|', ' ', ' ', ' ', ' ', ' ']]

people=['◓','▊','\\','/','/','\\']

congrat=[
  ["Здорово.Ты сможешь еще","Круто ,не сбавляй темп","Угадал ,повезло же",'Молодец. Не плохо',"Скоро  все и отгадаешь)",'Может еще отгадаешь что нибудь?'],

  ['Ну-ну ,что то пошло не по плану','Не та буковка','Как ты там не умер еще? ','Играть ты умеешь конечно','Ну эдак мы скоро закончим ','а ведь  у  тебя были все шансы']
]


def random_word(h):
  index=random.randint(100*h-100,100*h-1)
  sekret_word=words[index]
  return sekret_word


def hardness():
  global hard, sekretw, space_letters

  print('Начнем игру: выберите уровень сложности от 1 до 10\n')
  hard = input('-- ')
  try: 
    if type(int(hard)) == int and 1<=hard>=10 :
      hard = int(hard)
  except: 
    print('Установлено значение по умолчанию')
    hard=1
  sekretw= random_word(hard)
  space_letters = "_" * len(sekretw)

hardness()

input_magic=input('если знаете чит - введите , иначе Enter    ')
if input_magic == str(MAGIC_KEY):print(sekretw)

def paint (res,letter):
  # смотрит 1 или 0 и меняет спейс  пишет счет поздравления и рисует грид
  global count, step1, step2, step3, step4, step5, step6
  ind=random.randint(0,5)
  
  if res == 1:
    print(congrat[0][ind])
    for i in range(0,len(sekretw)):
      if sekretw[i]== letter:
        space_letters[i] = letter
        ind_let.append(i)
    

  else:
    print(congrat[1][ind])
    count+=1
    name= 'step'+str(count)
    name= people[count-1]
    if count==6:
      print('Конец игры')
      return 'end'
    
  for l in space_letters : print(i+' ') 
  print(len(ind_let,' / ',len(sekretw)))

  for x in range(len(grid)):
    for y in range(len(grid[x])):
        print(grid[x][y],' ', end='')
  print()

while 1:
  input_let=input('Введите букву:  ')
  is_here=1 if input_let in sekretw else 0
  
  if paint(is_here,input_let)!='end':
    paint(is_here,input_let)
  else: break










