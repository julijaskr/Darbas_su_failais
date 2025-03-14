

failas = open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\studentai.txt')
nuskaitytas_tekstas = failas.read() #perskaito faila
failas.close() # faila uzdare
print(nuskaitytas_tekstas) # ka perskaite atspausdino

print('=======')

failas = open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\studentai.txt')
nuskaitytas_tekstas = failas.read()
print('NUSKAITYTAS:', nuskaitytas_tekstas)
print()
kitas_tekstas = failas.read()
failas.close() # faila uzdare
print('KITAS:', kitas_tekstas)

print('=======')

# failas = open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\studentai.txt')
failas = open('./studentai.txt') # realetyvus kelio nurodymas
# failas = open('../') # paima is kito sluoksnio(gylio failus)
nuskaitytas_tekstas = failas.read()
print('NUSKAITYTAS:', nuskaitytas_tekstas)
print()
failas.seek(0) # pozicijos pakeitimas (nurodo kur turi buti kursiorius atidarius faila, jeigu nurodysi (5) atsistos ties 5 simboliu ir skaitys teksta nuo jo
per_nauja_tekstas = failas.read()
failas.close() # faila uzdare
print('PER NAUJA:', per_nauja_tekstas)

print('=======')

with open ('./studentai.txt') as failas: #taikomas skaityti dideliems failams
    tekstas = failas.read()
    print(tekstas)

print('=======')

failas = open('./studentai.txt')
tekstas = failas.read()
print(tekstas)
print(failas.closed)
failas.close()
print(failas.closed)
# print(failas.read()) # klaida I/O operation on closed file. I - input, O-output. klaida sako, kad failo neskaitys, nes jis jau uzdarytas

print('=======')

# kai naudoji tik open, tai faila reikia paciam uzdaryti
failas = open('./studentai.txt')
failas.read()
failas.close()
print(failas.closed) # True

# kai naudoji with open, tai funkcija pati uzdaro faila. Paiam to daryti nereikia
with open ('./studentai.txt') as failas:
    failas.read()
print(failas.closed)  # True

print('EKSTO SKAITYMAS PO VIENA EILUTE')

with open ('./studentai.txt') as failas:
    eilute= failas.readline()
    print(eilute)

print('PERSKAITO DAUGIAU EILUCIU, BET REIKIA KARTOTI KODA')

with open ('./studentai.txt') as failas:
    eilute= failas.readline()
    print(eilute)
    eilute = failas.readline()
    print(eilute)
    eilute = failas.readline()
    print(eilute)
    eilute = failas.readline()
    print(eilute)

print('===PERSKAITO VISAS EILUTES===') # sudeda i viena eilute

with open ('./studentai.txt') as failas:
    visas_tekstas = failas.readlines()
    print(visas_tekstas)

print('===NUIMA SIMBOLIUS PERKELIMO I KITA EILUTE SIMBOLIUS====')

with open ('./studentai.txt') as failas:
    visas_tekstas = failas.readlines()
    print('VISAS TEKSTAS:', visas_tekstas)
    sutvarkytas_tekstas = [ eilute[:-1] for eilute in visas_tekstas ] # prasuk cikla per eilute ir paimk viska is eilutes issskyrus paskutini elementa
print('SUTVARKYTAS TEKSTAS:', sutvarkytas_tekstas)

print('===PALIEKO PASKUTINTOS EILUTES PASKUTINI SIMBOLI===')

with open ('./studentai.txt') as failas:
    visas_tekstas = failas.readlines()
    print('VISAS TEKSTAS:', visas_tekstas)
    sutvarkytas_tekstas = [eilute.rstrip('\n') for eilute in visas_tekstas] #vienos eilutes ciklas, bus grazinta, kaip masyvas nes yra [] skliaustai
    print('SUTVARKYTAS TEKSTAS:', sutvarkytas_tekstas)

print('===OBJEKTAS PAVERCIAMAS MASYVU===')

with open ('./studentai.txt') as failas:
    tekstas = failas.read().splitlines() # splitlines gautus duomenis pavercia masyvu
    print(tekstas)

print('===KINTAMOJO TIPO PASITIKRINIMAS===')

with open ('./studentai.txt') as failas:
    print(type(failas.read())) # grazina teksta
    failas.seek(0)
    print(type(failas.readline())) # grazina teksta
    failas.seek(0)
    print(type(failas.readlines())) # grazina sarasa

    print(type(tekstas))  # parodo kokio tipo yra kintamasis "tekstas"

