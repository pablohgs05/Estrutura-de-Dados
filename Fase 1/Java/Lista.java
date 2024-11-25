package org.example;

// define um nó que contém o nome e uma referência ao próximo elemento da fila
class Lista {
    String nome;
    Lista proximo; // ponteiro para o próximo nó na fila

    public Lista(String nome) {
        this.nome = nome; // inicializa o nó com o nome recebido
        this.proximo = null; // inicializa a referência para o próximo nó como null
    }
}

// implementa os métodos de uma fila
class Fila {
    // adiciona uma nova pessoa ao final da fila
    public Lista adicionar(String nome, Lista primeiro, Lista ultimo) {
        Lista novo = new Lista(nome); // cria um novo nó
        if (primeiro == null) { // verifica se a fila está vazia
            primeiro = novo; // atualiza o início da fila
            ultimo = novo; // atualiza o final da fila
        } else {
            ultimo.proximo = novo; // liga o último nó ao novo
            ultimo = novo; // atualiza o último nó
        }
        return primeiro; // retorna o novo início da fila
    }

    // remove a primeira pessoa da fila
    public Lista remover(Lista primeiro, Lista ultimo) {
        if (primeiro == null) { // verifica se a fila está vazia
            throw new IllegalStateException("Fila vazia");
        }
        primeiro = primeiro.proximo; // atualiza o início para o próximo nó
        if (primeiro == null) { // se a fila ficar vazia, atualiza o final
            ultimo = null;
        }
        return primeiro; // retorna o novo início da fila
    }

    // retorna o nome da primeira pessoa na fila
    public String topo(Lista primeiro) {
        if (primeiro == null) { // verifica se a fila está vazia
            throw new IllegalStateException("Fila vazia");
        }
        return primeiro.nome; // retorna o nome do primeiro nó
    }

    // verifica se a fila está vazia
    public boolean isEmpty(Lista primeiro) {
        return primeiro == null; // retorna true se o início da fila for null
    }
}