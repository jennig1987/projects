print("\nYou awaken in a strange land. There is a field with a lone sheep in it.")

import time

time_duration = 2.5
time.sleep(time_duration)

print('''
             _.%%%%%%%%%%%%%
            /- _%%%%%%%%%%%%%
           (_ %\|%%%%%%%%%%%%
              %%%$$$$$$$$$$$%
                S%S%%%*%%%%S
            ,,,,# #,,,,,,,##,,,,,
''')



time.sleep(time_duration)

print('''
  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,
  ||  ||  ||  ||  ||| ||  ||  ||  ||  ||
  ||__||__||__||__|||_||__||__||__||__||
  |.--..--..--..--..--..--..--..--..--.|
  ||__||__||__||__|||_||__||__||__||__||
  |.--..--..--..--..--..--..--..--..--.|
  ||  ||  ||  ||  ||| ||  ||  ||  ||  ||
  \\//|\//gnv/\||/|\/\||\\|//\|\|//\|//\\///
      ''')
print(
    "\nYou see a gate to the field and have to decide if you enter the field or go back to sleep. \n"
)

time.sleep(time_duration)

decision = input('Do you open the gate or go back to sleep? Type "open" or "sleep" \n')
decision_lower = decision.lower()
if decision_lower == "open":
  time.sleep(time_duration)

  print("\nNow that you have entered the field through the gate you are greeted by the sheep.")

  time.sleep(time_duration)

  print('''
             _.%%%%%%%%%%%%%
            /- _%%%%%%%%%%%%%
           (_ %\|%%%%%%%%%%%%
              %%%$$$$$$$$$$$%
                S%S%%%*%%%%S
            ,,,,# #,,,,,,,##,,,,,
     ''')

  time.sleep(time_duration)

  print('\nThe sheep says "Hi! My name is Shaun."')

  time.sleep(time_duration)

  print("\nYou are surprised the sheep can talk. \n")

  time.sleep(time_duration)

  decision = input('Do you reply? Type "yes" or "no" \n')
  decision_lower = decision.lower()

  if decision_lower == "yes":
    print('\nYou say "Hi, Shaun."')
	
    time.sleep(time_duration)
	
    print("\nShaun asks if you want to follow him to the best yarn store in the land.")
	
    time.sleep(time_duration)
	
    decision = input('\nDo you follow Shaun? Type "yes" or "no" \n')
    decision_lower = decision.lower()
	
    if decision_lower == "yes":
        
      print("\nShaun leads you to the yarn store and you have a magical time and leave with all the yarn you can carry!!")

      time.sleep(time_duration)

      print('''
            
                                                     ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |Magical Yarn|`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___Store ___|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----..............LGB'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._
            ''')
	
    else:
        print('''
          The ground opens up and you are returned to your dream.
          Not very smart are ya? You missed out on free yarn!
                         _.-._
                        | | | |_
                        | | | | |
                        | | | | |
                      _ |  '-._ |
                      \`\`-.'-._;
                       \    '   |
                        \  .`  /
                         |    |
		      ''')
	
	
  else:
    print('''
          The ground opens up and you are returned to your dream.
          Too bad you didn't stick around.
                         _.-._
                        | | | |_
                        | | | | |
                        | | | | |
                      _ |  '-._ |
                      \`\`-.'-._;
                       \    '   |
                        \  .`  /
                         |    |
      ''')
	  
else:
    print('''
          Goodbye you unimaginative party pooper!
                         _.-._
                        | | | |_
                        | | | | |
                        | | | | |
                      _ |  '-._ |
                      \`\`-.'-._;
                       \    '   |
                        \  .`  /
                         |    |
      ''')
	  
