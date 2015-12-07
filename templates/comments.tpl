%setdefault('all', '0')
%setdefault('today', '0')
%setdefault('last_visit', '')
%setdefault('messages', '')
<!DOCTYPE html>
<html>
<head>
	%include templates/styles title="Отзывы"
	<link rel="stylesheet" type="text/css" href="styles/hw_style.css">
</head>
<body>
	%include templates/head
	<div class='col-xs-offset-1 col-xs-10 col-md-offset-2 col-md-8 col-lg-offset-3 col-lg-6 background'>
        <h3 id="reply-title" class="reply">Оставить отзыв</h3>
        <form action="/hw.html" method="post" id="comment_form" class="reply-form" enctype="multipart/form-data">
            <p>
                <label for="comment">Отзыв</label></p>
            <p>
                <textarea id="comment" name="answer_form" rows="4"></textarea>
            </p>
            <p class="submit_comment">
                <button name="submit" class="submit" onclick=clear_form()>Отправить</button>
            </p>
        </form>
        <div>
        %for message in messages:
            <p><b style="font-size:15px;color:black"><i>{{message[0]}}:</i></b>&nbsp;
                %s_b = '<b>'
                %e_b = '</b>'
                %s_i = '<i>'
                %e_i = '</i>'
                %img_s1 = '<img src="'
                %img_e1 = '">'
                %img_s2 = "<img src='"
                %img_e2 = "'>"
                %start = [s_b, s_i]
                %data = message[1]
                %length = len(data)
                %stack = []
                %tags = []
                %i = 0
                %j = []
                %while i < length:
                %    if i + 3 <= length and data[i:i + 3] in start:
                %        stack.append((data[i:i + 3], i))
                %        i += 3
                %    elif i + 9 <= length and (data[i:i + 10] == img_s1 or
                %                                     data[i:i + 10] == img_s2):
                %        stack.append((data[i:i + 10], i))
                %        i += 9
                %    elif i + 4 <= length and len(stack) > 0 and i - stack[-1][1] + 10 > 0:
                %        if stack[-1][0] == s_b and data[i:i + 4] == e_b:
                %            c = data[stack[-1][1] + 3:i].count('<')
                %            substr = data[stack[-1][1] + 3:i].replace('<', '&lt;')
                %            data = data[:stack[-1][1] + 3] + substr + data[i:]
                %            substr = data[stack[-1][1] + 3:i + c*3].replace('>', '&gt;')
                %            data = data[:stack[-1][1] + 3] + substr + data[i + c*3:]
                %            tags.append((stack[-1][1], i + c*6, s_b))
                %            j.append(stack[-1][1])
                %            j.append(stack[-1][1] + 3)
                %            j.append(i)
                %            j.append(i + 4 + c*6)
                %            i += 4 + c*6
                %            stack.pop(-1)
                %        elif stack[-1][0] == s_i and data[i:i + 4] == e_i:
                %            c = data[stack[-1][1] + 3:i].count('<')
                %            substr = data[stack[-1][1] + 3:i].replace('<', '&lt;')
                %            data = data[:stack[-1][1] + 3] + substr + data[i:]
                %            substr = data[stack[-1][1] + 3:i + c*3].replace('>', '&gt;')
                %            data = data[:stack[-1][1] + 3] + substr + data[i + c*3:]
                %            tags.append((stack[-1][1], i + c*6, s_i))
                %            j.append(stack[-1][1])
                %            j.append(stack[-1][1] + 3)
                %            j.append(i)
                %            j.append(i + 4 + c*6)
                %            i += 4 + c*6
                %            stack.pop(-1)
                %        else:
                %            i += 1
                         %end
                %    elif i + 2 <= length and len(stack) > 0:
                %        if stack[-1][0] == img_s1 and data[i:i + 2] == img_e1:
                %            if "'" in data[stack[-1][1] + 10:i] or '"' in data[stack[-1][1] + 10:i]:
                %                i += 2
                %            else:
                %                tags.append((stack[-1][1], i, img_s1))
                %                j.append(stack[-1][1])
                %                j.append(i + 4)
                %                i += 2
                %            end
                %            stack.pop(-1)
                %        elif stack[-1][0] == img_s2 and data[i:i + 2] == img_e2:
                %            if "'" in data[stack[-1][1] + 10:i] or '"' in data[stack[-1][1] + 10:i]:
                %                i += 2
                %            else:
                %                tags.append((stack[-1][1], i, img_s1))
                %                j.append(stack[-1][1])
                %                j.append(i + 4)
                %                i += 2
                %            end
                %            stack.pop(-1)
                %        else:
                %            i += 1
                         %end
                %    else:
                %        i += 1
                    %end
                %end
                %l = 0
                %if len(stack) == 0:
                %    i = 0
                %    while i < length:
                %       if i in j:
                %           string = data[l:i]
                %           k = j.index(i)
                %           if data[i:i+4] == '<img':
                %               tag = data[i:j[k + 1]]
                %               i = j[k + 1] + 1
                %               l = i
                %           else:
                %               tag = data[i:j[k + 3]]
                %               i = j[k + 3] + 1
                %               l = i
                            %end
                            {{string}}
                            {{!tag}}
                        %end
                        % i += 1
                     %end
                %end
                {{data[l:]}}
            </p>
        %end
        </div>
	</div>
	%include templates/bottom
</body>
</html>