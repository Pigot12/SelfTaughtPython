#Lists
#Arxizoume apo to 0

Penguins = ['African penguin' , 'Northern rockhopper penguin' , 'King penguin' , 'Adélie penguin' , 'Fairy penguin' ]

print(Penguins[0])

#Perissotera apo ena stoixeia
#Mas trwei enan ariumo(arxizei apo 0)
print(Penguins[0:2])

#Len=Length=Mhkos
print(len(Penguins))

#Teleutaio Stoixeio
print(Penguins[4])

#-=Arxizoyme apo to telos
print(Penguins[-2])

# Methods 

#Kata aujousa seira
Penguins.sort()
print(Penguins)

#tajinhnomenh antistrofa
Penguins.sort(reverse=True)
print(Penguins)

#Prosuesh stoixeiou
Penguins.append('Macaroni penguin')
print(Penguins)

#Afairoume
Penguins.remove('Macaroni penguin')
print(Penguins)

#Me sygkekrimenh Uesh
Penguins.insert(2 , 'Macaroni penguin')

Numbers = [5 , 5 , 5 , 1 , 5 , 2]

#max =maximum
print(max(Numbers))

#min=minumum
print(min(Numbers))

#sum=auroisma
print(sum(Numbers))

#print(Numbers[2])