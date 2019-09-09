# Django

## Model 정의

* title : charfield
* content : textfield
* created_at : auto_now_add, datetimefield
* updated_at : auto_now, datetimefield

## CRUD

* C
  * `/new/` : 글 작성 form
  * `/create/` : 저장 후 index로 보내기(redirect)
* R
  * `/1/` : `detail` 함수에서 처리
* D
  * `/1/delete/` : 삭제 후 index로 보내기
* U
  * `/1/edit/` : 글 수정 form
  * `/1/update/` : 저장 후 Read로 보내기