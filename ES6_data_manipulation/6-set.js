export default function setFromArray(values) {
  const set = new Set();
  values.forEach((element) => set.add(element));
  return set;
}
