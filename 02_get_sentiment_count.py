# counting positive and negative words in a text 
#concept: dictionaries and files

'''
You will be given a file with a content.

Your task is to count the number of positives and number of negatives and return the number which is asked for.

In the below code you will be given a function get_sentiment_count(filename, sentiment_type) where filename is the text file containing the content and sentiment_type is the negative or positive count that you have to return

A dictionary with positive and negative words are given in the program. you can use that

sentiment_type will contain either "negative" or "positive".

'''

import unittest

def get_sentiment_count(filename, sentiment_type):
  sentiment_words = {
    "negative":["aggressive","hostile","bad""good","excellent","beloved",,"against","rediculous","targeted","offended","offend","force","forceful","forcefully","annoyed","foolish","illogical","cheos"],
    "positive": ["adore","benevolent","developed","pride","proud","celebratory","optimistic","cheery"]
  }

  # Delete the bellow line and write your implementation
  f=open(filename,'r')
  c=0
  x=f.read()
  y=x.split()
  for i,j in sentiment_words.items():
    if(i==sentiment_type):
      z=j
      for a in y:
        for b in z:
          if(a==b):
            c+=1
  f.close()
  return c

  
# don't touch the code bellow

class Unit_test(unittest.TestCase):
  def test_01(self):
    
    self.assertEqual(get_sentiment_count("news_article.txt","positive"), 10)

  def test_02(self):
    self.assertEqual(get_sentiment_count("news_article.txt","negative"), 12)


if __name__ == '__main__':
  unittest.main(verbosity=2)
