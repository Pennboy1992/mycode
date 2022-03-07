#!usr/bin/env python3
import random
def getCard():
  nums = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
  suits = ['Hearts','Diamonds','Clubs','Spades']
  cards = []

  for suit in suits:
    for num in nums:
      cards.append({suit: num})

  return random.choice(cards)


def main():
  print(getCard())
  print(getCard())

main()
