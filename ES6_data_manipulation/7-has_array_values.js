// This script returns a boolean and the array elements exist within set

export default function hasValuesFromArray (set, array) {
  // Use the every method to check if all elements of the array are in the set
  return array.every((element) => set.has(element));
}
