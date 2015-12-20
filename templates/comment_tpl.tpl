%setdefault('messages', '')
%setdefault('addr', '#')
<button value='0' onclick='upper()' id='comment_b'>O</button>
<div class="comments_button" id='comment_button'>
    %include templates/comments messages=messages, addr=addr
</div>
