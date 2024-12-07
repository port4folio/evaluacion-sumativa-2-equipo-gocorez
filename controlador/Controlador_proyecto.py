from modelo.Proyecto import Proyecto

def agregar_proyecto(self, nombre, descripcion, fecha_inicio):
        nuevo_proyecto = Proyecto(nombre, descripcion, fecha_inicio)  # Usa el constructor de Proyecto
        self.proyectos.append(nuevo_proyecto)
        print(f"Proyecto '{nombre}' agregado.")

def editar_proyecto(self, nombre, nuevo_nombre=None, nueva_descripcion=None, nueva_fecha_inicio=None):
    for proyecto in self.proyectos:
        if proyecto.nombre == nombre:
            if nuevo_nombre:
                proyecto.nombre = nuevo_nombre
            if nueva_descripcion:
                proyecto.descripcion = nueva_descripcion
            if nueva_fecha_inicio:
                proyecto.fecha_inicio = nueva_fecha_inicio
            print(f"Proyecto '{nombre}' editado.")
            return
    print(f"Proyecto '{nombre}' no encontrado.")

def eliminar_proyecto(self, nombre):
    for proyecto in self.proyectos:
        if proyecto.nombre == nombre:
            self.proyectos.remove(proyecto)
            print(f"Proyecto '{nombre}' eliminado.")
            return
    print(f"Proyecto '{nombre}' no encontrado.")

def mostrar_proyectos(self):
    if not self.proyectos:
        print("No hay proyectos para mostrar.")
        return
    for proyecto in self.proyectos:
        print(f"Nombre: {proyecto.nombre}, Descripción: {proyecto.descripcion}, Fecha de Inicio: {proyecto.fecha_inicio.strftime('%Y-%m-%d')}")