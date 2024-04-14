export default function guardrail(mathFunction) {
  // Create an array to store the values and messages.
  const queue = [];

  try {
    // Execute the mathFunction function and add its return value to the array
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // If the function throws an error, add the error message to the array
    queue.push(`Error: ${error.message}`);
  } finally {
    // Add the processing message to the array,
    // regardless of whether the function was executed or an error was caught
    queue.push('Guardrail was processed');
  }
  // Return the resulting array
  return queue;
}
