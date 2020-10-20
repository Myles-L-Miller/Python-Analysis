
#Import a text file filled with a paragraph of your choosing.

#Assess the passage for each of the following:

  # Approximate word count

  # Approximate sentence count

  # Approximate letter count (per word)

  # Average sentence length (in words)


import os
import re

#Read File
ParagraphIndex=1
File = open(os.path.join("Instructions", "PyParagraph", "Resources", f"paragraph_{ParagraphIndex}.txt"),"r")
Paragraph=File.read().replace("\n"," ").replace("  "," ")

#Splitting to sentences
Sentences=re.split("(?<=[.!?]) +", Paragraph)

#Derermining count values
ApproxSCount=len(Sentences)
AvSLen=0
Words=[]
for Sentence in Sentences:
    AvSLen+=len(Sentence.split(" "))
    Words+=Sentence.split(" ")
AvSLen=round(AvSLen/ApproxSCount,1)
ApproxWCount=len(Words)

#Remove special characters from word length
AvWLen=0
for i in range(len(Words)):
    Words[i]=''.join(letter for letter in Words[i] if letter.isalnum())
    AvWLen+=len(Words[i])
AvWLen=round(AvWLen/ApproxWCount,1)

#Print
print("\nParagraph Analysis\n----------------------\n")
print(f"Approximate Word Count: {ApproxWCount}\n")
print(f"Approximate Sentence Count: {ApproxSCount}\n")
print(f"Average Letter Count: {AvWLen}\n")
print(f"Average Sentence Length: {AvSLen}\n")