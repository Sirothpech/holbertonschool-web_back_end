export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.filter((newGrade) => newGrade.studentId === student.id)[0];
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A'
      };
    });
}
