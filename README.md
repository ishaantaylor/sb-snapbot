# sb-snapbot
Snapchat Bot using agermanidis/SnapchatBot for Spartan Bhangra, my Bhangra team, that aggregates the members' snaps and displays them to the public.

## The Aggregator Bot has the following functionality:

1. Uploads snaps it is sent by usernames in `members.txt` to its story (viewable by only the bot's friends)
2. Adds back only usernames in a contiually updatable list of friends, `audience.txt`, and then sends a snap to the new friend
3. Marks receiving snaps viewed and sends back the same snap to verify the snap was uploaded without any problems
4. Saves snaps in specified folder `snaps/<username>`


