// returns an updated map for all items with an initial quantity of 1.

export default function updateUniqueItems(map) {
  // Check if the argument is a Map
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  // Iterate over each entry in the map and update the quantity if it is 1
  map.forEach((quantity, item) => {
    if (quantity === 1) {
      map.set(item, 100);
    }
  });
}
