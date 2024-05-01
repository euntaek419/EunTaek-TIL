function solution(number, limit, power) {
    count = [];
    result = 0;
    
    for (i = 0; i < number + 1; i++) { // 0부터 number까지
        count.push(0); // 0으로 초기화된 요소를 배열에 추가
    }

    for (i = 1; i <= number; i++) { // 숫자 1부터 number까지 약수 구하기
        for (j = i; j <= number; j += i) { // i부터 number까지 i씩 증가
            count[j] += 1;
        }
    }

    for (i of count) { // limit 보다 크면 power 더하기, 아니면 i 그대로 더하기
        if (i > limit) {
            result += power;
        } else {
            result += i;
        }
    }

    return result;
}