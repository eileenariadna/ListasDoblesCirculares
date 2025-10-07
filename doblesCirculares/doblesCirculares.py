class Nodo:
    """Clase que representa un nodo en la lista doble circular"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleCircular:
    """Clase que implementa una lista doble circular"""
    def __init__(self):
        self.cabeza = None
    
    def esta_vacia(self):
        """Verifica si la lista está vacía"""
        return self.cabeza is None
    
    def insertar_al_final(self, dato):
        """Inserta un nuevo nodo al final de la lista"""
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            # Si la lista está vacía, el nuevo nodo apunta a sí mismo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            # Obtener el último nodo (el anterior a la cabeza)
            ultimo = self.cabeza.anterior
            
            # Conectar el nuevo nodo
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo
            ultimo.siguiente = nuevo_nodo
            self.cabeza.anterior = nuevo_nodo
        
        print(f"✓ Elemento {dato} insertado al final")
    
    def insertar_al_inicio(self, dato):
        """Inserta un nuevo nodo al inicio de la lista"""
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior
            
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo
            self.cabeza.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
        
        print(f"✓ Elemento {dato} insertado al inicio")
    
    def eliminar(self, dato):
        """Elimina el primer nodo que contenga el dato especificado"""
        if self.esta_vacia():
            print(f"✗ La lista está vacía. No se puede eliminar {dato}")
            return False
        
        actual = self.cabeza
        
        # Buscar el nodo a eliminar
        while True:
            if actual.dato == dato:
                # Si solo hay un nodo
                if actual.siguiente == actual:
                    self.cabeza = None
                else:
                    # Reconectar los nodos vecinos
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    
                    # Si eliminamos la cabeza, actualizarla
                    if actual == self.cabeza:
                        self.cabeza = actual.siguiente
                
                print(f"✓ Elemento {dato} eliminado")
                return True
            
            actual = actual.siguiente
            
            # Si volvimos a la cabeza, el elemento no está
            if actual == self.cabeza:
                break
        
        print(f"✗ Elemento {dato} no encontrado")
        return False
    
    def buscar(self, dato):
        """Busca un elemento en la lista"""
        if self.esta_vacia():
            print("✗ La lista está vacía")
            return False
        
        actual = self.cabeza
        posicion = 0
        
        while True:
            if actual.dato == dato:
                print(f"✓ Elemento {dato} encontrado en la posición {posicion}")
                return True
            
            actual = actual.siguiente
            posicion += 1
            
            if actual == self.cabeza:
                break
        
        print(f"✗ Elemento {dato} no encontrado")
        return False
    
    def mostrar_adelante(self):
        """Muestra la lista recorriéndola hacia adelante"""
        if self.esta_vacia():
            print("La lista está vacía")
            return
        
        print("\n Lista (hacia adelante):", end=" ")
        actual = self.cabeza
        
        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        print(f"(vuelve a {self.cabeza.dato})")
    
    def mostrar_atras(self):
        """Muestra la lista recorriéndola hacia atrás"""
        if self.esta_vacia():
            print("La lista está vacía")
            return
        
        print(" Lista (hacia atrás):", end=" ")
        actual = self.cabeza.anterior
        
        while True:
            print(actual.dato, end=" <- ")
            actual = actual.anterior
            if actual == self.cabeza.anterior:
                break
        
        print(f"(vuelve a {self.cabeza.anterior.dato})\n")
    
    def contar_elementos(self):
        """Cuenta la cantidad de elementos en la lista"""
        if self.esta_vacia():
            return 0
        
        actual = self.cabeza
        contador = 0
        
        while True:
            contador += 1
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        return contador


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("    LISTA DOBLE CIRCULAR - MENÚ INTERACTIVO")
    print("-"*50)
    print("1. Insertar elemento al final")
    print("2. Insertar elemento al inicio")
    print("3. Eliminar elemento")
    print("4. Buscar elemento")
    print("5. Mostrar lista hacia adelante")
    print("6. Mostrar lista hacia atrás")
    print("7. Mostrar en ambas direcciones")
    print("8. Contar elementos")
    print("9. Salir")
    print("-"*50)


def main():
    """Función principal del programa"""
    lista = ListaDobleCircular()
    
    print("\n ¡Bienvenido a la demostración de Lista Doble Circular!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (1-9): ").strip()
            
            if opcion == "1":
                dato = input("Ingresa el elemento a insertar al final: ").strip()
                lista.insertar_al_final(dato)
                
            elif opcion == "2":
                dato = input("Ingresa el elemento a insertar al inicio: ").strip()
                lista.insertar_al_inicio(dato)
                
            elif opcion == "3":
                dato = input("Ingresa el elemento a eliminar: ").strip()
                lista.eliminar(dato)
                
            elif opcion == "4":
                dato = input("Ingresa el elemento a buscar: ").strip()
                lista.buscar(dato)
                
            elif opcion == "5":
                lista.mostrar_adelante()
                
            elif opcion == "6":
                lista.mostrar_atras()
                
            elif opcion == "7":
                lista.mostrar_adelante()
                lista.mostrar_atras()
                
            elif opcion == "8":
                cantidad = lista.contar_elementos()
                print(f"\n La lista tiene {cantidad} elemento(s)")
                
            elif opcion == "9":
                print("\n ¡Gracias por usar el programa! Hasta pronto.")
                break
                
            else:
                print("\n  Opción no válida. Por favor elige un número del 1 al 9.")
                
        except KeyboardInterrupt:
            print("\n\n Programa interrumpido. ¡Hasta pronto!")
            break
        except Exception as e:
            print(f"\n  Error: {e}")


# Ejecutar el programa
if __name__ == "__main__":
    main()