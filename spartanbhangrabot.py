from argparse 				import ArgumentParser
from snapchat_bots 			import SnapchatBot
from threading 				import Thread
from random 				import randint
from snapchat_bots.utils 	import save_snap

import time

members = ['ishaant']
friends = []

class SpartanBhangraBot(SnapchatBot):

	def delaymarkviewed(self, snap):
		t = randint(10, 30)
		time.sleep(t)
		self.mark_viewed(snap)

	def delaypoststory(self, snap):
		t = randint(10, 15)
		time.sleep(t)
		self.post_story(snap)

	def delayaddfriend(self, friend):
		print("thread got message to" + "add friend")
		t = randint(3, 10)
		time.sleep(t)
		self.add_friend(friend)
		self.send_snap(friend, Snap.from_file("res/sb.png"))

	## Important listeners
	def on_snap(self, sender, snap):
		print(members)
		save_snap(snap, 'snaps/' + str(sender))
		print(sender)
		if sender in members:
			print(sender)
			self.send_snap(sender, snap)
			self.delaypoststory(snap)
			self.delaymarkviewed(snap)

	def on_friend_add(self, friend):
		print("Friend %s tryna add me", friend)
		self.delayaddfriend(friend)

	def on_friend_delete(self, friend):
		self.delete_friend(friend)	


if __name__ == '__main__':
	parser = ArgumentParser("Spartan Bhangra")
	parser.add_argument('-u', '--username', required=True, type=str)
	parser.add_argument('-p', '--password', required=True, type=str)
	args = parser.parse_args()

	bot = SpartanBhangraBot(args.username, args.password)
	bot.listen()