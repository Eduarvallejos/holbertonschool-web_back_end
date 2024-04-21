// This script returns an array of objects located in a specific city.
export default function getStudentsByLocation(liststudents, city) {
  return liststudents.filter((student) => student.location === city);
}
