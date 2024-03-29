#!/usr/bin/env python3
#https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
import string
import math
import sys

def usage_and_help():
  if (len(sys.argv) > 1):
    if (sys.argv[1] == "--help" or sys.argv[1] == "--usage"):
      print(sys.argv[0], end='')
      print(" -f [filename]")
      print("where filename is the name of the file containing the cyphered text")
      exit()

def print_max_score(allscores):
  for i in range(len(allscores)):
    maximum = 'a'
    for j in allscores[i]:
      if allscores[i][j] > allscores[i][maximum]:
        maximum = j
    print ("the most likely letter for position " + str(i) + " is " + maximum)
      
def offset_string(message, offset):
  answer = ''
  for i in message:
    character = i
    for j in range(ord(offset)-97):
      character = previous_letter(character)
    answer = answer + character
  return answer

def score_probability(letter_probability):
  english_probability = {'A':.0812,'B':.0149,'C':.0271,'D':.0432,'E':.1202,'F':.023,'G':.0203,'H':.0592,'I':.0731,'J':.0010,'K':.0069,'L':.0398,'M':.0261,'N':.0695,'O':.0768,'P':.0182,'Q':.0011,'R':.0602,'S':.0628,'T':.0910,'U':.0288,'V':.0111,'W':.0209,'X':.0017,'Y':.0211,'Z':.0007}
  score = 0
  for i in letter_probability:
    score += math.sqrt(letter_probability[i] * english_probability[i])
  return score

def increment_letter_probablity(letter_probability):
  D = {}
  for i in letter_probability:
    D[next_letter(i)] = letter_probability[i]
  return D

def previous_letter(character):
  index = string.ascii_uppercase.find(character)
  index -= 1
  if (index < 0):
    index = 25
  return string.ascii_uppercase[index]
  
def next_letter(character):
  index = string.ascii_uppercase.find(character)
  index += 1
  if (index > 25):
    index = index % 26
  return string.ascii_uppercase[index]

def get_letter_probability(letter_count):
  num_letters = 0
  D = {}
  for i in letter_count:
    num_letters += letter_count[i]
  for i in letter_count:
    D[i] = letter_count[i] / num_letters
  return D
  
def get_letter_count(sum_letters):
  D = {}
  for i in string.ascii_uppercase:
    D[i] = 0
  for i in (sum_letters):
    D[i] +=1
  return D

def print_in_order(dict):
  number_of_factors_to_print = 10
  print("listing the top " + str(number_of_factors_to_print)+" factors")
  while(dict and number_of_factors_to_print>0): #when dict is empty it evaluates to false
    max = list(dict.keys())[0]
    for i in dict:
      if (dict[i] > dict[max]):
        max = i
    print("there were " + str(dict.pop(max)) + " occurances of the factor "+str(max))
    number_of_factors_to_print-=1
  
  
def CountFrequency(my_list):   
  freq = {} 
  for item in my_list: 
    if (item in freq): 
      freq[item] += 1
    else: 
      freq[item] = 1
  return freq

def getFactors(n):
  # Create an empty list for factors
  factors=[];

  # Loop over all factors
  for i in range(1, n + 1):
    if n % i == 0:
      factors.append(i)

  # Return the list of factors
  return factors
def get_cypher_groups(cypher_text, key_length):   
  sumstrings = {}
  for i in range(0,key_length):
    sumstrings[i] = ''
    for j in range(0,len(cypher_text)):
      if j%key_length == i:
        sumstrings[i] = sumstrings[i]+cypher_text[j]
  return sumstrings

def decrypt_and_print(sumstrings, key):
  decoded = []
  for i in range(len(key)):
    decoded.append( offset_string(sumstrings[i],key[i]))
  for i in range(len(decoded[len(decoded)-1])):
    for j in range(len(decoded)):
      print (decoded[j][i], end='')
  print("")
  

