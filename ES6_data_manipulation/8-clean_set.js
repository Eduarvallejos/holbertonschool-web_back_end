// This script returns a string of all set values starting with a specific string (startString).

export default function cleanSet(set, startString = '') {
  // Initialize an empty array to store filtered values
  const filteredValues = [];

  if (startString === '') {
    // Return an empty string if startString has no value
    return '';
  }

  // Iterate over each value in the set
  for (const value of set) {
    // Check if the value starts with the specified startString
    if (value.startsWith(startString)) {
      // Append the rest of the string to the filteredValues array
      filteredValues.push(value.slice(startString.length));
    }
  }

  // Join the filtered values with '-' separator to form the result string
  const result = filteredValues.join('-');

  return result;
}
