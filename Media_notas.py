# Função para cadastrar as notas dos alunos
def cadastrar_notas():
    Notas = []  # Inicializa uma lista vazia para armazenar as notas
    while True:  # Loop infinito até que o usuário decida parar
        nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))  # Solicita uma nota
        if nota == -1:  # Se o usuário digitar -1, encerra o loop
            break
        elif nota > 10:  # Verifica se a nota é maior que 10
            print("\nO número indicado é maior que o permitido (máximo 10).")
        elif nota < 0: # Verifica se a nota é menor que 0
            print("\nNota inválida. Digite um valor entre 0 e 10 ou -1 para encerrar.")
        else:
            Notas.append(nota)  # Adiciona a nota à lista apenas se for válida
    return Notas  # Retorna a lista de notas cadastradas
# Função para calcular a média das notas
def calcular_media(notas):
    if len(notas) == 0:  # Verifica se a lista está vazia para evitar divisão por zero
        return 0  # Retorna 0 se não houver nenhuma nota
    return sum(notas) / len(notas)  # Retorna a média das notas

# Função para determinar a situação do aluno com base na média
def determinar_situacao(media):
    if media >= 7:  # Se a média for maior ou igual a 7
        return "Aprovado"  # Retorna "Aprovado"
    else:
        return "Reprovado"  # Caso contrário, retorna "Reprovado"

# Função para exibir o relatório final
def exibir_relatorio(notas, media, situacao):
    print("\n RELATÓRIO FINAL")  # Título do relatório
    print("Notas inseridas:", notas)  # Exibe todas as notas cadastradas
    print(f"Média: {media:.2f}")  # Exibe a média com duas casas decimais
    print("Situação do aluno:", situacao)  # Exibe se o aluno foi aprovado ou reprovado

# Função principal que coordena a execução do programa
def main():
    print("Sistema de Gestão de Notas ")  # Mensagem de boas-vindas
    notas = cadastrar_notas()  # Chama a função para cadastrar notas
    media = calcular_media(notas)  # Calcula a média das notas
    situacao = determinar_situacao(media)  # Determina a situação do aluno
    exibir_relatorio(notas, media, situacao)  # Exibe o relatório final

# Chamada da função principal para iniciar o programa
main()