from datetime import datetime as dt
from random import randint

class Pessoa:
    #def falar(self):
    #    print(r'Pessoa está falando...')
    
    ano_atual = int(dt.strftime(dt.now(), '%Y'))
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome    = nome
        self.idade   = idade
        self.comendo = comendo
        self.falando = falando
        
        variavel = 'valor qualquer'
        
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
              
    def parar_falar(self):
        if not self.falando:
              print(f'{self.nome} não está falando')
              return
        print(f'{self.nome} parou de falar')
        self.falando = False
        
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo=False
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
        
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)      
        
    @staticmethod
    def gera_id():
        return randint(10000, 99999)

class Produto:
    def __init__(self, nome, preco):
        self.nome    = nome
        self.preco   = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    ##  Getter
    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    ##  Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

class A:
    vc = 123

class BaseDeDados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes']  = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')