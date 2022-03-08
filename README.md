# DRF-commerce

<br />

## :: 구현 목표 
- 커머스 서비스 상품 CRUD API 구현
- 상품 & 태그 어드민 페이지 구현

<br />



## :: Project Structure

```bash
.
├── README.md
├── commerce
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── settings.cpython-38.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── products
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── pagination.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── requirements.txt
```



## :: 구현 사항 설명 
1. 상품 생성 시 하기 조건 검증
      - 정가와 상품 가격은 양수여야 함
      - 상품의 가격은 정가보다 클 수 없음

2. GET 메서드 실행시 할인률 포함 & 10개 단위로 페이지네이션

3. 상품 & 태그 어드민 페이지
      - 어드민 페이지에서 각각의 필드를 조회하고 추가, 수정, 삭제 할 수 있습니다.

4. 모델 수정
    - Tag를 별도의 테이블로 분리해 ManyToMany 관계로 설정


<br />

## :: 성장 포인트 

- SlugRelatedField에 대해 알게 되었습니다.
- django admin 페이지를 사용해 볼 수 있었습니다.

## :: 기타 사용 라이브러리
django-admin-relation-links==0.2.5 <br />
django-mysql==4.5.0 <br />
drf-yasg==1.20.0 <br />
swagger-spec-validator==2.7.4 <br />

<br />

<br />

## :: 개선 필요 사항
1. 어드민 페이지 개선 및 커스텀 (템플릿 오버라이드) 필요
2. 테스트 코드를 작성 필요
3. 어드민 리스트 페이지에서 태그의 이름이 보이지 않는 문제 수정 필요
4. 태그 섹션 클릭시 태그 수정 페이지로 넘어가는 기능 구현 필요
