def solution(chicken):
    #치킨 1081마리 주문
    
    coupon1 = chicken       #1081개 사용
    
    print("1번째 남은 쿠폰 =", coupon1)
    
    coupon2 = coupon1 // 10 #108개 사용
    rest2 = coupon1 % 10 + coupon2
    
    print("2번째 남은 쿠폰 =", rest2)
    
    coupon3 = rest2 // 10   
    rest3 = rest2 % 10 + coupon3
    
    print("3번째 남은 쿠폰 =", rest3)
    
    coupon4 = rest3 // 10   
    rest4 = rest3 % 10 + coupon4
    
    print("4번째 남은 쿠폰 =", rest4)
    
    coupon5 = rest4 // 10   
    rest5 = rest4 % 10 + coupon5
    
    print("5번째 남은 쿠폰 =", rest5)
    
    coupon6 = rest5 // 10   
    rest6 = rest5 % 10 + coupon6
    
    print("6번째 남은 쿠폰 =", rest6)
    
    coupon7 = rest6 // 10   
    rest7 = rest6 % 10 + coupon7
    
    print("7번째 남은 쿠폰 =", rest7)
    
    
    
    
    
    
    return coupon2 + coupon3 + coupon4 + coupon5 + coupon6 + coupon7