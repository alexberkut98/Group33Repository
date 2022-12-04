import NewTextTone_core as main

greeting_text = main.greeting()
print(greeting_text)
nomatter = input()
isexit = False
while not isexit:
  text_result = main.exam_text(main.get_text())
  print('...')
  print(text_result)
  print('<<<')
  
  config = main.readconfig()
  repeat = input(config['repeat_text'])
  
  while repeat != 'n' and repeat != 'y':
    repeat = input('Некорректный ввод. Ожидаю ответ "n" или "y":')
  if repeat == 'n':
    isexit = True
  
print(config['end_text'])
print('Завершено пользователем...')
