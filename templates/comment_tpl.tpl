%setdefault('messages', '')
%setdefault('addr', '#')
<div class="comments_button" id='comment_button'>
    %include templates/comments messages=messages, addr=addr
</div>