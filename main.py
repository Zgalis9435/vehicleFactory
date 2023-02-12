from vehicle import vehicle
import pickle
#File creation
f=open('vehicleTXT.bin','rb')
#Main method
 #Car creation
vehicle1=vehicle('Opel','Blue',4,3)
#Car ToString
print(vehicle1)
#SaveObjectOnTxt
#pickle.dump(vehicle1,f)
#f.close()
vehicle2=pickle.load(f)
print(vehicle2)
