## 키워드

> 키워드는 정해진 특별한 의미가 부여된 단어

|  |  |  |  |  |
| -- | -- | -- | -- | -- | 
| break | else | instanceof | true | case
| false | new | try | catch | finally |
|null | typeof | continue | for | return |
| var | default | function | switch | void |
| delete | if | this | while | do |
| in | throw | with | const | class |

---

## 식별자

* 숫자로 시작하면 안 된다.
* 공백을 사용하면 안 된다.
* 키워드를 사용하면 안 된다.
* 특수 문자는 _과 $만 허용한다.

종류


---

## 이스케이프 문자

```
\t  *수평 탭     
\n  *행 바꿈
\\  *역 슬래시
\'  *작은 따옴표
\"  *큰 따음표
```

---

## 문자열 연결

```javascript
> '가나다라' + '마바사' + '아자차카' + '타파하'
=
> 가나다라마바사하자차카타파하 
```

---

## 논리 연산자
```javascript
! 논리 부정 (참이면 거짓, 거짓이면 참)
예)
!true = false
!(10 == 10) = false

&& 논리곱 (둘 다 참이여야 함)
예)
true && true = true
true && false = false

|| 논리합 (둘 중 하나만 참이어도 참)
예)
true || false = true
false || false = false
```

---

## 변수

```
var

* 변수 중복 선언 가능하여, 예기치 못한 값을 반환할 수 있다.
* 변수 선언문 이전에 변수를 참조하면 언제나 undefined를 반환한다.
```

```
const

* 변수 재할당이 불가능하다.
```

```
let

* 변수 재할당이 가능하다.
```

---




