# Python, Zestaw 2
# Kamil Nowak, Grupa 2
# 19.10.2022r.


#tworzymy line zawierajacy wyrazy oddzielone przez spacje, tabulacje i znak nowej lini
line = "jeden dwa\ttrzyy trzy cztery   piec \n szesc GvR"
print(line)

#dzielimy linie na osobne wyrazy i zapisujemy w liscie
lista_wyrazow = line.split()
print(lista_wyrazow)



# 2.10  ilosc wyrazow w line
print("\n# 2.10  ilosc wyrazow w line\n")
l = len(lista_wyrazow)
print(l)



# 2.11  znaki w napisie oddzielone podloga
print("\n# 2.11  znaki w napisie oddzielone podloga\n")
for word in lista_wyrazow:
    napis_bez = word
    podlogi = ""
    for litera in napis_bez:
        podlogi = podlogi+litera+"_"
    podlogi = podlogi[0:len(podlogi)-1]
    print(podlogi+" ")




# 2.12 slowo zlozone z pierwszych liter wyrazow w line
print("\n# 2.12 slowo zlozone z pierwszych liter wyrazow w line\n")
slowo = ""
for word in lista_wyrazow:
    slowo = slowo+word[0]
print(slowo)


# 2.12 slowo zlozone z ostatnich liter wyrazow w line
print("\n# 2.12 slowo zlozone z ostatnich liter wyrazow w line\n")
slowoLAST = ""
for word in lista_wyrazow:
    slowoLAST  = slowoLAST+word[-1]
print(slowoLAST)

#------------word[-1] <-- ostatni wyraz/litera



# 2.13 laczna dlugosc wyrazow w napisie
print("\n# 2.13 laczna dlugosc wyrazow w napisie\n")
suma = 0
for word in lista_wyrazow:
    suma = suma+len(word)
print(suma)



# 2.14 Najwiekszy wyraz i jego dlugosc
print("\n# 2.14 Najwiekszy wyraz i jego dlugosc\n")
dlugosc = 0
max = ""
for word in lista_wyrazow:
    if(len(word) > dlugosc):
        dlugosc = len(word)
        max = word
print("najwiekszy wyraz: "+str(max)+", "+str(dlugosc)+" liter")



# 2.15 napis bedacy ciagiem cyfr kolejnych liczb z listy L
print("\n# 2.15 napis bedacy ciagiem cyfr kolejnych liczb z listy L\n")
L = [123,5124,613,1,23,5512]
napis = ""
for liczba in L:
    napis = napis+str(liczba)
print(napis)



# 2.16 zamienic ciag znakow "GvR" na "Guido van Rossum"
print("\n# 2.16 zamienic ciag znakow \"GvR\" na \"Guido van Rossum\"\n")
i = 0
while(i < len(lista_wyrazow)):
    if(lista_wyrazow[i] == "GvR"):
        lista_wyrazow[i] = "Guido van Rossum"
    i = i+1
print(lista_wyrazow)



# 2.17 posortowac line alfabetycznie i wg dlugosci
print("\n# 2.17 posortowac line alfabetycznie i wg dlugosci\n")
#sortowanie listy alfabetycznie
print("#sortowanie listy alfabetycznie")
lista_sorted = sorted(lista_wyrazow)
print(lista_sorted)

#sortowanie listy wg dlugosci
print("#sortowanie listy wg dlugosci")
lista_sorted = sorted(lista_wyrazow, key=len, reverse=False)
print(lista_sorted)



# 2.18 znalezc liczbe cyfr zero w duzej liczbie calkowitej
print("\n# 2.18 znalezc liczbe cyfr zero w duzej liczbie calkowitej\n")
duza_liczba = 80050200
as_text = str(duza_liczba)
ilosc = 0
for litera in as_text:
    if litera == "0":
        ilosc = ilosc+1
print(ilosc)



# 2.19 na liscie mamy liczby 1,2,3 cyfrowe
print("\n# 2.19 na liscie mamy liczby 1,2,3 cyfrowe\n")
Lista = [123,55,7,223,12,9]
napis_trzy = ""
for number in Lista:
    napis_trzy = napis_trzy+(str(number).zfill(3))+", "
napis_trzy = napis_trzy[0:len(napis_trzy)-2]
print(napis_trzy)


