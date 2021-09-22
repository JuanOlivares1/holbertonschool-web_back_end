export default function updateUniqueItems(mapObject) {
  if (mapObject.constructor !== Map) {
    throw new Error('Cannot process');
  }
  for (const obj of mapObject) {
    if (obj[1] === 1) {
      mapObject.set(obj[0], 100);
    }
  }
  return mapObject;
}
