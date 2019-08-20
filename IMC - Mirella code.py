# IMC code
AlturaFloat = 1.65
PesoFloat = 60.0

imc = PesoFloat/(AlturaFloat**2)
print (imc)

print ("muito abaixo do peso", imc<17.0)
print ("abaixo do peso normal", imc>=17.0 and imc<=18.5)
print ("peso dentro do normal", imc>18.5 and imc<=25)
print ("peso acima do normal", imc>25 and imc<=30)
print ("muito acima do peso" imc>30)
