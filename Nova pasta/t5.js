function inverterString(texto) {
    let stringInvertida = "";
    for (let i = texto.length - 1; i >= 0; i--) {
        stringInvertida += texto[i];
    }
    return stringInvertida;
}

let texto = "Exemplo de string";
let resultado = inverterString(texto);
console.log("String original:", texto);
console.log("String invertida:", resultado);
