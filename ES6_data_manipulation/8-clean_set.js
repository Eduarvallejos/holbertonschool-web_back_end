// This script returns a string of all set values ​​starting with a specific string (startString)

export default function cleanSet(set, startString) {
  // Initialize an empty array to store filtered elements
  const filtervalues = [];
  // Iterate over each value in the set
  for (const valor of set) {
    // Check if the value starts with the specified startString
    if (valor.startsWith(startString)) {
      // Append the rest of the string to the filteredValues array
      filtervalues.push(valor.slice(startString.length));
    }
  }
  // Join the filtered values with '-' separator to form the result string
  const result = filtervalues.join('-');

  return result;
}
