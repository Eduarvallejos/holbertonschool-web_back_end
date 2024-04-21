// This script returns a string of all set values ​​starting with a specific string (startString)

export default function cleanSet(set, startString) {
    // Convertir el conjunto (Set) en un array utilizando el operador de propagación (...)
    const arrayFromSet = [...set];
    
    // Filtrar los elementos del array que empiezan con la cadena especificada
    const filteredValues = arrayFromSet.filter(element =>
        element.startsWith(startString)
    );
    
    // Unir los elementos filtrados en un string separados por '-'
    const result = filteredValues.join('-');

    return result;
}

