from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.0, 'O molhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim',10.0,'Gelada','Pequeno','Pudim de leite condensado, receita especial da vovó')
sobremesa_pudim.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()