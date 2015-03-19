from argparse 				import ArgumentParser
from snapchat_bots 			import SnapchatBot, Snap
from threading 				import Thread
from random 				import randint

import time


def getDelimitedArray(file):
	with open(file) as f:
		return [line.rstrip('\n') for line in f]

class Agregator(SnapchatBot):

	# helper methods to delay these actions
	def delaymarkviewed(self, snap):
		t = randint(10, 30)
		time.sleep(t)
		self.mark_viewed(snap)

	def delaypoststory(self, snap):
		t = randint(8, 10)
		time.sleep(t)
		self.post_story(snap)

	def delayaddfriend(self, friend):
		t = randint(2, 3)
		time.sleep(t)
		self.add_friend(friend)
		self.send_snap(friend, Snap.from_file("res/sb.png"))

	## Important listeners
	def on_snap(self, sender, snap):
		snap.save(dir_name='snaps/' + str(sender))
		if sender in getDelimitedArray('members.txt'):
			print(sender)
			self.delaypoststory(snap)
			self.send_snap(sender, snap)
			self.delaymarkviewed(snap)

	def on_friend_add(self, friend):
		print("Friend %s tryna add me", friend)
		if friend in getDelimitedArray('audience.txt') or friend in getDelimitedArray('members.txt'):
			self.delayaddfriend(friend)

	def on_friend_delete(self, friend):
		self.delete_friend(friend)	


if __name__ == '__main__':
	# accepts command line arguments `python spartanbhangrabot.py -u username -p password`
	parser = ArgumentParser("Agregator")
	parser.add_argument('-u', '--username', required=True, type=str)
	parser.add_argument('-p', '--password', required=True, type=str)
	args = parser.parse_args()

	bot = Agregator(args.username, args.password)
	bot.listen(60)