export default function createInt8TypedArray(length, position, value) {
  if (position > length) {
    throw new Error('Position outside range');
  }
  const int32View = new Int8Array(length);
  int32View[position] = value;
  return new DataView(int32View.buffer);
}
