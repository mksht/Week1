# Command Line Workflow: Star Wars

## Spoilers: Star Wars Episode IV: A New Hope
* This exercise contains spoilers for the 1977 film Star Wars (retitled as "Star Wars: Episode IV: A New Hope). While it has been over four decades, you have been warned.

## Problem Description
* Navigating your computer through terminal is an extremely important, practically required skill to be a programmer. The following is an assignment where you will make / delete folders and files to help you get used to navigating your terminal and manipulating your files with bash commands. Perform all commands within the *solution* directory (there is no `solution.py` here, you'll be creating all necessary files.)

### Use bash to perform the following commands, in order:
* Navigate into the "star_wars" folder
# $cd 3_star_wards
* Create a folder called "the_empire"
# $mkdir the_empire
* Create a folder called "the_rebellion"
# $mkdir the_rebellion
* Make the following folders
# $mkdir tatooine millenium_falcon death_star x_wing tie_fighter
	* "tatooine"
	* "millenium_falcon"
	* "death_star"
	* "x_wing"
	* "tie_fighter"
* Make the following text files (.txt) ***Make Sure to have the .txt extension on these files***
# $touch luke_skywalker.txt old_man_ben.txt han_solo.txt chewbacca.txt leia_organa.txt darth_vader.txt emperor_palpatine.txt
	* "luke_skywalker"
	* "old_man_ben"
	* "han_solo"
	* "chewbacca"
	* "leia_organa"
	* "darth_vader"
	* "emperor_palpatine"
* Open the darth_vader text file and add the text "Darth Vader"
# $ cat > darth_vader.txt
# Darth Vader
#press Ctrl+D to finish writing task.
	* **Bonus points** if you add the text without opening the file
# $ echo "Darth Vader" >> darth_vader.txt
# $ sed '$ a\
# > added lineeee' darth_vader.txt
#use sed '$ a\ if want to add after the last line' darth_vader.txt but it doesn't save because it's not modifying the source file. use sed -i to modify the source file. or don't use it and just use the output to rewrite the file.
# $ sed '/^a/d' darth_vader.txt  
#-> here you delete line that starts with character "a" using /d
# $ sed -i '/^a/d' darth_vader.txt  
#above is same thing but doing it in source file if you add -i.

* Move the emperor and darth vader into the folder "the_empire"
# $mv emperor_palpatine.txt darth_vader.txt the_empire
* Move "luke_skywalker" and "old_man_ben" to the "tatooine" folder
# $ mv luke_skywalker.txt old_man_ben.txt tatooine     
#-> note that it will move at least the files it finds even if it can't find one/doesn't exist.
* Luke has found out old man ben is actually Obi Wan Kenobi. Change the name of "old_man_ben" to "obi_wan_kenobi"
# $cd tatooine 
#--> note that you should be in that directory where the file is to change it.
# $mv old_man_ben.txt obi_wan_kenobi.txt
* Now they need to escape tatooine. Move "han_solo" and "chewbacca" into "tatooine"
# $cd ..
#--> moves up a directory to be able to reach han_solo and chewbacca files bc they're there.
# $mv han_solo.txt chewbacca.txt tatooine
* While all this is happening the Sith lords are sitting nice and cozy inside their giant metal moon. Move "darth_vader" and "emperor_palpatine" inside the "death_star"
# $mv darth_vader.txt emperor_palpatine.txt ../death_star
#above, using ../death_star to mean that move to death star which is in parent directory
* Back on tatooine the characters get on the fastest ship in the galaxy and take off to save the princess. Move all four files from tatooine into the millenium falcon
# $ mv tatooine/*.txt millenium_falcon
* The princess is also on the death star. Move "leia_organa" to the "death_star"
# $ mv leia_organa.txt death_star
* Our heroes sneak onto the Death Star. Move all the files inside the "millenium_falcon" onto the "death_star" 
# $mv millenium_falcon/*.txt death_star
* They found the princess! but in the process Obi Wan was struck down by Darth Vader. Delete the "obi_wan_kenobi" file 
# $ rm death_star/obi_wan_kenobi.txt
* Our other heroes retreat in anger. Move Luke, Leia, Han, and Chewbacca into the "millenium_falcon"
# $ mv death_star/{luke_skywalker.txt,leia_organa.txt,han_solo.txt,chewbacca.txt} millenium_falcon
* Alright the rebels have regrouped and come up with a plan to destroy the death star. Luke gets into an x-wing to use his sweet piloting skills. Move "leia" into the "the_rebellion" directory. Move Luke into the "x_wing"
#Doesn't work:$ mv -v millenium_falcon/{leia_organa.txt,luke_skywalker.txt} {the_rebellion,x_wing}
#also didn't work: $ echo "/the_rebellion/ /x_wing/" | xargs mv -v /millenium_falcon/{leia_organa.txt,luke_skywalker.txt}
#can try: $ mv -v millenium_falcon/leia_organa.txt the_rebellion && mv -v millenium_falcon/luke_skywalker.txt x_wing

# $ mv -v millenium_falcon/leia_organa.txt the_rebellion
# $ mv -v millenium_falcon/luke_skywalker.txt x_wing
* Vader, also a legendary pilot, gets into the tie fighter to defend the death star. Move "darth_vader" out of the death_star and into the "tie_fighter"
# $ mv death_star/darth_vader.txt tie_fighter
* Luke uses those sweet farm boy desert skills and fires some torpedos into the core of the death star, destroying it. **CAREFULLY** Delete the folder "death_star"
	* Remember that deletion of a directory is a high-stake operation
	* **DO NOT** do this without checking your command for correctness
# $rm -r death_star

## Testing
#didn't work. i tried renaming 3_star_wars to star_wars
# $ cd ..
# $ mv 3_star_wars star_wars
# cd star_wars
#but pytest still failed bc windows file separator was causing error. need to run either modify test_solution file so that it also works in git bash. for now, reinstalled python-pip and pytest through ubuntu so i can run a pytest on ubuntu. it worked.
* to test your solution, type 'pytest' within the **solutions** subdirectory. It will use python to make sure your final directory/file structure is correct.

## Submission
* Submit your answer in the *solution* subdirectory in this directory. Your "answer" will be the structure of the folders/files you created at the end of the exercise
