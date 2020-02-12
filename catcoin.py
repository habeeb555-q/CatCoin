#import libraries
import hashlib as hasher
from datetime import date, time, datetime
import random

#define an object of a catblock
class CatBlock:

  def __init__(self, index, time, foodAmount, previousCatBlockHash):
    self.index = index
    self.time = time
    self.foodAmount = foodAmount
    self.previousHash = previousCatBlockHash
    self.currentHash = self.getHash()

  def getHash(self):
  	sha = hasher.sha256()
  	sha.update(str(self.index).encode('utf-8') + str(self.time).encode('utf-8') + str(self.foodAmount).encode('utf-8') + str(self.previousHash).encode('utf-8'))
  	return sha.hexdigest()

    #Generate the first block
def catGenesisBlock():
  return CatBlock(0, datetime.now(), "Genesis Block", "0")

def createNextBlock(lastBlock):
  index = lastBlock.index + 1
  time = datetime.now()
  foodAmount = "Cat has " + str(random.randint(1, 500)) + " grams of food left"
  previousHash = lastBlock.currentHash
  return CatBlock(index, time, foodAmount, previousHash)

def visualiseBlockChain(blockChain):
  for i in range(0, len(blockChain)):
    text = ["Block: " + str(blockChain[i].index), blockChain[i].foodAmount, str(blockChain[i].time)]
    maxlen = max(len(s) for s in text)
    colwidth = maxlen + 2
    print('+' + '-'*colwidth + '+')
    for s in text:
      print('| %-*.*s |' % (maxlen, maxlen, s))
      print('+' + '-'*colwidth + '+')
      print('            |')

blockChain = [catGenesisBlock()]
i=1
for i in range(10):
  blockChain.append(createNextBlock(blockChain[-1]))

visualiseBlockChain(blockChain)
