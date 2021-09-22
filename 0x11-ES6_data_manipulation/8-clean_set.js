export default function cleanSet(set, startString) {
  if (!startString || set.size === 0) {
    return '';
  }
  const rtn = [];
  for (const word of set) {
    if (word.startsWith(startString)) {
      rtn.push(word.slice(startString.length, word.length));
    }
  }
  return rtn.join('-');
}
