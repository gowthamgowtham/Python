#!/usr/bin/python3
import unicodedata

# https://stackoverflow.com/a/6806203/252489 - Devanagari algorithm, worked well for kannada too :)
def kannada_split(line):
  virama = u'\N{KANNADA SIGN VIRAMA}'
  cluster = ''
  last = None
  for c in line:
    cat = unicodedata.category(c)[0]
    if cat == 'M' or cat == 'L' and last == virama:
      cluster += c
    else:
      if cluster:
        yield cluster
      cluster = c
    last = c
  if cluster:
    yield cluster

def get_second_letter(line):
  g = kannada_split(line)
  next(g)
  return next(g)

def find_praasa(poem):
  praasa = ''
  for line in poem.split('\n'):
    praasa = find_overlap(praasa, get_second_letter(line))
    if praasa == '':
      return "No praasa"
  return praasa

def find_overlap(current, next):
  if current == '':
    return next
  overlap = ''
  for i in range(0, min(len(current), len(next))):
    if current[i] == next[i]:
      overlap += current[i]
    else:
      break
  return overlap

poems = [
'''ಸತಿಯನೊಲ್ಲೆನು ಬ್ರಹ್ಮಚರ್ಯ
ಸ್ಥಿತಿಗೆ ತಪ್ಪುವನಲ್ಲ ನೀವನು 
ಚಿತವ ನೆನೆದರೆ ನಡೆಯಿ ಕೊಟ್ಟೆನು ಕಾಳಗವ ನಿಮಗೆ 
ವ್ರತದನಿಧಿ ಕುರುಭೂಮಿಯಲಿ ಶರ
ತತಿಯಲಿಪ್ಪತ್ತೊಂದು ದಿನ ಭೃಗು
ಸುತನೊಡೆನೆ ಕಾದಿದನು ವಿರಥನ ಮಾಡಿದನು ಭೀಷ್ಮ''',

'''ಸರ್ಪಯಜ್ಞದಲಾದ ದುರಿತದ
ದರ್ಪವನು ಕೆಡೆಬೀಳಲೊದೆಯಲು
ತರ್ಪಣಾದಿ ಕ್ರಿಯೆಗಳಲಿ ಸಾಮರ್ಥ್ಯವಿಲ್ಲೆಂದು
ದರ್ಪಕಾಹಿತ ಮೂರ್ತಿ ಮುನಿಮುಖ
ದರ್ಪಣನು ಶಿಷ್ಯನನು ಕರೆದು ಸ
ಮರ್ಪಿಸಿದನರಸಂಗೆ ವೇದವ್ಯಾಸಮುನಿರಾಯ''',

'''ರಾಯ ಚಿತ್ತೈಸೆಂದು ವೈಶಂ
ಪಾಯಮುನಿ ಹೇಳಿದನು ಕಮಲದ
ಳಾಯತಾಕ್ಷನ ಬಾಲಕೇಳಿ ವಿಧೂತ ಕಿಲ್ಬಿಷವ
ಕಾಯ ಕಲ್ಮಷಹರವಖಿಳ ನಿ
ಶ್ರೇಯಸದ ಸದ್ರೂಪುವಿನ ಸಂ
ದಾಯಕವ ನಿರ್ಮಲ ಮಹಾಭಾರತ ಕಥಾಮೃತ''',

'''ಜಾತಿ ಹೀನನ ಮನೆಯ ಜ್ಯೋತಿತಾ ಹೀನವೇ ?
ಜಾತಿ - ವಿಜಾತಿ ಏನಬೇಡ, ದೇವನೊಲಿ
ದಾತದೆ ಜಾತಾ , ಸರ್ವಜ್ಞ''',

'''ಮಂಡೆಬೋಳಾದೊಡಂ, ದಂಡ ಕೊಲ್ಪಿಡಿದೊಡಂ
ಹೆಂಡತಿಯ ಬಿಟ್ಟು ನಡೆದೊಡಂ, ಗುರುಮುಖವು
ಕಂಡಿಲ್ಲದಿಲ್ಲ ಸರ್ವಜ್ಞ''',

'''ಕಣ್ಣು , ನಾಲಿಗೆ, ಮನವು ತನದೆಂದನ್ನಬೇಡ
ಅನ್ಯರನು ಕೊಂದರೆನಬೇಡ, ಇವು ಮೂರು
ತನ್ನನ್ನೇ ಕೊಲ್ಲವುವು - ಸರ್ವಜ್ಞ''',

'''ಕಲ್ಲುಕಲ್ಲೆಂಬುವಿರಿ, ಕಲ್ಲೋಳಿಪ್ಪುದೆ ದೈವ ?
ಕಲ್ಲಲ್ಲಿ ಕಳೆಯ ನಿಲಿಸಿದ, ಗುರುವಿನ
ಸೊಲ್ಲಲ್ಲೇ ದೈವ, ಸರ್ವಜ್ಞ'''
]

for poem in poems:
  print(find_praasa(poem))