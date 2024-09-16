<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.4/lodash.min.js"></script>
    <title>Menu</title>
</head>
<body>
    
</body>
<script>

/* ENUNCIADO
Build out a dinner menu in JAVASCRIPT. Here are your instructions to build that dinner.
Bottega dinner
Have the Main Menu and a Sides Menu
You get one entree and two side choices at regular cost.
- show them the entire menu (print out)
- A user selects an entree.
- “Waitress” makes a comment based on their selection
- comment can either be a comparison of the two items, or random comment pulled from a comment vault.
- Tell them the price
- repeat the above options for side choices (comment and a price)
- total up the cost

BONUS
Have breakfast, lunch, and dinner menu. Breakfast has different items, lunch and dinner have the same items but are different prices.

BONUS: Allow for item customization (how items are prepared, decide additional cost implications)
*/

const menuPrincipal = [
    {
        categoria: "ensalada",
        options: [
            {nombre: "ensalada cesar", precio: 6.50},
            {nombre: "ensalada ilustrada", precio: 6.75},
        ]
    },
    {
        categoria: "pasta",
        options: [
            {nombre: "macarrones carbonara", precio: 9.30},
            {nombre: "espaguetis boloñesa", precio: 7.20},
            {nombre: "raviolis a la romana", precio: 5.60},
        ]
    },
    {
        categoria: "verdura",
        options: [
            {nombre: "menestra verdura", precio: 10.00},
            {nombre: "sopa de calabaza", precio: 4.40},
            {nombre: "alcachofas en salsa", precio: 7.50},
    ]
    },
];

const menuGuarnicion = [
    {nombre: "patatas fritas", precio: 2.00},
    {nombre: "ensalada", precio: 3.00},
    {nombre: "boniato frito", precio: 2.00},
    {nombre: "alubias", precio: 4.00},
    {nombre: "pimientos del piquillo", precio: 2.00},
];  

const menuDesayuno = [
    {
        categoria: "tostadas",
        options: [
            {nombre: "pan tumaca", precio: 6.20},
            {nombre: "mantequilla y mermelada", precio: 7.20},
            {nombre: "nutella", precio: 8.00},
        ]
    },
    {
        categoria: "croissants",
        options: [
            {nombre: "mantequila y mermelada", precio: 7.20},
            {nombre: "jamons york y queso", precio: 8.20},
            {nombre: "solo", precio: 6.00},
        ]
    }
];


/*FUNCTION 1 - Elegir Menu*/

const elegirMenu = () => {
    let ans;
    let goodAns = false;
    const choices = ["1", "2", "3", "desayuno", "comida", "cena"];

    do{
        ans = prompt(`Buenas! Qué menú desea escoger?
        1. Desayuno
        2. Comida
        3. Cena`);

        if(ans === null || choices.includes(ans.toLowerCase())){
            goodAns = true;
        } else {
            alert("Esa no es una buena opción...");
        }
    } while (!goodAns);

    if(ans === null) return ans;

    ans = ans.toLowerCase();

    if(ans === "1" || ans === "desayuno") return "desayuno";
    if(ans === "2" || ans === "comida") return "comida";
    if(ans === "3" || ans === "cena") return "cena";
}


/*FUNCTION 2 - VER Menu*/

const verMenu = (menu) => {

    if(menu[0].categoria){
        for(item of menu){
            console.log(`\n${item.categoria.toUpperCase()}`);
        
            verMenu(item.options);
        }

    } else {
        for(item of menu){
            console.log(`\t - ${item.nombre}: \t ${item.precio}€`);
        }
    }
}


/*FUNCTION 3 - HACER Eleccion*/

const hacerEleccion = (menu) => {
    if(menu[0].categoria){
        let optionsMenu = [];

        for(item of menu){
            optionsMenu.push(...item.options);
        }

        return hacerEleccion(optionsMenu);

    } else {
        let choice; 

        do{
            choice = prompt("Elige tu opción: ");
            if(choice !== null){
                choice = menu.find(obj => obj.nombre === choice.toLowerCase());
            }

            if(choice == undefined){
                console.log("\n Disculpe, eso no es una selección dentro del menú\n");
            }

        } while(choice === undefined);

        return choice || "\n Disculpe, no tenemos lo que usted quiere...";
    }
};


/*FUNCTION 4 - HACER Comentario*/

const hacerComentario = (choice, total) => {

    if(typeof choice !== "string"){
        console.log(`\nHas elegido ${choice.nombre.toUpperCase()}, buena elección!`);
        console.log(`\n El precio es de ${choice.precio}€.`);

        return total + choice.precio;

    } else {
        console.log(choice);
    }
};


/*FUNCTION 5 - PEDIR Opciones*/

const pedirOpciones = (menu, times) => {
    let totalPrecio = 0;

    for(let i=0; i<times; i++){
        let choice = hacerEleccion(menu);
        totalPrecio = hacerComentario(choice, totalPrecio);
    }
    return totalPrecio;

};


const eleccionMenu = elegirMenu();

let totalPrecio = 0;

if(eleccionMenu === "desayuno"){
    console.log("DESAYUNO BOTTEGA\n");

    console.log(`\n---MENU DESAYUNO---`);
    console.log("*Todos los desayunos incluyen café y zumo a elegir.")
    verMenu(menuDesayuno);

    totalPrecio += pedirOpciones(menuDesayuno, 2)

} else if(eleccionMenu === "comida"){
    console.log("COMIDA BOTTEGA\n");

    const modificarPrecio = (menu) => {
        if(menu[0].categoria){
            for(item of menu){
                modificarPrecio(item.options);
            }
        } else {
            for(item of menu){
                item.precio = Math.round((item.precio * 0.8)*100) / 100;
            }
        }
        return menu;
    }

    const mod_menuComida = modificarPrecio([...menuPrincipal]);
    const mod_MenuGuarnicion = modificarPrecio([...menuGuarnicion]);

    console.log(`\n MENÚ PRINCIPAL`);
    verMenu(mod_menuComida);

    totalPrecio += pedirOpciones(mod_menuComida, 1);

    console.log(`\n Elige ahora tu primera opción del MENÚ GUARNICIÓN`);
    verMenu(mod_MenuGuarnicion);

    totalPrecio += pedirOpciones(mod_MenuGuarnicion, 1);

    console.log(`\n Elige tu segunda opción del MENÚ GUARNICIÓN`);
    verMenu(mod_MenuGuarnicion);

    totalPrecio += pedirOpciones(mod_MenuGuarnicion, 1);

/*Aquí en lugar de repetir el bloque de codigo, podriamos aplicar:
totalPrecio += pedirOpciones(sideLunchMenu, 2) y de ese modo se pasa el valor 2 a "veces"
y se eligen dos platos de guarnición.

El ejemplo está en el SIGUIENTE CONDICIONAL:
 */

} else if(eleccionMenu === "cena"){
    console.log("CENA - BOTTEGA\n");

    console.log(`\nElige ahora tu primera opción del MENÚ CENA`);
    verMenu(menuPrincipal);

    totalPrecio += pedirOpciones(menuPrincipal, 1);

    console.log(`\nElige dos opciones del MENÚ GUARNICIÓN:`)
    verMenu(menuGuarnicion);

    totalPrecio += pedirOpciones(menuGuarnicion, 2);
};

totalPrecio = Math.round(totalPrecio * 100) / 100;
console.log(`\n El precio TOTAL es ${totalPrecio || 0}€`);


</script>
</html>
