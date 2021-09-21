export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents.filter((obj1) => obj1.location === city).map((obj) => {
    const rtn = obj;
    for (const gradeObj of newGrades) {
      if (gradeObj.studentId === obj.id) {
        rtn.grade = gradeObj.grade;
      } else if (obj.grade === undefined) {
        rtn.grade = 'N/A';
      }
    }
    return rtn;
  });
}
