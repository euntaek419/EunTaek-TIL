function solution(arr, queries) {
    result = [];
    
    for (i = 0; i < queries.length; i++) {
        query = queries[i];
        s = query[0];
        e = query[1];
        k = query[2];
        sub = arr.slice(s, e + 1);
        
        filter = [];
        for (let j = 0; j < sub.length; j++) {
            if (sub[j] > k) {
                filter.push(sub[j]);
            }
        }
        
        if (filter.length > 0) {
            min = filter[0];
            for (j = 1; j < filter.length; j++) {
                if (filter[j] < min) {
                    min = filter[j];
                }
            }
        result.push(min);
        } else {
            result.push(-1);
        }
    }
    return result;
}