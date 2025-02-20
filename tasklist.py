# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

# Função para adicionar tarefa
def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

# Função para listar tarefas
def listar_tarefas(tarefas):
    if tarefas:
        print("\nTarefas:")
        for idx, tarefa in enumerate(tarefas, 1):
            print(f"{idx}. {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")

# Função para remover tarefa
def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida}' removida!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido.")

# Função principal
def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            remover_tarefa(tarefas)
        elif opcao == '4':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Iniciar o programa
if __name__ == "__main__":
    main()
