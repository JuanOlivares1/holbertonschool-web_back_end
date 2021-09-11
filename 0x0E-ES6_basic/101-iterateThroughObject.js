export default function iterateThroughObject(reportWithIterator) {
  let returnString = '';
  let counter = 1;
  for (const idx of reportWithIterator) {
    if (counter === reportWithIterator.length) {
      returnString += `${idx}`;
    } else {
      returnString += `${idx} | `;
      counter += 1;
    }
  }
  return returnString;
}
