function solution(n, lost, reserve) {
    result = [];
    count = 0;

    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);

    new_lost = lost.filter(l => !reserve.includes(l));
    new_reserve = reserve.filter(r => !lost.includes(r));

    // 모두 가지고 있다고 가정
    for (i = 0; i < n; i++) {
        result.push(1);
    }

    // 잃어버린 사람 추려내기
    new_lost.forEach(l => {
        result[l - 1] -= 1;
    });

    new_reserve.forEach(r => {
        result[r - 1] += 1;
    });

    // 빌려줄 수 있으면 앞쪽 사람부터 빌려주기
    new_reserve.forEach(r => {
        if (r > 1 && result[r - 2] === 0) { // 2번째보다 크면 앞으로 빌려주기 가능
            result[r - 2] += 1;
            return; // 앞 학생에게 빌려주었으면 건너뛰기
        }

        if (r < n && result[r] === 0) { // 또는 뒷 번호에 빌려주기
            result[r] += 1;
        }
    });

    // 세기
    result.forEach(r => {
        if (r >= 1) {
            count += 1;
        }
    });

    return count;
}
