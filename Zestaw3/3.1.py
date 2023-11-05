x = 2; y = 3;
if (x > y):
    result = x;             #kod poprawny, jednak średniki nie są wymagane
else:
    result = y;


################

#for i in "axby": if ord(i) < 100: print (i)       #kod niepoprawny, brak nowej linii w wyrażeniu warunkowym


################

for i in "axby": print (ord(i) if ord(i) < 100 else i)      #kod poprawny
