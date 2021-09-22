export default function cleanSet(set, startString) {
  if (!startString
      || typeof startString !== 'string'
      || typeof set !== 'object') {
    return '';
  }
  const rtn = [];
  for (const word of set) {
    if (word.startsWith(startString)) {
      rtn.push(word.slice(startString.length));
    }
  }
  return rtn.join('-');
}
