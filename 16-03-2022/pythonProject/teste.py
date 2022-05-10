

n1 = int(input("Lim. inferior"))
n2 = int(input("Lim superior"))
n3 = int(input("Verificador"))

while (n1 <= n2):
    if(n1 % n3 == 0):
        print(n1)
    n1+=1