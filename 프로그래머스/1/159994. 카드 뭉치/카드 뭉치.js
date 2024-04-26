function solution(cards1, cards2, goal) {
    one = 0;
    two = 0;
    result = [];

    for (i = 0; i < goal.length; i++) {
        if (one < cards1.length && goal[i] === cards1[one]) {
            result.push(goal[i]);
            one++;
        } else if (two < cards2.length && goal[i] === cards2[two]) {
            result.push(goal[i]);
            two++;
        } else {
            return "No";
        }
    }

    if (result.join('') == goal.join('')) {
        return "Yes";
    } else {
        return "No";
    }
}