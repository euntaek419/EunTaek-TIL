function solution(lottos, win_nums) {
  result = [];
  lottos.sort((a, b) => a - b);
  win_nums.sort((a, b) => a - b);
  
  count = 0;
  zero = 0;
  
  for (i = 0; i < lottos.length; i++) {
    if (lottos[i] === 0) {
      zero += 1;
    }
    for (j = 0; j < win_nums.length; j++) {
      if (lottos[i] === win_nums[j]) {
        count += 1;
      }
    }
  }
  
  // 1등부터 5등까지 구하기
  if (count + zero === 6) {
    result.push(1);
  } else if (count + zero === 5) {
    result.push(2);
  } else if (count + zero === 4) {
    result.push(3);
  } else if (count + zero === 3) {
    result.push(4);
  } else if (count + zero === 2) {
    result.push(5);
  } else {
    result.push(6);
  }
  
  // 꼴등 구하기
  if (count === 6) {
    result.push(1);
  } else if (count === 5) {
    result.push(2);
  } else if (count === 4) {
    result.push(3);
  } else if (count === 3) {
    result.push(4);
  } else if (count === 2) {
    result.push(5);
  } else {
    result.push(6);
  }
  
  return result;
}