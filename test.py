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


def text_completion(sentences:list, option:str):
  """text_completion

  Args:

  Returns:
  """
  if(option == 'correct'):
    prompt = 'Give me some corrections for these sentences:\n\n' + sentences
  elif(option == 'naturally'):
    prompt = 'Can you make it more natural in spoken English?:\n\n' + sentences
  elif(option == 'easier'):
    prompt = 'Can you make it easier?:\n\n' + sentences
  else:
    print('[*] Unexpected option. in text_completion()')
    exit(0)
    
  try:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response
    
  except openai.error.RateLimitError:
    print('[*] You exceeded your current quota')
    exit(0)



sentence = """
How's it going?

I heard you bought a new MP3 player.
It's the new one from Apple, right?
I'm just thiking of(going to) getting the same one~~~
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
That was really helpful

Talk to you later. Bye
"""
sentences = remove_space(sentence)
print(sentences)

# ret = text_completion(sentences, 'naturally')
# print(ret)
# print(sentences)