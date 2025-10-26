# what do the following regexes match?

a. hello 
--> hello

b. Hello
--> Hello World, Hello mary

c. ^Hello
--> Hello World

d. ^Hell*o
--> Hello world, Hellllllllo Anamaniacs

e. ^Hell+0 
--> Hellllllllo Anamaniacs

f.^Hell?o world
--> Hello world, Helo john, Hellllllllo Anamaniacs

g. ^hello [A-Z]
--> nothing 

h. ^Hello [A-Z]
--> Hello World

i. =
--> var = 123

j. #
--> change this #this will change 

k. [
--> what [about] this 

l. ^$
--> line n. 10