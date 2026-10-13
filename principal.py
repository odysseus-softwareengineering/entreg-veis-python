"""Script principal: demonstra importação e reaproveitamento de módulos."""
import calculadora
import utilidades
import estatistica as est


def main():
    """Executa exemplos das funções importadas."""
    print(f"Soma: {calculadora.somar(12, 8):.2f}")
    print(f"Subtração: {calculadora.subtrair(12, 8):.2f}")
    print(f"Multiplicação: {calculadora.multiplicar(12, 8):.2f}")

    resultado_divisao = calculadora.dividir(12, 0)
    if resultado_divisao is None:
        print("Divisão não realizada: divisor igual a zero.")
    else:
        print(f"Divisão: {resultado_divisao:.2f}")

    print(f"30 °C em Fahrenheit: {utilidades.converter_celsius_para_fahrenheit(30):.1f}")
    print(f"Senha válida: {utilidades.validar_senha('python123')}")
    print(f"Total da caixa: R$ {utilidades.calcular_total_caixa(4.5, 9.9, 3.0):.2f}")
    print(f"Ficha: {utilidades.criar_ficha_aluno(nome='Ana', turma='A', nota=8.5)}")

    valores = [2, 4, 4, 8, 10]
    print(f"Média: {est.media(valores):.2f}")
    print(f"Mediana: {est.mediana(valores):.2f}")
    print(f"Moda(s): {est.moda(valores)}")
    print(f"Fatorial de 5: {est.fatorial(5)}")
    print(est.relatorio("Resumo", "Funções importadas", "Exemplos executados", separador="="))


if __name__ == "__main__":
    main()
