# Reversing dictionary
# concept: Dictionaries

'''
In this program you will be given an input dictionary and your task is to reverse it

for example take

dict = {"Ram": 12, "Laxman": 12, "Lakshmi": 12, "Vishesh": 8}

the reverse will contain

dict = {12 : ["Ram", "Laxman", "Lakshmi"], 8 : ["Vishesh"]}

meaning that the values are turned into keys and keys are turned into values. When there are multiple keys with same value, they need to grouped.

So in the resulting dictionary, each value is a list, where each list contain one or more words.

'''

import unittest
def reverse(original):
  """
  should create and return a new dictionary where
  the values of the original are now keys!
  """
  reversed_dict = {}
  # Write your code here
  for i,j in original.items():
    l=[]
    for m,n in original.items():
      if j==n:
        l.append(m)
    reversed_dict.update({j:l})

  return reversed_dict



  
# don't touch the code bellow

class Unit_test(unittest.TestCase):
  def test_01(self):
    input = {"Ram": 12, "Laxman": 50, "Lakshmi": 70, "Vishesh": 8}
    output = {12 : ["Ram"], 50 : ["Laxman"], 70 : ["Lakshmi"], 8 : ["Vishesh"]}
    
    self.assertEqual(reverse(input), output)

  def test_02(self):
    input = {"Ram": 12, "Laxman": 12, "Lakshmi": 12, "Vishesh": 8}
    output = {12 : ["Ram", "Laxman", "Lakshmi"], 8 : ["Vishesh"]}
    
    self.assertEqual(reverse(input), output)


if __name__ == '__main__':
  unittest.main(verbosity=2)
