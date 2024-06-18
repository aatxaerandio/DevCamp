/* EJERCICIOS PRÁCTICOS JAVASCRIPT */



/*Ejercicio 1
Cree un bucle for en JS que imprima cada nombre en esta lista. 
miLista = “velma”, “exploradora”, “jane”, “john”, “harry”.*/

let milista = ["velma", "exploradora", "jane", "john", "harry"]

for(let counter = 0; counter < milista.length; counter++){
  console.log(milista[counter]);
}

/*
velma
exploradora
jane
john
harry
*/





/*Ejercicio 2
Cree un bucle while que recorra la misma lista y también imprima los nombres.
Nota: Recuerda crear un contador para que el ciclo no sea infinito.*/

let milista = ["velma", "exploradora", "jane", "john", "harry"]

counter = 0;
while(counter < milista.length){
  console.log(milista[counter]);
  counter++;
}

/*
velma
exploradora
jane
john
harry
*/





/*Ejercicio 3
Cree una función de flecha que devuelva "Hola mundo".*/

const saludos = () => {
    console.log('Hola mundo');
  }
  

  saludos()  // Hola mundo
