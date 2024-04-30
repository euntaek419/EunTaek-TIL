function solution(k, m, score) {
  box = Math.floor(score.length / m);

  score.sort(function(a, b) { return b - a; });

  result = 0;
  temp = [];

  for (i = 0; i < box; i++) { 
    temp = score.slice(i * m, (i + 1) * m);
    result += Math.min.apply(null, temp) * m;
    temp = [];
  }

  return result;
}