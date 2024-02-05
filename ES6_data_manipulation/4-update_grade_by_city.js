export default function updateStudentGradeByCity(students, city, newGrades) {
  let arr = [];
  arr = students.map((student) => {
    if (student.location === city) {
      let grade = 'N/A';
      newGrades.forEach((dict) => {
        if (student.id === dict.studentId) grade = dict.grade;
      });
      return { ...student, grade };
    }
    return null;
  }).filter((result) => result !== null);

  return arr;
}
