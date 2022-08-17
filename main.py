instrucciones = ""
continuar = True
memoria = [[""],[0]]
acumulador = 0
icr = ""
mar = ""
uc = ""
mdr = 0

def instruccion_set(par1, par2):
  memoria[0].append(par1)
  memoria[1].append(par2)
  
def instruccion_ldr(par1):
  global acumulador
  acumulador = memoria[1][memoria[0].index(par1)]
  
def instruccion_str(par1):
   memoria[1][memoria[0].index(par1)]=acumulador
  
def instruccion_shw(par1):
  print(memoria[1][memoria[0].index(par1)])
  
while (continuar):  
  instrucciones = input()
  lista_instrucciones = instrucciones.split()
  if(lista_instrucciones[0]=="SET"):
    instruccion_set(lista_instrucciones[1],lista_instrucciones[2])
  if(lista_instrucciones[0]=="ADD"):
    if(lista_instrucciones[2] == "NULL"):
      acumulador = int(acumulador) + int(memoria[1][memoria[0].index(lista_instrucciones[1])])
    else:
      if(lista_instrucciones[3] == "NULL"):
        acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
        acumulador = int(acumulador) + int(memoria[1][memoria[0].index(lista_instrucciones[2])])
      else:
        acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
        acumulador = int(acumulador) + int(memoria[1][memoria[0].index(lista_instrucciones[2])])
        instruccion_set(lista_instrucciones[3],acumulador)
  if(lista_instrucciones[0]=="SUB"):
    if(lista_instrucciones[2] == "NULL"):
      acumulador = int(acumulador) - int(memoria[1][memoria[0].index(lista_instrucciones[1])])
    else:
      if(lista_instrucciones[3] == "NULL"):
        acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
        acumulador = int(acumulador) - int(memoria[1][memoria[0].index(lista_instrucciones[2])])
      else:
        acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
        acumulador = int(acumulador) - int(memoria[1][memoria[0].index(lista_instrucciones[2])])
        instruccion_set(lista_instrucciones[3],acumulador)
  if(lista_instrucciones[0]=="MUL"):
    if(lista_instrucciones[2] == "NULL"):
      acumulador = int(acumulador) * int(memoria[1][memoria[0].index(lista_instrucciones[1])])
    else:
      if(lista_instrucciones[3] == "NULL"):
        acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
        acumulador = int(acumulador) * int(memoria[1][memoria[0].index(lista_instrucciones[2])])
      else:
        acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
        acumulador = int(acumulador) * int(memoria[1][memoria[0].index(lista_instrucciones[2])])
        instruccion_set(lista_instrucciones[3],acumulador)
  if(lista_instrucciones[0]=="DIV"):
    print("Error.")
  if(lista_instrucciones[0]=="INC"):
    acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
    acumulador = int(acumulador) + 1
    memoria[1][memoria[0].index(lista_instrucciones[1])] = acumulador    
  if(lista_instrucciones[0]=="DEC"):
    acumulador = memoria[1][memoria[0].index(lista_instrucciones[1])]
    acumulador = int(acumulador) - 1
    memoria[1][memoria[0].index(lista_instrucciones[1])] = acumulador 
  if(lista_instrucciones[0]=="MOV"):
    memoria[1][memoria[0].index(lista_instrucciones[2])] = memoria[1][memoria[0].index(lista_instrucciones[1])]
    memoria[1][memoria[0].index(lista_instrucciones[1])] = 0 
  if(lista_instrucciones[0]=="LDR"):
    instruccion_ldr(lista_instrucciones[1])
  if(lista_instrucciones[0]=="STR"):
    instruccion_str(lista_instrucciones[1])
  if(lista_instrucciones[0]=="BEQ"):
    if(lista_instrucciones[2] == "NULL"):
      if((int(memoria[1][memoria[0].index(lista_instrucciones[1])]) - int(acumulador)) ==0):
        memoria[1][memoria[0].index(lista_instrucciones[1])] = 0
    else:
      if((int(memoria[1][memoria[0].index(lista_instrucciones[1])]) - int(memoria[1][memoria[0].index(lista_instrucciones[2])])) ==0):
        memoria[1][memoria[0].index(lista_instrucciones[1])] = 0
      else:
         if((int(memoria[1][memoria[0].index(lista_instrucciones[1])]) - int(memoria[1][memoria[0].index(lista_instrucciones[2])])) ==0):
            instruccion_set(lista_instrucciones[3],0)
  
  if(lista_instrucciones[0]=="SHW"):
    if(lista_instrucciones[1]=="ACC"):
      print(acumulador)
    else:
      if(lista_instrucciones[1]=="ICR"):
        print(icr)
      else:
        if(lista_instrucciones[1]=="MAR"):
          print(mar)
        else:
          if(lista_instrucciones[1]=="MDR"):
            print(mdr)
          else:
            if(lista_instrucciones[1]=="UC"):
              uc = icr
              print(uc)
            else:
              instruccion_shw(lista_instrucciones[1])
  if(lista_instrucciones[0]=="END"):
    continuar = False

  try:
    
    icr = lista_instrucciones[0] + " " + lista_instrucciones[1]
    mar = lista_instrucciones[1]
    mdr = memoria[1][memoria[0].index(lista_instrucciones[1])]
  except:
    mdr = ""

