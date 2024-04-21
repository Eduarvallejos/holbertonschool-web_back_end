// This script returns a new ArrayBuffer with an Int8 value at a specific position.

export default function createInt8TypedArray(length, position, value) {
  // Check if position is within the range of the array length
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);
  // Create a DataView to access and manipulate the ArrayBuffer
  const view = new DataView(buffer);
  // Set the Int8 value at the specified position
  view.setInt8(position, value);

  return view;
}
