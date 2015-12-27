%setdefault('messages', '')
%setdefault('addr', '#')

<button value='0' onclick='upper()' id='comment_b'>O</button>
<div class="comments_button" id='comment_button'>
    <div id='feedback'>
        <h3 id="reply-title" class="reply">Оставить отзыв</h3>
        <!--<form action="{{addr}}" id="comment_form" class="reply-form" enctype="multipart/form-data">-->
        <div id="comment_form" class="reply-form">
            <p>
                <label for="comment">Отзыв</label></p>
            <p>
                <textarea id="comment" name="answer_form" rows="4"></textarea>
            </p>
            <p class="submit_comment">
                <button name="submit" id='submit' class="submit" onclick='vote()'>Отправить</button>
            </p>
        </div>
    </div>
    %include templates/comments messages=messages

</div>
