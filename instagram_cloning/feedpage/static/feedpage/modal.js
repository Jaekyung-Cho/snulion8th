$('#feed-create').submit((e)=>{
  e.preventDefault()

  $.ajax({
    url: '/home/',  // feed create을 POST 받는 url과, view함수는 "/feeds/"였습니다. 
    method: 'POST',
    data: {  // 요청(request)로 함께 보낼 데이터 정의
      title: $(`input#title`).val(),
      photo: $(`input#photo`).val(),
      content: $(`textarea#content`).val(),
      csrfmiddlewaretoken: $(e.currentTarget).data('csrfmiddlewaretoken')   // 장고 security와 관련해서 아무나 feed를 생성하지 못하도록 form 액션을 할 때는, csrf_token이 필요
    },
    dataType: "json",  // json => "javascript object notation"
    success(response) {
      console.log(response)
      console.log(1)
      window.location.href = '/home/'   //** redirect
    },
    error(response, status, error) {
      console.log(response, status, error);
    }
  })
})