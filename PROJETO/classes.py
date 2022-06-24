class Usuario:
    def __init__(self, nome, idade, email, cpf, senha):
        self._nome = nome
        self._idade = idade
        self._email = email
        self._cpf = cpf
        self._senha = senha

    
    def __repr__(self):
        return ('\nNome: {} - Idade: {} - Email: {} - CPF: {} - Senha: {}'.format(self._nome, self._idade, self._email, self._cpf, self._senha))

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        print('Erro. Utilize o método novo_nome()!')

    def novo_nome(self, nome_novo):
        if nome_novo != '':
            self._nome = nome_novo

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def nome(self, idade):
        print('Erro. Utilize o método nova_idade()!')

    def nova_idade(self, nova_idade):
        if nova_idade != '':
            self._idade = nova_idade

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        print('Erro. Utilize o método novo_email()!')

    def novo_email(self, novo_email):
        if novo_email != '':
            self._email = novo_email

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        print('Erro. Utilize o método nova_senha()!')

    def nova_senha(self, nova_senha):
        if nova_senha != '':
            self._senha = nova_senha
    
    @property
    def cpf(self):
        return self._cpf

    