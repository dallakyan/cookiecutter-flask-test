from ntpath import join
from app.blog.models import Post

# from https://stackoverflow.com/questions/18834636/random-word-generator-python
import requests
import random
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.content.splitlines()
len_words = len(words)

from app.app import create_app
app = create_app()
with app.app_context():
    for i in range(20):
        title = ' '.join([words[random.randint(0, len_words)].decode('utf8').title() for j in range(5)] )
        message = ' '.join([words[random.randint(0, len_words)].decode('utf8').title() for j in range(20)] )
        post = Post(title=title, message=message)
        post.save()

