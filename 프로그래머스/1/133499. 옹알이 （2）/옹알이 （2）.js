function solution(babbling) {
    count = 0;

    for (i = 0; i < babbling.length; i++) {
        babbling[i] = babbling[i].replace(/aya/g, '*');
        babbling[i] = babbling[i].replace(/\*\*/g, 'aya');
        
        babbling[i] = babbling[i].replace(/ye/g, '&');
        babbling[i] = babbling[i].replace(/&&/g, 'ye');
        
        babbling[i] = babbling[i].replace(/woo/g, '^');
        babbling[i] = babbling[i].replace(/\^\^/g, 'woo');
        
        babbling[i] = babbling[i].replace(/ma/g, '%');
        babbling[i] = babbling[i].replace(/%%/g, 'ma');
    }

    for (j = 0; j < babbling.length; j++) {
        babbling[j] = babbling[j].replace(/\*/g, '');
        babbling[j] = babbling[j].replace(/&/g, '');
        babbling[j] = babbling[j].replace(/\^/g, '');
        babbling[j] = babbling[j].replace(/%/g, '');
        
        if (babbling[j] === '') {
            count++;
        }
    }

    return count;
}