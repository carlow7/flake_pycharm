class FilaNormal:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha: str = 'none'

    def gerasenha(self) -> None:  # não retorna nada#
        self.senha = f'NM{self.codigo}'

    def resatafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self) -> None:
        self.resatafila()
        self.gerasenha()
        self.fila.append(self.senha)

    def chamaclient(self, caixa: int) -> int:
        client_atual: int = self.fila.pop(0)
        self.clientes_atendidos.append(client_atual)
        return (f'Cliente Atual: {client_atual} dirija ao caixa {caixa}')
