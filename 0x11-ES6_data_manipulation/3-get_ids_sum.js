export default function getStudentIdsSum(getListStudents) {
  return getListStudents.map((obj) => obj.id).reduce((prev, curr) => prev + curr);
}
