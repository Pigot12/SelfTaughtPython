Social = ["1" , "2" , "3" , "4"]
Media = ["1" , "2" , "3" , "4"]

#Emfanizoume sugkekrimeno Ariumo
##print(Social[2])

#Prostetoume sthn lista
Social.append("5")

##print(Social)

#Afairoume apo thn lista
Social.remove("5")

#Makrenoume mia lista me mia allh
Social.extend(Media)
print(Social)

#Bazeis ena value sthn lista
Social.insert(1, "10")
print (Social)