export default function updateUniqueItems(arr) {
  const uniqueItems = new Set(arr);
  for (const item of uniqueItems) {
    if (item === 'Apples') {
      uniqueItems.delete(item);
      uniqueItems.add('Apples');
    }
  }
  return uniqueItems;
}
