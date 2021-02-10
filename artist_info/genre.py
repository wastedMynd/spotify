# import
import requests


def get_genre_by(artist):
  with requests.get('https://www.google.com') as responce:
    print(responce.ok)


if __name__=='__main__':
  get_genre_by('James Blunt')
