# Sistema de Gerenciamento de Vendas (Simulador de Loja)

Este projeto é uma aplicação simples em Python que simula o atendimento em uma loja de eletrônicos, permitindo calcular o valor final de uma compra com base em descontos e métodos de pagamento.

## Lógica de Funcionamento (Passo a Passo)
1. **Inicialização**: O sistema define os preços fixos dos produtos (memória interna).
2. **Entrada de Dados**: O usuário informa seu nome e escolhe um produto através de um código numérico.
3. **Validação**: O sistema verifica se o código do produto é válido.
4. **Processamento**: 
   - O sistema identifica o preço do item escolhido.
   - Pergunta ao usuário a forma de pagamento.
   - Aplica um desconto de 10% se for pagamento à vista (Pix/Dinheiro) ou mantém o preço se for parcelado.
5. **Saída**: Exibe um resumo da compra, incluindo o nome do cliente, o produto escolhido e o valor final calculado.
## Como Executar
1. Certifique-se de ter o Python instalado (versão 3.10 ou superior recomendada).
2. Baixe o arquivo `app.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python app.py
