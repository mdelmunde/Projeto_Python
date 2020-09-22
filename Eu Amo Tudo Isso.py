class cliente:

    def __init__(self, *args, **kwarg):
        self.nome = kwarg.get("nome", "")
        self.idade = kwarg.get("idade", 0)
        
        self.pedido = kwarg.get("pedido", object)

class pedido:
    
    def __init__(self, *args, **kwarg):
        self.itens = kwarg.get("itens", {})
        self.nPedido = kwarg.get("nPedido", object)


def inserir_cli_fila(cliente):
    if cliente.idade > 65:
        filaIdoso.append(cliente)
        filaPedidos.append(cliente.pedido)
    else:
        filaNormal.append(cliente)
        filaPedidos.append(cliente.pedido)
        
filaNormal = []
filaIdoso = []
filaPedidos =[]


PedidoMatheus = pedido(nPedido=1, itens="wopper")
PedidoDuda = pedido(nPedido=2, itens="rodeio")
PedidoMaria = pedido(nPedido=3, itens="cheddar duplo")

Matheus = cliente(nome="Matheus", idade=19, pedido=PedidoMatheus)
Duda = cliente(nome="Duda", idade=30, pedido=PedidoDuda)
Maria = cliente(nome="Maria", idade=76, pedido=PedidoMaria)


inserir_cli_fila(Matheus)
inserir_cli_fila(Duda)
inserir_cli_fila(Maria)

print('lista de pedidos')
for i in range(0,3):
    
    print(filaPedidos[i].nPedido, "-", filaPedidos[i].itens)


