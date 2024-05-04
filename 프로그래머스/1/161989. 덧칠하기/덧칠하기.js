function solution(n, m, section) {
  array = new Array(n+1).fill(true);
  count = 0;

  for (i of section) {
    array[i] = false;
  }

  for (i = 0; i < array.length; i++) {
    if (array[i] === false) {
      count++;
      array[i] = true;
      for (j = 0; j < m; j++) {
        if (i + j <= n) {
          array[i+j] = true;
        }
      }
    }
  }

  return count;
}