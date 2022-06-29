## 선택자

* 전체 선택자 *
* 태그 선택자 div, span, h1~h6 ...
* 아이디 선택자 #id
* 클래스 선택자 .class

---

## 반응 선택자

* :active - 클릭하는동안 변경
* :hover - 마우스를 올릴 때 변경

---

## 구조 선택자

* :first-child - 형제 관계에서 첫 번째로 등장하는 태그 선택
* :last-child - 형제 관계에서 마지막으로 등장하는 태그 선택

* :nth-child(1) - 형제 관계에서 앞에서 1 번째로 등장하는 태그 선택
* :nth-child(5) - 형제 관계에서 앞에서 5 번째로 등장하는 태그 선택

* :nth-last-child(1) - 형제 관계에서 뒤에서 1 번째로 등장하는 태그 선택
* :nth-last-child(5) - 형제 관계에서 뒤에서 5 번째로 등장하는 태그 선택

---

## 단위

* % = 백분율
* 1em = 1배수
* 1.5em = 1.5배수
* px = 픽셀

---

## 박스 속성

![박스 속성 이미지](https://t1.daumcdn.net/cfile/tistory/2322D34B54742D8D22)

* margin 속성 - 테투리와 다른 태그 사이의 테투리 바깥쪽 여백
* border 속성 - 테두리
* padding 속성 - 테두리와 글자 사이의 테두리 안쪽 여백, 배경색은 padding 영역까지만 적용
* width 속성 - 글자를 감싸는 영역의 가로 크기
* height 속성 - 글자를 감싸는 영역의 세로 크기


---

## 배경 속성

* background-repeat - 배경 이미지의 반복 형태 지정
* background-attachment - 배경 이미지의 부착 형태 지정(ex. scroll 값일 경우, 스크롤 이동시에도 배경 고정)
* background-position - 배경 이미지의 위치 지정

---

## 위치 속성

* z-index - 앞, 뒤 위치 조절 기능
* position:relative - 상대적으로 위치를 배치할 수 있다.

---

## 그림자 & 그레이디언트

* text-shadow
* box-shadow

* [그레이디언트 생성기](https://www.colorzilla.com/gradient-editor/)

---

## 중앙 정렬

```css
width : 960px;
margin : 0 auto;
```
---

## 반응형 웹

```html
<meta name="viewport" content="user-scalable=no,initial-scale=1, maximum-scale=1">
```

viewport meta 태그에 입력할 수 있는 값

```
* width             /* width = 240 화면 너비 */
* height            /* height = 800 화면 높이 */ 
* initial-scale     /* initial-scale = 2.0 초기 확대 비율 */
* user-scalable     /* user-scalable = no 확대 및 축소 가능 여부 */
* minimum-scale     /* minimum-scale = 1.0 최소 축소 비율 */
* maximum-scale     /* maximum-scale = 2.0 최대 확대 비율 */
* target-densitydpi /* target-densitydpi = medium-dpi DPI 지정 */
```

## 미디어 쿼리

@media

