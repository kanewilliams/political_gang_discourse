import re
import os

def split_by_regex(text):
  paragraph_regex = r"(?:\r?\n){2,}|^\s*$\n"
  paragraphs = re.split(paragraph_regex, text, flags=re.MULTILINE)
  return paragraphs

def split_into_key_value(text):
  regex = r"(.*?)\s*\((.*?)\)"
  match = re.match(regex, text)

  if match:
    key = match.group(1).strip()
    value = match.group(2).strip()
    return key, value
  else:
    return None, None  

def remove_number_before_text(text):
  regex = r"^\d+\.\s*"  
  return re.sub(regex, "", text).strip()  

def write_to_file2(filename, content):
  with open(filename, 'w', encoding="utf-8") as f:
    f.write(content)

    
labour_mps = {
    "GINNY ANDERSEN": "LABOUR",
    "CAMILLA BELICH": "LABOUR",
    "GLEN BENNETT": "LABOUR",
    "RACHEL BOYACK": "LABOUR",
    "RACHEL BROOKING": "LABOUR",
    "REUBEN DAVIDSON": "LABOUR",
    "BARBARA EDMONDS": "LABOUR",
    "SHANAN HALBERT": "LABOUR",
    "PEENI HENARE": "LABOUR",
    "CHRIS HIPKINS": "LABOUR",
    "WILLIE JACKSON": "LABOUR",
    "INGRID LEARY": "LABOUR",
    "JO LUXTON": "LABOUR",
    "KIERAN MCANULTY": "LABOUR",
    "TRACEY MCLELLAN": "LABOUR",
    "DAMIEN O'CONNOR": "LABOUR",
    "GREG O'CONNOR": "LABOUR",
    "DAVID PARKER": "LABOUR",
    "WILLOW-JEAN PRIME": "LABOUR",
    "PRIYANCA RADHAKRISHNAN": "LABOUR",
    "ADRIAN RURAWHE": "LABOUR",
    "DEBORAH RUSSELL": "LABOUR",
    "JENNY SALES": "LABOUR",
    "CARMEL SEPULONI": "LABOUR",
    "LEMAUGA LYDIA SOSENE": "LABOUR",
    "CUSHLA TANGAERE-MANUEL": "LABOUR",
    "JAN TINETTI": "LABOUR",
    "PHIL TWYFORD": "LABOUR",
    "TANGI UTIKERE": "LABOUR",
    "AYESHA VERRALL": "LABOUR",
    "DUNCAN WEBB": "LABOUR",
    "HELEN WHITE": "LABOUR",
    "ARENA WILLIAMS": "LABOUR",
    "MEGAN WOODS": "LABOUR",
    "MILES ANDERSON": "NATIONAL",
    "CARL BATES": "NATIONAL",
    "ANDREW BAYLY": "NATIONAL",
    "DAN BIDOIS": "NATIONAL",
    "CHRIS BISHOP": "NATIONAL",
    "CAMERON BREWER": "NATIONAL",
    "SIMEON BROWN": "NATIONAL",
    "GERRY BROWNLEE": "NATIONAL",
    "MIKE BUTTERICK": "NATIONAL",
    "HAMISH CAMPBELL": "NATIONAL",
    "CARLOS CHEUNG": "NATIONAL",
    "JUDITH COLLINS": "NATIONAL",
    "TIM COSTLEY": "NATIONAL",
    "MATT DOOCEY": "NATIONAL",
    "GREG FLEMING": "NATIONAL",
    "PAULO GARCIA": "NATIONAL",
    "PAUL GOLDSMITH": "NATIONAL",
    "NICOLA GRIGG": "NATIONAL",
    "RYAN HAMILTON": "NATIONAL",
    "DANA KIRKPATRICK": "NATIONAL",
    "BARBARA KURIGER": "NATIONAL",
    "MELISSA LEE": "NATIONAL",
    "NANCY LU": "NATIONAL",
    "CHRIS LUXON": "NATIONAL",
    "DAVID MACLEOD": "NATIONAL",
    "GRANT MCCALLUM": "NATIONAL",
    "TODD MCCLAY": "NATIONAL",
    "JAMES MEAGER": "NATIONAL",
    "MARK MITCHELL": "NATIONAL",
    "JOSEPH MOONEY": "NATIONAL",
    "RIMA NAKHLE": "NATIONAL",
    "KATIE NIMON": "NATIONAL",
    "CHRIS PENK": "NATIONAL",
    "TAMA POTAKA": "NATIONAL",
    "MAUREEN PUGH": "NATIONAL",
    "SUZE REDMAYNE": "NATIONAL",
    "SHANE RETI": "NATIONAL",
    "TOM RUTHERFORD": "NATIONAL",
    "PENNY SIMMONDS": "NATIONAL",
    "SCOTT SIMPSON": "NATIONAL",
    "STUART SMITH": "NATIONAL",
    "ERICA STANFORD": "NATIONAL",
    "SAM UFFINDELL": "NATIONAL",
    "LOUISE UPSTON": "NATIONAL",
    "TIM VAN DE MOLEN": "NATIONAL",
    "SIMON WATTS": "NATIONAL",
    "CATHERINE WEDD": "NATIONAL",
    "VANESSA WEENINK": "NATIONAL",
    "NICOLA WILLIS": "NATIONAL",
    "STEVE ABEL": "GREEN",
     "KAHURANGI CARTER": "GREEN",
     "MARAMA DAVIDSON": "GREEN",
     "JULIE ANNE GENTER": "GREEN",
     "HŪHANA LYNDON": "GREEN",
     "RICARDO MENÉNDEZ MARCH": "GREEN",
     "TAMATHA PAUL": "GREEN",
     "LAN PHAM": "GREEN",
     "JAMES SHAW": "GREEN",
     "CHLÖE SWARBRICK": "GREEN",
     "DARLEEN TANA": "GREEN",
     "TEANAU TUIONO": "GREEN",
     "CELIA WADE-BROWN": "GREEN",
     "SCOTT WILLIS": "GREEN",
     "LAWRENCE XU-NAN": "GREEN",
     "MARK CAMERON": "ACT",
     "KAREN CHHOUR": "ACT",
     "SIMON COURT": "ACT",
     "ANDREW HOGGARD": "ACT",
     "CAMERON LUXTON": "ACT",
     "NICOLE MCKEE": "ACT",
     "PARMJEET PARMAR": "ACT",
     "DAVID SEYMOUR": "ACT",
     "TODD STEPHENSON": "ACT",
     "LAURA TRASK": "ACT",
     "BROOKE VAN VELDEN": "ACT",
     "JAMIE ARBUCKLE": "NZ FIRST",
     "CASEY COSTELLO": "NZ FIRST",
     "ANDY FOSTER": "NZ FIRST",
     "SHANE JONES": "NZ FIRST",
     "JENNY MARCROFT": "NZ FIRST",
     "MARK PATTERSON": "NZ FIRST",
     "WINSTON PETERS": "NZ FIRST",
     "TANYA UNKOVICH": "NZ FIRST",
}

