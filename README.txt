For this project, I am making a program that is a passivization of the input. The program uses Lark to parse the input into a tree. 
The program uses the length of the roots to add the part of the string into an array. Then the program will change the verb and preposition(if needed) of the array.
The program will finally build the array into the passivization of the input string. If it can't build for any reason, then it will output "no valid parse."


The time and the location at the end of the sentence stay there even if "no" switch with the first "no."
If the order at the end is time then location, it will not parse.
The verb will change into past tense.
The verb will also change from the "giving end" to the "receiving end" (gives -> received)
if the preposition is "with" then the proposition will not change.
The preposition will change to by to be in the "receiving end."
	
I run it with python en.py
You can put the text under the Corpus
or you can run it with passive(parser, [your string here])

The order is:
name determination adjective(if you want to add any adjective) animal verb determination thing preposition name determination adjective(if you want to add any adjective) animal (place and time if you want to add here)

You are welcome to add names, things, and animals to the grammar.

here are some samples:
Mary the big cat shares a big pizza to Elizabeth the fish 
Mary the big cat shares a big pizza to Elizabeth the fish at home in the afternoon
Linda the zebra drinks a bottle with Betty the crab
Linda the zebra buys a hamburger from Mary the cat
John the dog shares a toy with David the fox
James a little tiger shares a hamburger with Robert the nice fox in the school during sunset
Maria the lizard eats a pizza with Betty the crab
Maria the unique tiger gives a pizza to Barbara the cat at the ocean in the afternoon