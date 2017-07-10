"""
This is an example of the Paladins game's stupid chat filter that
filters out the slang terms even when they are used in other words
which are not slangs.
Example=input- "ClassGrass" | output- "Cl***Gr***"
"""
import re
Input=raw_input("Enter text: ")
Output=Input

slanglist=['retard','ass', 'bitch']
for i in slanglist:
    replace=len(i)*'*'
    In=re.compile(re.escape(i),re.IGNORECASE)   #Case-insensitive
    Output=re.sub(In,replace,Output)            #replacement
print Output

#Below is another way to do the same using dictionaries, here the key
#will be slang term and value will be asterisks
#this can be used for terms which have spaces between them
#Though an exception can be made for spaces in above code for the same

##slangs={'retard':'******','ass':'***','bitch':'*****'}
##for i in slangs.keys():
##    In=re.compile(re.escape(i),re.IGNORECASE)
##    Output=re.sub(In,slangs[i],Output)
##print Output

#Another way to make this without using re module is given below but it's case sensitive

##slangs={'retard':'******','ass':'***','bitch':'*****'}
##Input=raw_input("enter text: ")
##Output=Input
##for i in slangs.keys():
##    a=i.lower()
##    b=i.capitalize()
##    c=i.upper()
##    if a in Input:
##        Output=Output.replace(a,slangs[a])
##    if b in Input:
##        Output=Output.replace(b,slangs[a])
##    if c in Input:
##        Output=Output.replace(c,slangs[a])
##print Output



#P.S. This is a mockery.
