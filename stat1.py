#compteur nb : seq , susC, susD, other, gh, pl .



#compter le nombre de seq initiale de notre base de donnee

import sys

def parserMultiFasta(nomFichier):
	i = 0
	fic = open(nomFichier, 'r')
	line = fic.readline()
	for line in fic :
		if line.startswith('>'):
			#print(line)
			i += 1
	print("nombre de seq = ",i)
parserMultiFasta(sys.argv[1])

"""	
dans notre fichier fasta il ya 2461188	seq 	
"""

#combien code pour des susC

import sys

def parserMultiFasta(nomFichier):
	i = 0
	susC= '||<div class="Trans"'
	fic = open(nomFichier, 'r')
	line = fic.readline()
	for line in fic :
		if susC in line:
			#print(line)
			i += 1
	print("nombre de susC = ",i)
parserMultiFasta(sys.argv[1])

"""	
dans notre fichier fasta il ya 83404 SusC 	

"""

#combien code pour des susD

import sys

def parserMultiFasta(nomFichier):
	i = 0
	susD= '||<div class="SusD"'
	fic = open(nomFichier, 'r')
	line = fic.readline()
	for line in fic :
		if susD in line:
			#print(line)
			i += 1
	print("nombre de susD = ",i)
parserMultiFasta(sys.argv[1])

"""	
dans notre fichier fasta il ya 23777 SusD 	
"""
#combien code pour des others

import sys

def parserMultiFasta(nomFichier):
	i = 0
	other= '||<div class="other"'
	fic = open(nomFichier, 'r')
	line = fic.readline()
	for line in fic :
		if other in line:
			i += 1
	print("nombre de other = ",i)
parserMultiFasta(sys.argv[1])

"""	
dans notre fichier fasta il ya 2096455 other 	
"""

#combien code pour de gh et de pl 

import sys

def parserMultiFasta(nomFichier):
	i = 0
	pl_gh= '||<div class="PL"' and '||<div class="PL"'
	fic = open(nomFichier, 'r')
	line = fic.readline()
	for line in fic :
		if pl_gh in line:
			i += 1
	print("nombre de gh/pl = ",i)
parserMultiFasta(sys.argv[1])

#3673 GH
#3673 PL

