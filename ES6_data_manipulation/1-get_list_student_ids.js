// This script returns arrays of identifiers

export default function getListStudentIds(argument) {
  if (!Array.isArray(argument)) {
    return [];
  }

  return argument.map((students) => students.id);
}
