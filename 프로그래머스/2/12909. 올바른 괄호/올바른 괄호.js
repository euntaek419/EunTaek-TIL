function solution(s) {
  result = [];
  for (i = 0; i < s.length; i++) {
    if (s[i] == "(") {
      result.push(s[i]);
    } else {
      if (result.length == 0) {
        return false;
      } else {
        result.pop();
      }
    }
  }
  return result.length == 0;
}