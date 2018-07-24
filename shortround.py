from errbot import BotPlugin, botcmd
from random import seed
from random import choice

# seed rando generator
seed(1)

class ShortRoundPlugin(BotPlugin):
  """ShortRound plugin for Errbot"""

  def lines(self):
    lines = [
      "Diamonds? Diamonds!",
      "Dr. Jones! No more parachutes!",
      "Haha! Very funny! Haha! All wet!",
      "Hang on, lady. We going for a ride.",
      "He no nuts. He crazy!",
      "Hey! You cheat, Dr. Jones! You cheat!",
      "Hey, Dr. Jones, no time for love! We've got company!",
      "Hey, lady! You call him Dr. Jones!",
      "I keep telling you, you listen to me more, you live longer!",
      "I step on something. Feels like I step on fortune cookies.",
      "I very little, you cheat very big!",
      "Indy!!!! Cover your heart!!!!!",
      "Indy, I love you! Wake up, Indy! Wake up!",
      "It wasn't me. It's her!",
      "Maybe he like OLDER women!",
      "No Indy! The left tunnel! The left! Indy!",
      "Okey dokey, Dr. Jones. Hold on to your potatoes!",
      "Strong bridge! Strong wood! Aaarrghhhh!!!",
      "Tell me later what happen.",
      "That's no cookie!",
      "They crash the plane to make you come here?",
      "Three aces! I win! Two more games, I have all your money! Ha, ha, ha!",
      "Very funny! Very funny! ...Uh oh!",
      "What is Sankara?",
      "Wow! Holy Smoke! Crash landing!",
      "You call him Doctor Jones, doll!",
      "You make me poor! No fun! Playing with you no fun!",
      "You say to stand against the wall. Not my fault. Not my fault!"
    ]
    return lines

  @botcmd
  def quote(self, msg, args):
    """random movie quote"""
    return choice(self.lines())


