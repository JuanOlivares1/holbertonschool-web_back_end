export default function createIteratorObject(report) {
  const newList = [];
  for (const idx of Object.values(report.allEmployees)) {
    for (const i of idx) {
      newList.push(i);
    }
  }
  return newList;
}
