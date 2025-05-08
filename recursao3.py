def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau(nome)


def sauda2(nome):
    print("Como vai " + nome + "?")


def tchau(nome):
    print("ok, tchau!")

sauda("Hugo")