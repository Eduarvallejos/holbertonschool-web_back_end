export default function createEmployeesObject(departmentName, employees) {
  const employeesobject = {};

  employeesobject[departmentName] = employees;

  return employeesobject;
}
