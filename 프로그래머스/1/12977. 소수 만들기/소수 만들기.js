function solution(nums) {
    count = new Array(3000).fill(true);
    count[0] = count[1] = false;

    for (i = 2; i < 3000; i++) {
        if (count[i]) {
            for (j = i * i; j < 3000; j += i) {
                count[j] = false;
            }
        }
    }

    countPrime = 0;

    for (i = 0; i < nums.length - 2; i++) {
        for (j = i + 1; j < nums.length - 1; j++) {
            for (k = j + 1; k < nums.length; k++) {
                sum = nums[i] + nums[j] + nums[k];
                if (count[sum]) {
                    countPrime++;
                }
            }
        }
    }

    return countPrime;
}