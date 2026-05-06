## 2. Conteúdo do arquivo `app.py`

```python
# --- Variáveis Internas (Sistema) ---
PRODUTO_1 = "Smartphone"
PRECO_1 = 2000.00
PRODUTO_2 = "Notebook"
PRECO_2 = 4500.00

def executar_sistema():
    print("--- BEM-VINDO À LOJA TECH ---")
    
    # --- Entrada de Dados (Usuário) ---
    nome_cliente = input("Digite seu nome: ")
    print(f"\nProdutos disponíveis:\n1. {PRODUTO_1} (R$ {PRECO_1})\n2. {PRODUTO_2} (R$ {PRECO_2})")
    
    escolha = input("Digite o código do produto (1 ou 2): ")
    
    # Variáveis de controle (Tipos: str, float, bool)
    produto_selecionado = ""
    valor_base = 0.0
    codigo_valido = True

    # --- Estrutura Condicional (Simulando Lógica de Seleção) ---
    if escolha == "1":
        produto_selecionado = PRODUTO_1
        valor_base = PRECO_1
    elif escolha == "2":
        produto_selecionado = PRODUTO_2
        valor_base = PRECO_2
    else:
        print("Erro: Código de produto inválido.")
        codigo_valido = False

    if codigo_valido:
        # --- Bônus: Menu Interativo e Validação ---
        print("\nFormas de Pagamento:")
        print("1. À vista (10% de desconto)")
        print("2. Parcelado (Preço normal)")
        
        pagamento = input("Escolha a opção (1 ou 2): ")
        
        # --- Processamento Matemático e Lógico ---
        valor_final = valor_base
        aplicou_desconto = False

        if pagamento == "1":
            # Operação matemática: Desconto de 10%
            valor_final = valor_base * 0.90
            aplicou_desconto = True
        
        # --- Saída de Resultados ---
        print("\n" + "="*30)
        print(f"RESUMO DA COMPRA")
        print(f"Cliente: {nome_cliente}")
        print(f"Produto: {produto_selecionado}")
        print(f"Valor Final: R$ {valor_final:.2f}")
        
        if aplicou_desconto:
            print("Status: Desconto de 10% aplicado com sucesso!")
        else:
            print("Status: Pagamento sem descontos.")
        print("="*30)

if __name__ == "__main__":
    executar_sistema()
