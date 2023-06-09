import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def remove_space(sentence:str):
  """remove_space

  Args:
      sentence (str): input string

  Returns:
      sentences (str list): split sentence and remove space
  """
  sentences = sentence.split('\n')

  remove_idx = []
  for i in range(len(sentences)):
    if sentences[i] == '':
      remove_idx.append(i)

  actual_idx = 0
  for idx in remove_idx:
    sentences.pop(idx - actual_idx)
    actual_idx += 1
    
  return sentences

def preprocess_sentence(sentence:str, split_ratio:int=3):
  rm_space_li = remove_space(sentence)
  
  remain = len(rm_space_li) % split_ratio
  rm_li_len = len(rm_space_li)
  
  merged_li = []
  for i in range(0, rm_li_len - remain, split_ratio):
      s = ""
      for j in range(i, i+split_ratio):
        s = rm_space_li[j] + "\n"
      merged_li.append(s)
  
  s = ""
  for i in range(rm_li_len - remain, rm_li_len):
    s += rm_space_li[i] + "\n"
  merged_li.append(s)
  
  return merged_li


def text_completion(sentence:str, option:str):
  """text_completion

  Args:
      sentence (str): preprocessed sentence
      option (str): command
        - grammar   : correct grammar
        - naturally : more natural
        - easier    : more easy sentence expression
        - typo      : correct typo

  Returns:
      (openai Object): response
  """
  
  if(option == 'correct'):
    prompt = 'Give me some corrections for these sentences:\n\n' + sentence
  elif(option == 'naturally'):
    prompt = """Can you make it more natural in spoken English?\n
                You can use some fillers and modern words.\n\n""" + sentence
  elif(option == 'easier'):
    prompt = 'Can you make it easier in spoken English?:\n\n' + sentence
  elif(option == 'typo'):
    prompt = """Please let me know if there are any typos that need correcting. 
                If not, don't respond.:\n\n""" + sentence
  else:
    print('[*] Unexpected option. in text_completion()')
    exit(0)
    
  try:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=len(sentence) * 4,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response
    
  except openai.error.RateLimitError:
    print('[*] You exceeded your current quota')
    exit(0)
  except openai.error.APIError:
    print('[*] Bad gateway.')
    exit(0)
    
def get_whisper(sentence:str, option:str):
  out =  text_completion(sentence, option)
  return out["choices"][0]["text"]


if __name__ == '__main__':

  sentence = """
How's it going?

I heard you bought a new MP3 player.
It's the new one from Apple, right?
I'm just thiking of(going to) getting the same one!

so I have some questions for you.

Where did you get it?
On the official website?

Did you get any discounts?
Oh, 10% for new customers until next weekend?
great!

What color do you have?
White? Does it come in black?
Ugh, It's out of stockk right now.
What a bummer.

Do you think it is better than the previous model?
Would you recommend it?

Ok thanks.
That was really helpful.
Talk to you later. Bye.
"""
  out = get_whisper(sentence, "correct")
  print(out)
  