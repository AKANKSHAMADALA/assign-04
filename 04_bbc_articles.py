# bbc articles   
# concept: dictionary and files

'''
You will be given a list of bbc files as list and a searh_key

Build a dictionary with word as keys and value as a list of bbc file names in which the word is present.

for example if "people" is passed as search key it should be able to return a list of filenames like ["bb1.txt", "bb2.txt", "bbc4.txt"] because "people" word is present in all the listed files. 

Now you can imagine that your dictionary should contain each word as key and values should be a list of filenames in which it exists
'''

import unittest
def bbc_articles(filenames, search_key):
  # Delete the bellow line and write your implementation
  l=[]
  for i in filenames:
    f=open(i,'r')
    x=f.read()
    y=x.split()
    if search_key in y:
      l.append(i)
    f.close()
  return l
        
# don't touch the code bellow

class Unit_test(unittest.TestCase):
  def test_01(self):

    search_key = "people"
    
    self.assertEqual(bbc_articles(["bbc1.txt", "bbc2.txt", "bbc3.txt", "bbc4.txt"], search_key), ["bbc1.txt", "bbc2.txt", "bbc4.txt"])

  def test_02(self):

    search_key = "critical"
    
    self.assertEqual(bbc_articles(["bbc1.txt", "bbc2.txt", "bbc3.txt", "bbc4.txt"], search_key), ["bbc3.txt", "bbc4.txt"])
 

if __name__ == '__main__':
  unittest.main(verbosity=2)
