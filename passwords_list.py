#liste of alphabets and numbers, will generates a list of: 1.679.616 Passwords
lista= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]

for i in lista:
    for j in lista:
        for k in lista:
            for l in lista:
                print(i+j+k+l) 
    