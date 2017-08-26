import re
import random

class Question:
	def __init__(self, q, a):
		self.q = q
		self.a = a


Ryes = '^yes$|^y$'
Rno = '^no$|^n$'

Questions = [
	Question("Is it an animal?", "animal"),
	Question("Is it a plant?", 'plant'),
	Question("Is it an inanimate object?", 'inanimate'),
	Question("Is it bigger than a toilet?", 'large'),
	Question("Is it smaller than a basketball?", 'small'),
	Question("Is it partially or sometimes white?", 'white'),
	Question("Is it partially or sometimes black?", 'black'),
	Question("Is it partially or sometimes blue?", 'blue'),
	Question("Is it partially or sometimes green?", 'green'),
	Question("Is it partially or sometimes grey?", 'grey'),
	Question("Is it partially or sometimes red?", 'red'),
	Question("Is it something people eat?", 'eat'),
	Question("Is it something people cook?", 'cook'),	
	Question("Is it a place?", 'place'),
	Question("Is it a country?", 'country'),
	Question("Is it a city?", 'city'),
]

# Attrs = ['animal', 'vegetable', 'mineral', 'large', 'small']

Lex = {
	'cow': ['animal', 'large', 'black', 'white', 'eat', 'cook'],
	'rabbit': ['animal', 'white', 'small', 'eat', 'cook'],
	'bat': ['animal', 'black', 'small'],
	'mouse': ['animal', 'small', 'brown', 'white', 'grey'],
	'broccoli': ['plant', 'green', 'eat', 'small', 'cook'],
	'apple': ['plant', 'red', 'green', 'eat', 'small'],	
	'diamond': ['inanimate', 'small'],
	'mountain': ['inanimate', 'large', 'grey'],
	'The United States': ['place', 'country'],
	'New York City': ['place', 'city'],
	'The Moon': ['place', 'inanimate', 'white', 'grey', 'large'],
}

def attrsinlex():
	global Lex
	
	res = set()
	for k in Lex:
		for x in Lex[k]:
			res.add(x)
	return list(res)

def checkquestions(question):
	global Questions
	
	Questions.remove(question)	
	Attrs = attrsinlex()
	newq = []
	for q in Questions:
		if q.a in Attrs:
			newq.append(q)
	Questions = newq	

def preservebyattr(attr):
	global Lex
	
	newlex = {}
	for x in Lex:
		if attr in Lex[x]:
			newlex[x] = Lex[x]
	Lex = newlex
	
def removebyattr(attr):
	global Lex
	
	newlex = {}
	for x in Lex:
		if not attr in Lex[x]:
			newlex[x] = Lex[x]
	Lex = newlex

def frame():
	print('Hello! I will ask a question now.\n')
	mainloop(1)

def mainloop(qref):
	global Lex
	global Questions
	
	if len(Questions) == 0:
		print('Sorry, I don\'t know :(')
		return
	
	if len(Lex) == 1:
		print('Is it a ' + list(Lex)[0] + '?')
		return
	# print([q.q for q in Questions])
	question = random.choice(Questions)
	answer = input(str(qref) + ": " + question.q)
	answer = yesno(answer)
	if answer == 0:
		removebyattr(question.a)
	elif answer == 1:
		preservebyattr(question.a)
	checkquestions(question)
	mainloop(qref+1)
	
def yesno(string):
	if re.search(Ryes, string):
		return 1
	elif re.search(Rno, string):
		return 0
	else:
		return -1

frame()