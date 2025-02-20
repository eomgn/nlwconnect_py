class MinhaClase:
    def __enter__(self):
        print('Entrando...')
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saindo...')

with MinhaClase() as mc:
    print('Dentro do bloco with')