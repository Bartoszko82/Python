#if 2 > 1:
#    if 3 > 2:
#        print("OK")
#    else:
#        print("FAIL")
#    print("DONE")

#liczymy bmi

#bmi = int(input())
#chudy = "niedowaga"
#normalny = "waga prawidłowa"
#gruby = "nadwaga"
#
#if bmi < 18.5:
#    print(chudy)
#if bmi >= 18.5:
#    if bmi < 25.0:
#        print(normalny)
#if bmi >= 25.0:
#    print(gruby)

#test ELIF

#n = 0
#
#if n < 1:
#    print("jeden")
#elif n < 2:
#    print("dwa")
#elif n < 3:
#    print("trzy")
#else:
#    print("duzo")

#KROTKI

#names = ("Paulina", "Kowalksa")
#details = (27, 1.70)
#point = ("Area51", (37, 115))
#print(names+details)
#print(point)

#wracamy do BMI + formatowanie 

#bmi = 21.398273497
bmi = int(input())
chudy = "niedowaga"
normalny = "waga prawidłowa"
gruby = "nadwaga"
tekst = str()

if bmi < 18.5:
    tekst = chudy
if bmi >= 18.5:
    if bmi < 25.0:
        tekst = normalny
if bmi >= 25.0:
    tekst = gruby
    
wynikA = "Twoje BMI: %.2f (%s)" % (bmi, tekst)
wynikB = "Twoje BMI: %.2f (%s)" % (bmi, tekst)
wynikC = "{:^50}".format("Twoje BMI: %.2f (%s)" % (bmi, tekst))
wynikD = "Twoje BMI: %.2f (%s)".center(60) % (bmi, tekst)

print("{:^40}".format(wynikA))    
print(wynikB.center(40, ))
print(wynikC)
print(wynikD)


