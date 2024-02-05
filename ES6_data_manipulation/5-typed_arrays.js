export default function createInt8TypedArray(length, position, value) {
  const arr = new Int8Array(length);
  if (position > length) throw Error('Position outside range');
  arr[position] = value;
  const { buffer } = arr;
  return new DataView(buffer, 0, length);
}
