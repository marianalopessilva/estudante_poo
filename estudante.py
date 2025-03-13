# objeto
class Pessoa:
    # init = parametro dos atributos
    def __init__(self, nome_completo, data_de_nascimento, cpf, rg, genero, cor, telefone, trabalhando=False):
        self.__nome_completo = nome_completo
        self.__data_de_nascimento = data_de_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self._genero = genero
        self._cor = cor
        self.__telefone = telefone
        self._trabalhando = trabalhando

    def get_nome_completo(self):
        return self.__nome_completo

    def get_data_de_nascimento(self):
        return self.__data_de_nascimento

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def get_genero(self):
        return self._genero

    def get_cor(self):
        return self._cor

    def get_telefone(self):
        return self.__telefone

    def is_trabalhando(self):
        return self._trabalhando


        # status = tenho que modificar o status da pessoa
    def set_trabalhar(self, status):
        # status = o que eu quero que a pessoa faça
        # status = true / not status = false
        if self._trabalhando and status:
            print(f'{self.__nome_completo} já está trabalhando')
        elif not self._trabalhando and status:
            self.__trabalhando = status
            print(f'{self.__nome_completo} começou a trabalhar')
        else:
            print(f'{self.__nome_completo} não precisa trabalhar')


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


class Estudante(Pessoa):
    def __init__(self, nome_completo, escola, turma, numero_chamada, registro_matricula, data_de_nascimento, genero,
                 cpf, rg, email,cor, telefone, telefone_pais):
        super().__init__(nome_completo, data_de_nascimento, cpf, rg, genero,cor, telefone)
        self.escola = escola
        self.turma = turma
        self.numero_chamada = numero_chamada
        self.registro_matricula = registro_matricula
        self.email = email
        self.telefone_pais = telefone_pais
        self.estudando = False
        self.intervalo = False
        self.descansando = True

    def apresentar(self):
        print(
            f'Prazer, me chamo {self.get_nome_completo()}, estudo na escola {self.escola}, na turma do {self.turma}, meu número de chamada é {self.numero_chamada}, e meu registro escolar é {self.registro_matricula}'
            f'\n nasci no dia {self.get_data_de_nascimento()}, sou do gênero {self.get_genero()}, \n os números do meu CPF são: {self.get_cpf()} e os do meu RG: {self.get_rg()},'
            f'\n caso precise, aqui está meu email: {self.email}, \n meu número de telefone: {self.get_telefone()} \n e o telefone dos meus pais {self.telefone_pais}')

        if self.estudando:
            print(f'{self.get_nome_completo()} está na escola {self.escola} e vai começar a estudar')
        else:
            print(f'{self.get_nome_completo()} não está em horário de aula')

        if self.intervalo:
            print(f'{self.get_nome_completo()} está no intervalo')
        else:
            print(f'{self.get_nome_completo()} não está no intervalo')

        if self.descansando:
            print(f"{self.get_nome_completo()} está em casa descansando")
        else:
            print(f'{self.get_nome_completo()} não está em casa')


        # status = tenho que modificar o status da pessoa
    def estudar(self, status):
        # status = o que eu quero que a pessoa faça
        # status = true / not status = false
        if self.estudando and status:
            print(f'{self.get_nome_completo()} já está na escola estudando')
        elif not self.estudando and status:
            self.estudando = status
            print(f'{self.get_nome_completo()} está indo para escola estudar')
        else:
            print(f'{self.get_nome_completo()} não está em horário de aula, está em casa descansando')


    def pausar(self):
        if self.intervalo:
            print(f'{self.get_nome_completo()} está no intervalo')
        else:
            print(f'{self.get_nome_completo()} ainda está em horário de aula')


    def descansar(self, status):
        # status = o que eu quero que a pessoa faça
        # status = true / not status = false
        if self.descansando and status:
            print(f'{self.get_nome_completo()} já está em casa descansando')
        elif not self.descansando and status:
            self.estudando = status
            print(f'{self.get_nome_completo()} está na saída da escola, indo para casa descansar')
        else:
            print(f'{self.get_nome_completo()} ainda está na escola estudando')


p2 = Estudante("Mariana", "SESI",
               "3°EM", "26",
               "2479", "03/08/2007",
               "feminino", "433.148.748-20",
               "222222222", "marianalopessilva387@gmail.com",
               "cor","(18)99769-9870", "(18)99133-8807")

p2.apresentar()
p2.descansar(True)