def check_mp_party(name, party):
    name = name.upper()
    #print(name)
    if name in labour_mps:
        if labour_mps[name] == party:
            #print(labour_mps[name])
            return True
        else:
            #print(party)
            return False
    return False 

import string

def remove_left_symbols(text):
  """
  This function removes non-alphanumeric characters and whitespace from the left side of a string.

  Args:
      text: The string to be processed.

  Returns:
      The string with non-meaningful symbols removed from the left side.
  """
  start = 0
  for char in text:
    if char in string.printable and not char.isspace():
      break
    start += 1
  return text[start:]

def clean_text(text):
  """
  This function removes repeated spaces, removes the space before "(", 
  and removes non-meaningful symbols from the left side of a string.

  Args:
      text: The string to be processed.

  Returns:
      The cleaned string.
  """
  text = text.strip()  # Remove leading/trailing whitespace first
  text = re.sub(r"\s+", " ", text)  # Remove repeated spaces
  text = re.sub(r"\s\)", ")", text)  # Remove space before "("
  text = re.sub(r"\s:", ":", text)  # Remove space before ":"
  return text

def split_one_text(text, filename):
    #these two patterns split one line into speakers (if there is a text with one line)
    pattern = r'(?<=[.?!])\s*(?=(?:\b\w+\b\s*){0,12}:)'
    text = re.sub(pattern, r"\n\n", text)

    pattern = r"^(.*?)(?::)"
    
    paragraphs = (split_by_regex(text))

    newtext = ""
    for paragraph in paragraphs:
        paragraph = remove_left_symbols(paragraph)
        paragraph = clean_text(paragraph)
        if paragraph[0] == ":":
            newtext += paragraph  
        else:
            newtext += "\n\n" + paragraph
    text = newtext        
    pattern = r'(?<!^)(?=\b[A-Z]{3,}(?:\s[A-Z]{3,})+\b)'
    text = re.sub(pattern, r"\n\n", text)

    pattern = r"^(.*?)(?::)"
    
    paragraphs = (split_by_regex(text))
    speaker_party = {}
    speaker_text = {}
    current_speaker = "default"
    speaker_text[current_speaker] = ""
    current_text = ""
    
    for paragraph in paragraphs:
      if paragraph.endswith("Hon "):
        paragraph = paragraph[:-4] 
      matches = re.findall(pattern, paragraph, flags=re.DOTALL)  
      current_text = paragraph
      if len(matches) != 0 :
          #this length should work
          if len(matches[0]) < 65:
              current_text = paragraph[len(matches[0])+2:]
              key, value = split_into_key_value(matches[0])
              # if we can split it into two parts __some text (some text)__
              if key is not None:
                  current_speaker = remove_number_before_text(key).upper()
                  speaker_party[remove_number_before_text(key).upper()] = value
                  if not(key in speaker_text.keys()):
                      speaker_text[current_speaker] = ""
              else:
                  current_speaker = remove_number_before_text(matches[0]).upper()
                  if not(current_speaker in speaker_text.keys()):
                      speaker_text[current_speaker] = ""
      if speaker_text[current_speaker] == "":                
          speaker_text[current_speaker] += current_text 
      else:
          speaker_text[current_speaker] += "\n" + current_text 


    for speaker, party in speaker_party.items():
       #up = party.upper()
       #check_mp_party
       if party.upper().find("LABOUR") != -1 or check_mp_party(speaker, "LABOUR"):
           write_to_file2("labour/"  + filename[:-4]+ speaker+".txt", speaker_text[speaker])
       elif party.upper().find("NATIONAL") != -1 or check_mp_party(speaker, "NATIONAL"):
           write_to_file2("national/"  + filename[:-4]+ speaker+".txt", speaker_text[speaker])
       elif party.upper().find("GREEN")  != -1 or check_mp_party(speaker, "GREEN"):
           write_to_file2("green/"  + filename[:-4]+ speaker+".txt", speaker_text[speaker])
       elif party.upper().find("ACT") != -1 or check_mp_party(speaker, "ACT"):
           write_to_file2("act/"  + filename[:-4]+ speaker+".txt", speaker_text[speaker])
       else:
           write_to_file2("other/" + filename[:-4]+ speaker+".txt", speaker_text[speaker])

directory = 'files'
 

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    #print(filename)
    if os.path.isfile(f):
        try:
            with open(f, 'r', encoding="utf8") as file:
                file_content = file.read()
                split_one_text(file_content, filename)
         
        except FileNotFoundError:
            print(f"File '{f}' not found.")
        except Exception as e:
            print(f"File '{f}' An error occurred: {e}")
        





