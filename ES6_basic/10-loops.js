export default function appendToEachArrayValue(array, appendString) {
  const arrays = [];
  for (const value of array) {
    arrays.push(appendString + value);
  }

  return arrays;
}
