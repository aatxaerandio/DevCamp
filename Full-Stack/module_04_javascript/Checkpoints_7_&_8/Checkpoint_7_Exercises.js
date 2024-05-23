//Crea una función que acepte 4 argumentos:
//Suma los dos primeros argumentos, luego los dos segundos y multiplicalos.
//Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". 
//Si es más pequeño, la consola registra "¡El número es menor que 50!"

function numeros(a, b, c, d) {
  var sum_1 = a + b;
  var sum_2 = c + d;
  var num_total = sum_1 * sum_2;

  if (num_total > 50) {
    console.log("¡El número es mayor que 50!");
  } else {
    console.log("¡El número es menor que 50!");
  }
}

numeros(a, b, c, d)


// Se crea una función que se llama "numeros" y dentro de ella tres variables son los requisitos de sumas y multiplicaciones.
// Mas tarde se crea el condicional usando "if" y "else", imprimiendo cadenas diferentes segun el valor de "num_total".
// Para llamar a la funcion, simplemente poner los valores de a, b, c, d y listo, nos devolverá una cadena u otra.
// A modo de mejoría, se podría añadir un "console.log(num_total) debajo de la variable "nuM_total", para que ya de paso nos dé el valor total de la multiplicación.
