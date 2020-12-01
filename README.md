# christmas_connect_4

All the code for actually playing connect 4 is in core_code.py.  To run, copy all of the contents into a jupyter notebook.  If you're using a juypter/colab notebook, you'll want to run `%matplotlib inline` in a cell as well.  To test the code yourself, type and run `play()`.  This will take user input, rather than use a bot.

**How to use with your bot**

Instead of just running `play()`, you can run `play([test_bot, test_bot])` to have the random test bot play itself.  If you want to test your own bot, just replace one of the test_bot's with your_bot.

**How your bot should work**

Your bot should be a function that takes in the board (a numpy array of 0's where no one has played and either -1 (white) or 1 (black)) and which color it is playing (-1 or 1).  It should return a column number from 0-6 of where it would like to play next.  If your bot returns an invalid row, `play()` will ask it again for a new move.

**Tournament**

Outside of just downloading a connect 4 bot from somewhere else, you can use other dependencies beyond numpy, etc.  Don't exploit bugs (LMK if you find them)--standard connect 4 rules.

Games will be round-robin style, so your bot will play each other bot 100 times.  Since two bots might end up playing the same one or two games over and over again, the 'winner' of each pairing will be the one which wins the majority of the games in that pairing.  Thus if bot_1 wins 51 games against bot_2, that counts as one 'win' for bot_1.  The overall winner is the bot which beats the largest number of other bots.
