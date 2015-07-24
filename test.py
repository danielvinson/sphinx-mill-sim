import requests
import random
import pprint

def createSampleDeck():
  deckList = []
  for i in range(20):
    deckList.append('Mountain')
  for i in range(40):
    deckList.append('Lightning Bolt')
  return deckList

def shuffle(deckList):
  # This could potentially be improved
  return random.shuffle(deckList)

def getCard(cardName):
  try:
    r = requests.get('http://api.mtgapi.com/v2/cards?name='+cardName)
    return r.json()
  except:
    return False

def sharedColors(cardName1, cardName2):
  # Inputs should be names of cards
  # Ex. sharedColors('Lightning Bolt','Ancestral Recall')
  card1 = getCard(cardName1)
  card2 = getCard(cardName2)
  if card1['cards'][0]['colors'] and card2['cards'][0]['colors']:
    for color in card1['cards'][0]['colors']:
      if card2['cards'][0]['colors'].__contains__(color):
        return True
  return False

def runSimulation(deck):
  numTrials = 1
  trialResults = []
  for trial in range(numTrials):
    testDeck = deck[:] # Slice to create a copy instead of a reference to the original
    activationCount = 1
    shuffle(testDeck)
    while len(testDeck) > 0:
      print testDeck
      if sharedColors(testDeck[0],testDeck[1]):
        del testDeck[0:2]
        continue
      else:
        del testDeck[0:2]
        activationCount += 1
        continue
    print activationCount
    trialResults.append(activationCount)
  return trialResults

runSimulation(createSampleDeck())