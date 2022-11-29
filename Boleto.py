class Boleto:
    def __init__(self, codigo, asiento, total, cliente):
        self.codigo = codigo
        self.asiento = asiento
        self.total = total
        self.cliente = cliente
        self.usado = False

    def __str__(self):
        return f'Codigo: {self.codigo}, Usado: {self.usado}, Asiento: {self.asiento}, Total: {self.total}, Cliente: {self.cliente}'