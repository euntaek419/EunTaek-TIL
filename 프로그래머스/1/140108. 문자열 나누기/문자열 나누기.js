function solution(s) {
  word = ''
  count = 0
  result = 0

  for (i = 0; i < s.length; i++) {
    if (count == 0) {
      word = s[i];
      result += 1;
    }

    if (s[i] == word) {
      count += 1;
    } else if (s[i] !== word) {
      count -= 1;
    }
  }

  return result;
}