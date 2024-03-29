# Marriage License Generator
_by Gary Pang, "CodeWritingCow"_

## What It Does
This Python program produces a txt file of new marriage licenses for newspaper publication. I was a reporter, and I wrote the program back in 2014 to make my job easier.

## How It Works
It opens a txt file (ex. marriages_2014-05-01.txt) with information like this:

Kevin Allen Kerlish; 1201 E. Second St., Berwick; Michael Kerlish; Cynthia Kerlish; Jenna Elaine Szymaszek; Nanticoke; Michael Smith; Heather Szymaszek
William Charles Little; 359 Fisher Ave., Catawissa; Charles Little; Jane Little; Danielle Nikole Presto; same; Karen Lou Presto; the late Anthony Howard Presto

And makes a new txt file (marriages_2014-05-01_list.txt) like this:

* Kevin Allen Kerlish, 1201 E. Second St., Berwick, son of Michael Kerlish and Cynthia Kerlish, 
and Jenna Elaine Szymaszek, Nanticoke, daughter of Michael Smith and Heather Szymaszek
* William Charles Little, 359 Fisher Ave., Catawissa, son of Charles and Jane Little, 
and Danielle Nikole Presto, same, daughter of Karen Lou Presto and the late Anthony Howard Presto

(When the program starts, it asks user to type a txt file's name. In this example, type "marriages_2014-05-01".)

## Requirements
Someone must visit the local courthouse, read each new marriage license, and write a txt with the following info:

groom; groom_address; groom_dad; groom_mom; bride; bride_address; bride_dad; bride_mom
groom; groom_address; groom_dad; groom_mom; bride; bride_address; bride_dad; bride_mom
groom; groom_address; groom_dad; groom_mom; bride; bride_address; bride_dad; bride_mom ...

Each field must be separated by a semicolon. Each new license must be in one paragraph (see example above.) Avoid extra breaks before and after each paragraph (watch that "enter" key!) Otherwise, you'll get an error message.


## Things to Work on
* Pennsylvania legalized same-sex marriage in May 2014. Program still writes "groom, son of ..." and "bride, daughter of ..." I might add options for users to tell the program whether if a couple is gay or lesbian.

* Add codes to the program, so it won't throw an error when there are extra paragraph breaks.
