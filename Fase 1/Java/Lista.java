package org.example;

class Lista {
    String nome;
    Lista proximo;

    public Lista(String nome) {
        this.nome = nome; 
        this.proximo = null; 
    }
}

class Fila {
    public Lista adicionar(String nome, Lista primeiro, Lista ultimo) {
        Lista novo = new Lista(nome);
        if (primeiro == null) {
            primeiro = novo;
            ultimo = novo;
        } else {
            ultimo.proximo = novo;
            ultimo = novo; // atualiza o último nó
        }
        return primeiro; // retorna o novo início da fila
    }

    // remove a primeira pessoa da fila
    public Lista remover(Lista primeiro, Lista ultimo) {
        if (primeiro == null) {
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