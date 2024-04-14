export default function divideFunction(numerator, denominator) {
  // Check if the denominator is equal to 0
  if (denominator === 0) {
    // If equal to 0, throw an error
    throw new Error('cannot divide by 0');
  } else {
    // If the denominator is not equal to 0, return the result of the division
    return numerator / denominator;
  }
}
