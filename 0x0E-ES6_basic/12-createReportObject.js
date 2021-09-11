export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments: function getDptsNum() {
      return Object.keys(employeesList).length;
    },
  };
}