def main():
  usage_and_help()
  cypher_text = "MSKTEBJVWTMABZLFJOUCMYQNOVTEJQGXLRARVZNWHJDTUXEUSECNZMYDXSCNIGARCZODRYZHZNQFXPSROVTLSOZZQZWDXAYBUGWROTOZWOCCTQYDSWZZPRUPWROVTGCSRYMVDWHKGZHHEVOYBBOYBUCQTGEHGICGDZCYKNBGEZUUARCTQQUNSLSSYAVQSJGNUMFHWSGYMYGFWYKXHDWAKUNSGQAEQVRWDXGISTWEPGISPGXSUTJRXZFKCMPJLQQRWFWJCAXJYMPGKBMEQMCJEKHLQCUZTBGDSEUCEWAZGEQAYDCIUWYGMSEOVTWGSXEZHDPRKKXJSJRUCVVFJCAXPRSCHEUCEWMIXTQAYJSGXVVFRTUXBUWDCSKABEPPUJGGGESRRGBMEVGZTVXPOOTBCSDGOTOLGFPEOUGJJWTMBBLPZREWHAEKORTVXJCAJWALPJKTBEQJCARTTWEPEONLGFRUTTLUFHRUWFWQCUZTBGDSQOKXGQTZNMFMYRGEAUGPGUUPJZPSSGZVWDVGQMVLDVGQMVLQCXSMJZZONSQYGNCSKWAUZAKUVYWEGMUTBKPMUAZODFSYKDRJJPUJGPMETUUBYGZGKEWHYZHZUBHJYAKGZBMYRGTLCMEMUAZSWPHUTBUWRFUAVQYZHZGBNCPHNKPBDOCLGTYAXHAXVVFRZUUARXZCZRWBKPYOISBXQHNKAHFOOEYPBWDDRKIFWWCAOARHFZRSMBXQCLSGXFPSYPIPCRSZHIPCNCSKWATPTUXMJWNFGISYGDSEUCETWIKYMIWCMHULLUFHLUWGDZCYKNBGEZUUARCTQQUNSLSSYAVQSJGNUMFHWSGYMYGFWYKXHDWAKUNSGQAEQVRWDXGISTWEPGISPGXSUTJRXZFKCMPJLQQRWFWJCAXJYMPGKBMEQMCJEKHLPJKXGOGOMIABRNPFEHWQQNIZKDRJJPUJGPMESBKZLTZREICGWGSXEJBVJQAZMIWCMHULLWGSXEJBVJQAZNBGEZUUAR"
  if(len(sys.argv) > 1):  
    if (sys.argv[1] == "-f"):
      code_file = open(sys.argv[2],'r')
      cypher_text = code_file.read()
  cypher_text = cypher_text.strip()
  print("the following cypher text will be used:")
  print(cypher_text)

  length = 3 #the length of the segments in the cypher text
  D = {}
  for i in range(0, len(cypher_text)-(length-1)):
    cur = cypher_text[i:i+length] #cur will be every substring of the cyphertext with the given length at some point
    if not cur in D:
      D[cur] = []
      for j in range (0, len(cypher_text)-(length-1)):
        if (cypher_text[j:j+length] == cur):
          D[cur].append(j) #find all indexes that are have the same string and stick them in the dictionary
  #offsets will contain the list of the number of letters  between all repeats. 
  offsets = []
  for i in D:
    if len(D[i])>1: #number of repeats that must be present
      for x, y in zip(D[i], D[i][1::]):
        offsets.append(y-x)

  #for each number in offsets get the factors of that number and store them in allfactors.
  allfactors = []
  for i in offsets:
    for j in getFactors(i):
      allfactors.append(j)
  freq = CountFrequency(allfactors)
  print_in_order(freq)
  
  key_length = int(input("please enter the key's length: "))
  print(key_length)

  #seperate the cypher text's characters into groups based on which character of the key was used to encode them.

  sumstrings = get_cypher_groups(cypher_text, key_length)
  
  #for each group of characters encode the group with a ceaser's cipher using keys a-z and calculate the Bhattacharyya distance between the character frequency distribution of the resultant text and the character frequency distribution of English text.  Print out the letter that results in the highest distance (score) for each group.  
  allscores = [dict() for x in range(key_length)]
  for i in range(key_length):
    for j in string.ascii_lowercase:
      score = score_probability(get_letter_probability(get_letter_count(offset_string(sumstrings[i], j))))
      allscores[i][j] = score
  print_max_score(allscores)

  while(True):
    print("please type the key to decrypt the message")
    key = input()
    decrypt_and_print(sumstrings, key)

if __name__ == "__main__":
  main()
