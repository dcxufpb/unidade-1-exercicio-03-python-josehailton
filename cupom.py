nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def imprime_dados_loja():
    # Implemente aqui
    nome_loja
    s01 = ("%s, %d %s" % (logradouro, numero, complemento))
    s02 = ("%s - %s - %s" % (bairro, municipio, estado))
    s03 = ("CEP:%s Tel %s" % (cep, telefone))
    observacao
    s04 = ("CNPJ: %s" % cnpj)
    s05 = ("IE: %s" % inscricao_estadual)
    stringResultado = "{}\n{}\n{}\n{}\n{}\n{}".format(nome_loja, s01, s02, s03, observacao, s04, s05)
    return print(stringResultado) 
