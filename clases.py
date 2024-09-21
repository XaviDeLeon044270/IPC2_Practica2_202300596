class Auto:
    autos = []

    def __init__(self, tipo, marca, modelo, descripcion, precio, cantidad, urlImagen):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.urlImagen = urlImagen

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}, Descripción: {self.descripcion}, Precio: {self.precio}, Cantidad: {self.cantidad}, URL Imagen: {self.urlImagen}"

    @classmethod
    def agregarAuto(cls, tipo, marca, modelo, descripcion, precio, cantidad, urlImagen):
        cls.autos.append(Auto(tipo, marca, modelo, descripcion, precio, cantidad, urlImagen))
        return cls.autos

    @classmethod
    def eliminarAuto(cls, idTipo_eliminar):
        cls.autos = [auto for auto in cls.autos if auto.tipo != idTipo_eliminar]

    @classmethod
    def obtenerAutos(cls):
        return cls.autos
    

