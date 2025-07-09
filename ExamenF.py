productos={
    "8475HD":["Hp","15.6","8GB","DD","1T","intel core i5","Nvidia GTX1050"],
    "2175HD":["Lenovo","14","4GB","SSD","512GB","intel core i5","Nvidia GTX1050"],
    "JjfFHD":["Asus","14","16GB","SSD","256GB","intel core i7","Nvidia RTX2080ti"],
    "fgdxFHD":["HP","15.6","8GB","DD","1T","intel core i3","Integrada"],
    "GF75HD":["Asus","15.6","8GB","DD","1T","intel core i7","Nvidia GTX1050"],
    "123FHD":["Lenovo","14","6GB","DD","1T","AMD Ryzen 5","integrada"],
    "342FHD":["Lenvo","15.6","8GB","DD","1T","AMD Ryzen 7","Nvidia GTX1050"],
    "UWU131HD":["Dell","15.6","8GB","DD","1T","AMD Ryzen 3","Nvidia GTX1050"],
}

stock={"8475HD":[387990,10],"2175HD":[327990,4],"JjfFHD":[424990,1],"fgdxFHD":[664990,21],"GF75HD":[749990,2],
    "123FHD":[290890,32],"342FHD":[444990,7],"UWU131HD":[349990,1],"FS1230HD":[249990,0],}
def stock_marca(marca):
    total=0
    marca=marca.lower()
    for codigo in productos:
        if productos[codigo][0].lower()==marca:
            if codigo in stock:
                total+=stock[codigo][1]
    print(f"El stock de {marca.capitalize()}es: {total}")

def busqueda_precio(precio_min,precio_max):
    resultados=[]
    for codigo in productos:
        if codigo in stock:
            precio=stock[codigo][0]
            cantidad=stock[codigo][1]
            if precio_min<=precio<=precio_max and cantidad>0:
                marca=productos[codigo][0]
                resultados.append(f"{marca}")
    if resultados:
        resultados.sort()
        print("Los computadores en el rango de precios elegidos son:",resultados)
    else:
        print("No hay notebooks en ese ramgo de precios.")

def actualizar_precio(codigo,nuevo_precio):
    if codigo in stock:
        stock[codigo][0]=nuevo_precio
        return True
    else:
        return False

while True:
    print("══════════════════════════════════════")
    print("          --MENU PRINCIPAL--          ")
    print("║1. Stock por Marca.                 ║")
    print("║2. Busqueda en rango de precios.    ║")
    print("║3. Actualizar precios o stock de PC.║")
    print("║4. Salir.                           ║")
    print("══════════════════════════════════════")
    opcion=input("Ingrese opcion: ")
    if opcion=="1":
        Marcas=input("|Ingrese la marca del notebook(HP,LENOVO,ASUS Y DELL): ")
        stock_marca(Marcas)
    elif opcion=="2":
        while True:
            try:
                p_min=int(input("|Ingrese precio minimo: "))
                p_max=int(input("|Ingrese precio maximo: "))
                break
            except:
                print("|Ingrese valores enteros validos!!!!.")
        busqueda_precio(p_min,p_max)
    elif opcion=="3":
        while True:
            marca=input("|Ingrese la marca del notebook (HP, LENOVO, ASUS, DELL): ").strip().lower()
            modelos_disponibles=[]
            for codigo in productos:
                if productos[codigo][0].lower()==marca and codigo in stock:
                    modelos_disponibles.append(codigo)
            if not modelos_disponibles:
                print("No hay modelos disponibles para esa marca.")
                resp=input("Desea intentar con otra marca? (si/no): ").strip().lower()
                if resp!="si":
                    break
                else:
                    continue
            print("Modelos disponibles para",marca.capitalize(),":",modelos_disponibles)
            codigo=input("Ingrese el modelo de computador a actualizar: ").strip()
            try:
                nuevo_precio=int(input("Ingrese el nuevo precio del computador: "))
                resultado=actualizar_precio(codigo,nuevo_precio)
                if resultado==True:
                    print("Precio actualizado")
                else:
                    print("El modelo no existe")
            except:
                print("Debes ingresar un numero.")
            resp=input("Desea actualizar otro precio de notebook? (si/no): ").strip().lower()
            if resp!="si":
                break
    elif opcion=="4":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opcion valida")
