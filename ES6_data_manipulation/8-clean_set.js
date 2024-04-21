// This script returns a string of all set values ​​starting with a specific string (startString)
export default function cleanSet (set, startString) {
  // Initialize an empty array to store the filtered elements
  const filterValues = [];

  // Check if startString is undefined
  const isStartStringUndefined = typeof startString === 'undefined';

  // Iterate over each value in the set
  for (const value of set) {
    // If startString is undefined or the value starts with startString
    if (isStartStringUndefined || value.startsWith(startString)) {
      // Add the rest of the string to the filterValues array
      filterValues.push(value.slice(startString?.length));
    }
  }

  // Join the filtered elements with the separator '-' to form the result string
  const result = filterValues.join('-');

  return result;
}
