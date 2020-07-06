
$('.scroll-top').on('click', function(event) {
  $(window).scrollTop(0);
});

$(".more-comment-button").on('click', function(event) {
  $(this).toggleClass("showing-comment");

  if ($(this).hasClass("showing-comment")) {
    $(this).text("HIDE COMMENTS");
    $(".toggle_comment").not(".last_comment").show();
  } else {
    $(this).text("MORE COMMENTS");
    $(".toggle_comment").not(".last_comment").hide();
  }
});

$('.feed_text').submit((e) => {
  e.preventDefault();
  console.log('form submitted');
  const $this = $(e.currentTarget);
  const fid = $this.data('fid');
  const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

  $.ajax({
      type: 'POST',
      url: `${fid}/new_comment/`, 
      data: { 
          fid: fid,
          csrfmiddlewaretoken: csrfmiddlewaretoken,
          content: $(`input#${fid}[name=content]`).val(),
      },
      dataType: 'json',
      success: function(response) { 
          console.log(response);
          const str = `
            <div class="feed_comment_each toggle_comment last_comment">
              <p>ㄴ</p>
              <a class="user_name">
                <p>${response.username} :</p>
              </a>
              <div class="comment_main">
                <p>${response.content}</p>
                <a href="/home/${fid}/${response.id}}/delete/" class="comment_delete" data-fid="${fid}" data-cid="${response.id}" data-csrfmiddlewaretoken="${csrfmiddlewaretoken}">delete</a>
              </div>
            </div>
          `;
          const toggle_str = `
              <div class="more-comment-btn">
                <button class="more-comment-button">MORE COMMENT</button>
              </div> 
          `

          const $commentBtn = $('.more-comment-button');
          const $lastComment = $('.last_comment');


          if($commentBtn.length===1 && $lastComment.length===1){
            if ($commentBtn.hasClass('showing-comment')) {
                $lastComment.removeClass('last_comment');
            } else {
                $lastComment.removeClass('last_comment').hide();
            }
          }
          else{
            console.log(1)
            if($('.feed_comment_each').length > 0){
              console.log(2)
              $(toggle_str).insertBefore($('.feed_comment'));
            }
          }

          if($lastComment.length===0){
            $('.feed_comment').append(str)
          }
          else{
            $(str).insertAfter($lastComment);
          }
          $(`input#${fid}[name=content]`).val('');
      },
      error: function(response, status, error) {
          console.log(response, status, error);
      },
      complete: function(response) {
          console.log(response);
      },
  });
});

$('.feed_heart_ajax').click((e) => {
  e.preventDefault();
  console.log('form submitted');
  const $this = $(e.currentTarget);
  const fid = $this.data('fid');
  const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

  $.ajax({
      type: 'POST',
      url: `/home/${fid}/like_feed/`, 
      data: { 
          fid: fid,
          csrfmiddlewaretoken: csrfmiddlewaretoken,
          content: $(`input#${fid}[name=content]`).val(),
      },
      dataType: 'json',
      success: function(response) { 
          console.log(response);
          $('.feed_heart_count').text(response.like_count)
      },
      error: function(response, status, error) {
          console.log(response, status, error);
      },
      complete: function(response) {
          console.log(response);
      },
  });
});

$('.comment_delete').click((e) => {
  e.preventDefault();
  console.log('form submitted');
  const $this = $(e.currentTarget);
  const fid = $this.data('fid');
  const cid = $this.data('cid');
  const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

  $.ajax({
      type: 'POST',
      url: `/home/${fid}/${cid}/delete/`, 
      data: { 
          fid: fid,
          cid: cid,
          csrfmiddlewaretoken: csrfmiddlewaretoken,
          content: $(`input#${fid}[name=content]`).val(),
      },
      dataType: 'json',
      success: function(response) { 
          console.log(response);
          if($this.parent().parent().hasClass('last_comment')){
            $this.parent().parent().prev().addClass('last_comment')
          }
          $this.parent().parent().remove()
      },
      error: function(response, status, error) {
          console.log(response, status, error);
      },
      complete: function(response) {
          console.log(response);
      },
  });
});