print('===PERSKAITO TEKSTA IR PERMETA I SKIRTINGAS EILUTES===') # sudeda i atskiras eilutes. PRIVALUMAS SIO KODO, KAD JIS NETURI PERSKAITYTI VISO FAILO, KAI TIK RANDA UZDUOTA UZDUOTI NUSTOJA SKAITYTI IR FAILA UZDARO. 2IA TUO ATVEJU JEIGU IESKOTI PVZ.VARDO IR VISOS JAM PRISKIRTOS EILUTES

eilutes = []
with open ('./studentai.txt') as failas:
    while True:
        eilute = failas.readline().rstrip('\n') #suka cikla ir vis iesko naujos eilute
        if not eilute: # jeigu eilutes neranda cikla sustabdo
            break #
        print('nuskaityta eilute:', eilute) # jeigu randa eilute atlieka veiksmus, paraso nuskaityta eilute ir teksta
        eilutes.append(eilute)
print(eilutes)

eilutes = []
with open ('./studentai.txt') as failas:
    for eilute in failas:#cia variantas kai suka cikla
        eilute = eilute.rstrip('\n')
        print('nuskaityta eilute:', eilute)
        eilutes.append(eilute)
print(eilutes)

print('===')
studentai = []
with open('./studentai.txt', encoding="utf8") as failas: #perskaito teksta ir uzsideda koda , encoding="utf8" - nurodo kokia koduote naudoti norint sutvarkyti teksta, kad nemestu ivairiu simboliu
    for eilute in failas: # suka cikla kiekvienai eilutei
        eilute = eilute.rstrip('\n') # nuimame nereikalinga simboli eilutes gale (\n)
        isskaidyta = eilute.split(';') # kiekviena elementa atskiria per uzduota simboli.siuo atveju ';'
        studentas = dict(              #priskiria raktinius zodzius,pvz.vardas ir tuomet lengviau ieskoti ne pagal elementus, o pagal raktinius zodzius
            vardas = isskaidyta[0],
            pavarde = isskaidyta[1],
            amzius = isskaidyta[2],
            mokykla = isskaidyta[3],
            vidurkis = isskaidyta[4]
        )
        studentai.append(studentas)
print(studentai) #atspausdina visus elementus
print(studentai[1]) # atspausdina pirma eilute po lenteles pavadinimu (header)
print(studentai[1]['pavarde']) # istraukia pirmos eilutes studenta, pagal raktini zodi 'pavarde'

print('===RASYMAS I FAILA/ FAILO PILDYMAS===')

with open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\rasymui.txt', 'w') as failas:
    failas.write('pirma\n')
    failas.write('antra\n')
    failas.write('trecia\n')
    failas.write('ketvirta\n')

print('===KARTOTI DAUG KARTU TA PATI TEKSTA===')

with open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\rasymui.txt', 'w') as failas: #'w' - rasymas i faila, 'a' - rasymas i faila, ji papildant, 'r+' - failo skaitymas ir rasymas, 'r' - failo nuskaitymas
    failas.write('LABAS\n' * 5)

print('===PAPILDOMAS FAILAS TEKSTU===')

with open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\rasymui.txt', 'a') as failas:
    failas.write('siandien sviecia saule\n')
    failas.write('ir yra daug sniego')

print('===FAILAS PERSKAITOMAS IR PAPILDOMAS TEKSTU===') # tekstas atsiranda failo virsuje. r+ gali dirbti tik su egzistuojanciais failais

with open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\rasymui.txt', 'r+') as failas:
    failas.write('siandien sviecia saule\n')
    failas.write('ir yra daug sniego\n')

with open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\auto.txt') as failas:
    tekstas = failas.read()
    print(tekstas)

automobiliai = []
with open('C:\\Users\\lucky\\PycharmProjects\\Darbas_su_failais\\auto.txt') as failas:
    for eilute in failas: # suka cikla kiekvienai eilutei
        eilute = eilute.rstrip('\n') # nuimame nereikalinga simboli eilutes gale (\n)
        isskaidyta = eilute.split(';')
        automobilis = dict(
            marke = isskaidyta[0],
            modelis = isskaidyta[1],
            metai = isskaidyta[2],
            variklis = isskaidyta[3]
        )
        automobiliai.append(automobilis)
# print(automobiliai)
# print(automobiliai[1])
# print(automobiliai[2] ['metai'])

metai = [int(automobilis['metai']) for automobilis in automobiliai]
print(metai)
vidurkis= sum(metai) / len(metai)
print(f'Automobiliu metu vidurkis: {vidurkis:.0f}')

with open('./rezultatai.txt', 'w') as failas:
    failas.write(f'Automobiliu metu vidurkis: {vidurkis:.0f}') # .0 - parodo, kiek skaičių po kablelio (šiuo atveju 0 skaičiai), f - reiškia, kad tai "float" tipo skaičius (dešimtainis)

