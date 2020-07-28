#Encript Function
def caesar_encript(txt,shift):
  pass
  result=""
  for i in range(len(txt)):
    char = txt[i]
    if(char.isalpha()):
      if(char.isupper()):
        result += chr((ord(char) + shift-65)%26+65)
      else:
        result += chr((ord(char) + shift-97)%26+97)
    else:
      result += char
  return result
    
# Decript Function
def caesar_decript(chiper,shift):
  return caesar_encript(chiper,-shift)
