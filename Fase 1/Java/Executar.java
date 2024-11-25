package org.example;

// executa operações na fila simulando uma fila de lotérica
public class Executar {
    public static void main(String[] args) {
        Lista primeiro = null;
        Lista ultimo = null;
        int tamanho = 0;

        Fila fila = new Fila(); // cria uma nova fila

        primeiro = fila.adicionar("Manoel", primeiro, ultimo);
        ultimo = primeiro; // atualiza o último nó
        tamanho++; // incrementa o tamanho da fila

        primeiro = fila.adicionar("Joseval", primeiro, ultimo);
        ultimo = ultimo.proximo;
        tamanho++;

        primeiro = fila.adicionar("Enzo", primeiro, ultimo);
        ultimo = ultimo.proximo;
        tamanho++;

        System.out.println("Primeira pessoa na fila: " + fila.topo(primeiro));
        System.out.println("Tamanho da fila: " + tamanho);

        // remove o primeiro elemento, se a fila não estiver vazia
        if (tamanho > 0) {
            primeiro = fila.remover(primeiro, ultimo);
            tamanho--; // decrementa o tamanho da fila

            System.out.println("Pessoa removida: Manoel");
            System.out.println("Primeira pessoa após remoção: " + fila.topo(primeiro));
            System.out.println("Tamanho da fila após remoção: " + tamanho);
        }
    }
}
