// This script returns students from a specific city with their new grade

export default function updateStudentGradeByCity(liststudents, city, newGrades) {
  // Filter students who are in the specific city
  const studentsInCity = liststudents.filter(student => student.location === city);
  // Map about students in the city and update their grades
  const updateStudents = studentsInCity.map(student => {
    // Check if there is a new grade for the student in newGrades
    const newGrade = newGrades.find(grade => grade.studentId === student.id);
    // If a new rating is found, update it; otherwise set it to N/A
    return {
      id: student.id,
      firstName: student.firstName,
      location: student.location,
      grade: newGrade ? newGrade.grade : 'N/A'
    };
  });
  return updateStudents;
}
