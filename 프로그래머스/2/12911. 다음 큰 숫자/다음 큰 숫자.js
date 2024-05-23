function solution(n) {
    bn1 = n.toString(2); // n을 이진수 문자열로 변환
    count = 0;
    for (i = 0; i < bn1.length; i++) { // n의 1의 개수 세기
        if (bn1[i] == '1') {
            count++;
        }
    }

    for (i = n + 1; i < 1000000; i++) {
        count2 = 0;
        bn2 = i.toString(2); // i를 이진수 문자열로 변환
        for (j = 0; j < bn2.length; j++) {
            if (bn2[j] == '1') {
                count2++;
            }
        }

        if (count == count2) {
            return parseInt(bn2, 2); // 이진수 문자열을 정수로 변환하여 반환
        }
    }
}
