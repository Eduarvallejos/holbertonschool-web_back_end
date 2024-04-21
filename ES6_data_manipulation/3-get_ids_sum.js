// This script returns the sum of all student ids.

export default function getStudentIdsSum(liststudents) {
  return liststudents.reduce((acumulador, student) => acumulador + student.id, 0);
}
