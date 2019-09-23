# sb-snapbot
Snapchat Bot using agermanidis/SnapchatBot for Spartan Bhangra, my Bhangra team, that aggregates the members' snaps and displays them to the public. Also supports private group story.

## The Aggregator Bot has the following functionality:

- Uploads snaps it is sent by usernames in `members.txt` to its story (viewable by only the bot's friends)
- Adds back only usernames in a contiually updatable list of friends, `audience.txt`, and then sends a snap to the new friend
- Marks receiving snaps viewed and sends back the same snap to verify the snap was uploaded without any problems
- Saves snaps in specified folder `snaps/<username>`


