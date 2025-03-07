# objeto
class Pessoa:
    # init = parametro dos atributos
    def __init__(self, nome_completo, data_de_nascimento, cpf, rg, genero, cor, telefone, trabalhando=False):
        self.nome_completo = nome_completo
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.rg = rg
        self.genero = genero
        self.cor = cor
        self.telefone = telefone
        self.trabalhando = trabalhando

    def apresentar(self):
        # apresentacao (listagem) dos atributos
        print(f'\n Prazer, meu nome é {self.nome_completo}, \n nasci no dia {self.data_de_nascimento},'
              f'\n os números do meu CPF são: {self.cpf}, \n e os do meu RG: {self.rg},'
              f'\n sou do gênero {self.genero}, \n e minha cor é {self.cor},'
              f'\n caso precise, anote meu número: {self.telefone}')
        if self.trabalhando:
            print("Trabalhando")
        else:
            print("Não está trabalhando")

    def trabalhar(self):
        if self.trabalhando:
            self.trabalhando = True
            print(f'{self.nome_completo} começou a trabalhar')
        else:
            print(f'{self.nome_completo} já está trabalhando')


class Estudante(Pessoa):
    def __init__(self, nome_completo, escola, turma, numero_chamada, registro_matricula, data_de_nascimento, genero, cpf, rg, email, telefone, telefone_pais):
        super().__init__(nome_completo, data_de_nascimento, cpf, rg, genero, telefone)
        self.escola = escola
        self.turma = turma
        self.numero_chamada = numero_chamada
        self.registro_matricula = registro_matricula
        self.email = email
        self.telefone_pais = telefone_pais
        self.estudando = True
        self.intervalo = False
        self.casa = False

    def apresentar(self):
        print(
            f'Prazer, me chamo {self.nome_completo}, estudo na escola {self.escola}, na turma do {self.turma}, meu número de chamada é {self.numero_chamada}, e meu registro escolar é {self.registro_matricula}'
            f'\n nasci no dia {self.data_de_nascimento}, sou do gênero {self.genero}, \n os números do meu CPF são: {self.cpf} e os do meu RG: {self.rg},'
            f'\n caso precise, aqui está meu email: {self.email}, \n meu número de telefone: {self.telefone} \n e o telefone dos meus pais {self.telefone_pais}')
        if self.estudando:
            print(f'{self.nome_completo} está na escola {self.escola} e vai começar a estudar')
        else:
            print(f'{self.nome_completo} não está em horário de aula')

        if self.intervalo:
            print(f'{self.nome_completo} está no intervalo')
        else:
            print(f'{self.nome_completo} não está no intervalo')

        if self.casa:
            print(f"{self.nome_completo} está em casa descansando")
        else:
            print(f'{self.nome_completo} não está em casa')


    def estudar(self):
        if self.estudando:
            self.estudando = True
            print(f'{self.nome_completo} foi para a escola e está estudando')
        else:
            print(f'{self.nome_completo} não está em horário de aula')

    def pausar(self):
        if self.intervalo:
            self.intervalo = False
            print(f'{self.nome_completo} está no intervalo')
        else:
            print(f'{self.nome_completo} ainda está em horário de aula')

    def descansar(self):
        if self.estudando:
            self.estudando = True
            print(f'{self.nome_completo} ainda está em horário de aula')
        elif self.intervalo:
            self.intervalo = True
            print(f'{self.nome_completo} não está em horário de aula, mas está no intervalo na escola')
        else:
            print(f'{self.nome_completo} foi embora da escola, está em casa para descansar')


p1 = Pessoa("Mariana", "03/08/2007", "43314874820", "222222222", "feminino", "branca", "(18)99769-9870")
p1.apresentar()
p1.trabalhar()
p2 = Estudante("Mariana", "SESI", "3° ano do Ensino Médio", "26", "2479",
               "03/08/2007", "feminino", "43314874820", "222222222", "marianalopessilva387@gmail.com",
               "(18)99769-9870", "(18)99133-8807")
p2.apresentar()

