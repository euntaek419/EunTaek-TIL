function solution(s) {
  s = s.toLowerCase();
  s = s.split('');
  s[0] = s[0].toUpperCase();
  for (i = 0; i < s.length; i++) {
    if (s[i] === ' ') {
      if (i < s.length - 1) {
        s[i + 1] = s[i + 1].toUpperCase();
      }
    }
  }
  return s.join('');
}