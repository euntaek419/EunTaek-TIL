function solution(name, yearning, photo) {
  score = {};
  result = [];

  for (i = 0; i < name.length; i++) {
    score[name[i]] = yearning[i];
  }

  for (i = 0; i < photo.length; i++) {
    tempScore = 0;
    for (j = 0; j < photo[i].length; j++) {
      if (photo[i][j] in score) {
        tempScore = tempScore + score[photo[i][j]];
      }
    }
    result.push(tempScore);
  }

  return result;
}