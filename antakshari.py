#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import random

# List of valid letters for kannada antakshari
aksharagalu = ['ಕ','ಖ','ಗ','ಘ','ಙ','ಚ','ಛ','ಜ','ಝ','ಞ',
               'ಟ','ಠ','ಡ','ಢ','ಣ','ತ','ಥ','ದ','ಧ','ನ',
               'ಪ','ಫ','ಬ','ಭ','ಮ','ಯ','ರ','ಲ','ವ','ಶ','ಷ','ಸ','ಹ','ಳ']
# Movie database. Key is movie name, value is incremented if movie is used
movies = {'ಸುಬ್ಬಾಶಾಸ್ತ್ರಿ':0, 'ರಂಗನಾಯಕಿ':0, 'ಕಥಾಸಂಗಮ':0, 'ಮಯೂರ':0, 'ರತ್ನಗಿರಿ ರಹಸ್ಯ':0, 
          'ಯಜಮಾನ':0, 'ನಾಗರಹಾವು':0, 'ವಂಶಿ': 0, 'ಶರಪಂಜರ':0, 'ಯುಗ ಪುರುಷ':0,
          'ಕಿಟ್ಟು ಪುಟ್ಟು':0, 'ಟಗರು':0 }

def get_last_letter(word):
  for letter in reversed(word):
    if letter in aksharagalu:
      return letter
  raise Exception("No suitable letter " + word)

def get_random_movie():
  index = random.randint(0,len(movies)-1)
  movie = list(movies.keys())[index]
  movies[movie] = 1
  return movie

def get_next_movie(letter):
  for movie in movies:
    if movies[movie] == 0 and movie[0] == letter:
      movies[movie] = 1
      return movie
  raise Exception("No next movie for letter " + letter)

def play(max):
  movie = get_random_movie()
  print("First guess", movie)
  count = 0
  while count < max:
    count = count + 1
    last_letter = get_last_letter(movie)
    print("Letter", last_letter)
    movie = get_next_movie(last_letter)
    print("Next movie", movie)
  print('Game over')

play(5)