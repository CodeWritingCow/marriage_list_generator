Marriage License Generator, v1.2
A Python Program by Gary Pang, "CodeWritingCow"


---------- WHAT IT DOES ----------
This app produces a txt file of new marriage licenses for newspaper publication. (I'm a reporter/page designer).


---------- HOW IT WORKS ----------
It opens a txt file (ex. marriages_2014-05-01.txt) with information like this:

Kevin Allen Kerlish; 1201 E. Second St., Berwick; Michael Kerlish; Cynthia Kerlish; Jenna Elaine Szymaszek; Nanticoke; Michael Smith; Heather Szymaszek
William Charles Little; 359 Fisher Ave., Catawissa; Charles Little; Jane Little; Danielle Nikole Presto; same; Karen Lou Presto; the late Anthony Howard Presto

And makes a new txt file (marriages_2014-05-01_list.txt) like this:

• Kevin Allen Kerlish, 1201 E. Second St., Berwick, son of Michael Kerlish and Cynthia Kerlish, 
and Jenna Elaine Szymaszek, Nanticoke, daughter of Michael Smith and Heather Szymaszek
• William Charles Little, 359 Fisher Ave., Catawissa, son of Charles and Jane Little, 
and Danielle Nikole Presto, same, daughter of Karen Lou Presto and the late Anthony Howard Presto

(When the app starts, it asks user to type a txt file's name. In this example, type "marriages_2014-05-01".)


---------- REQUIREMENTS ----------
Someone must visit the local courthouse, read each new marriage license, and write a txt with the following info:

groom; groom_address; groom_dad; groom_mom; bride; bride_address; bride_dad; bride_mom
groom; groom_address; groom_dad; groom_mom; bride; bride_address; bride_dad; bride_mom
groom; groom_address; groom_dad; groom_mom; bride; bride_address; bride_dad; bride_mom ...

Each field must be separated by a semicolon. Each new license must be in one paragraph (see example above.) Avoid extra breaks before and after each paragraph (watch that "enter" key!) Otherwise, you'll get an error message.


---------- THINGS TO WORK ON ----------
• Pennsylvania just legalized same-sex marriage this month. App still writes "groom, son of ..." and "bride, daughter of ..." My local county courthouse just issued the first license to a gay couple, and I had to manually rewrite the final txt. Maybe I can add options telling the app if a couple is gay or lesbian.

• Add codes to the app, so it won't throw an error when there are extra paragraph breaks (see REQUIREMENTS above).


- Gary Pang, May 31, 2014