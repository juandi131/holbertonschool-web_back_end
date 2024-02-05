export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';
  let ret = '';
  for (const i of set) if (i && i.startsWith(startString)) ret += i.replace(startString, '-');
  return ret.substring(1);
}
