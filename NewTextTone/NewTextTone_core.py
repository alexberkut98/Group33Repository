from transformers import pipeline

def readconfig():
  config = open('NewTextTone.config', mode='r', newline='\n')

  greeting_text = ''
  start_text = ''
  positive_text = ''
  negative_text = ''
  neutral_text = ''
  end_text = ''
  repeat_text = ''

  while True:
    try:
      line=next(config)
      
      if line=='greeting_text={\n':
        line=next(config)
        while line != '}\n':
          greeting_text = greeting_text + line
          line = next(config)
      
      if line=='start_text={\n':
        line=next(config)
        while line != '}\n':
          start_text = start_text + line
          line = next(config)
          
      if line=='positive_text={\n':
        line=next(config)
        while line != '}\n':
          positive_text = positive_text + line
          line = next(config) 
          
      if line=='negative_text={\n':
        line=next(config)
        while line != '}\n':
          negative_text = negative_text + line
          line = next(config) 
          
      if line=='neutral_text={\n':
        line=next(config)
        while line != '}\n':
          neutral_text = neutral_text + line
          line = next(config) 
          
      if line=='end_text={\n':
        line=next(config)
        while line != '}\n':
          end_text = end_text + line
          line = next(config)       

      if line=='repeat_text={\n':
        line=next(config)
        while line != '}\n':
          repeat_text = repeat_text + line
          line = next(config)  
      
    except StopIteration:
      break
  config.close()

  greeting_text = greeting_text[:-1]
  start_text = start_text[:-1]
  positive_text = positive_text[:-1]
  negative_text = negative_text[:-1]
  neutral_text = neutral_text[:-1]
  end_text = end_text[:-1]
  repeat_text = repeat_text[:-1]

  config = {'greeting_text':greeting_text,
            'start_text':start_text,
            'positive_text':positive_text,
            'negative_text':negative_text,
            'neutral_text':neutral_text,
            'end_text':end_text,
            'repeat_text':repeat_text}
  return config

def check_config():
  config = readconfig()
  print('------')
  print(config['greeting_text'])
  print('------')
  print(config['start_text'])
  print('------')
  print(config['positive_text'])
  print('------')
  print(config['negative_text'])
  print('------')
  print(config['neutral_text'])
  print('------')
  print(config['repeat_text'])
  print('------')
  print(config['end_text'])
  print('------')
  
def greeting():
  config = readconfig()
  greeting_text = config['greeting_text']
  return greeting_text
  
def get_text():
  config = readconfig()
  print(config['start_text'])
  print('>>>')
  input_text = input()
  return input_text
  
def exam_text(input_text: str):
  config = readconfig()
  classifier = pipeline('sentiment-analysis',   
                        'blanchefort/rubert-base-cased-sentiment')
  exam_result = classifier(input_text)[0]
  if exam_result['label']=='NEGATIVE':
    text_result = config['negative_text']
  elif exam_result['label']=='POSITIVE':
    text_result = config['positive_text']
  else: text_result = config['neutral_text']
  return text_result
