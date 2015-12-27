%import parsing
%setdefault('messages', '')
%setdefault('addr', '#')


<div id='feedback'>
    <h3 id="reply-title" class="reply">Оставить отзыв</h3>
    <!--<form action="{{addr}}" method="post" id="comment_form" class="reply-form" enctype="multipart/form-data">-->
    <form action="{{addr}}" id="comment_form" class="reply-form" enctype="multipart/form-data">
        <p>
            <label for="comment">Отзыв</label></p>
        <p>
            <textarea id="comment" name="answer_form" rows="4"></textarea>
        </p>
        <p class="submit_comment">
            <button name="submit" id='submit' class="submit" onclick='vote()'>Отправить</button>
        </p>
    </form>
</div>
<div id="comment_form">
    %for message in messages:
        <p class="answer"><b style="font-size:15px;color:black"><i>{{message[0]}}:</i></b>&nbsp;
            %data = message[1]
            %s_b = '<b>'
            %e_b = '</b>'
            %s_i = '<i>'
            %e_i = '</i>'
            %img_s1 = '<img src="'
            %img_e1 = '">'
            %img_s2 = "<img src='"
            %img_e2 = "'>"
            %start = [s_b, s_i]
            %end = [e_b, e_i]
            %length = len(data)
            %stack = []
            %tags = []
            %i = 0
            %j = []
            %data = parsing.clear_space(data)
            %while i < length:
            %   try:
            %        i += data[i:].index("<")
            %        if data[i:i + 3] in start:
            %            stack.append((data[i:i + 3], i))
            %            i += 3
            %        elif i + 10 <= length and (data[i:i + 10] == img_s1 or
            %                                           data[i:i + 10] == img_s2):
                        %close_index_1 = parsing.get_index(data[i + 11:], '">')
                        %close_index_2 = parsing.get_index(data[i + 11:], "'>")
                        %open_index = parsing.get_index(data[i + 11:], "<")
                        %bracket1 = parsing.get_index(data[i + 11:], '"')
                        %bracket2 = parsing.get_index(data[i + 11:], "'")
                        %if data[i:i + 10] == img_s1 and (
                        %                close_index_1 < open_index or open_index < 0) and close_index_1 == bracket1:
                            {{!data[i:close_index_1 + 13]}}
                        %    i = close_index_1 + 13
                        %elif data[i:i + 10] == img_s2 and (
                        %                close_index_2 < open_index or open_index < 0) and close_index_2 == bracket2:
                            {{!data[i:close_index_2 + 13]}}
                        %    i = close_index_2 + 13
                        %else:
                        %   close_index_1 = parsing.get_index(data[i + 11:], ">")
                        %   if close_index_1 > -1:
                        %       if bracket1 > -1:
                                    {{!data[i:bracket1 + 12] + '>'}}
                        %       elif bracket2 > -1:
                                    {{!data[i:bracket2+12] + '>'}}
                        %       end
                        %       i += close_index_1 + 12
                        %    else:
                        %        i += 1
                        %        #  break
                        %    end
                        %end
                    %elif i + 4 <= length and len(stack) > 0 and i - stack[-1][1] + 4 > 0 and data[i:i + 4] in end:
                        %if stack[-1][0] == s_b:
                        %    if data[i:i + 4] != e_b:
                        %       if data[i:i + 4] != e_i:
                        %           counter = data[stack[-1][1]: stack[-1][1] + 3].count("<")
                        %           counter += data[stack[-1][1]: stack[-1][1] + 3].count(">")
                        %           data = data[:stack[-1][1]] + parsing.screening(data[stack[-1][1]: stack[-1][1] + 3]) + data[stack[-1][1] + 3:]
                        %           i += counter * 4
                                    %if len(stack) < 2:
                                        {{data[stack[-1][1]:i+4]}}
                                    %end
                        %       else:
                                    %if len(stack) < 2:
                                        {{data[stack[-1][1]:i+4]}}
                                    %end
                        %           i += 4
                        %       end
                        %    else:
                                %i += 4
                                %if len(stack) < 2:
                                    {{!data[stack[-1][1]:i+4]}}
                                %end
                            %end
                        %    stack.pop()
                        %elif stack[-1][0] == s_i:
                        %    if data[i:i + 4] != e_i:
                        %       if data[i:i + 4] != e_b:
                        %           counter = data[stack[-1][1]: stack[-1][1] + 3].count("<")
                        %           counter += data[stack[-1][1]: stack[-1][1] + 3].count(">")
                        %           data = data[:stack[-1][1]] + parsing.screening(data[stack[-1][1]: stack[-1][1] + 3]) + data[stack[-1][1] + 3:]
                        %           i += counter *4
                                    %if len(stack) < 2:
                                        {{data[stack[-1][1]:i+4]}}
                                    %end
                        %       else:
                                    %if len(stack) < 2:
                                        {{data[stack[-1][1]:i+4]}}
                                    %end
                        %           i += 4
                        %       end
                        %    else:
                        %       i += 4
                                %if len(stack) < 2:
                                    {{!data[stack[-1][1]:i+4]}}
                                %end
                            %end
                        %    stack.pop()
                        %end
                    %else:
                    %    index = parsing.get_index(data[i:], ">")
                    %    if index == -1:
                    %       data = parsing.screening(data[i:])
                            {{data[i:]}}
                    %       break
                    %    else:
                    %       counter = data[i:index + i].count("<")
                    %       counter += data[i:index + i].count(">")
                    %       data = data[:i] + parsing.screening(data[i:index + i + 1]) + data[index + i + 1:]
                    %       i += index + 3 +counter*4
                    %    end
                    %end
            %   except ValueError:
                    {{data[i:]}}
            %       break
            %   finally:
                   % length = len(data)
            %   end
                %end
        </p>
    %end
</div>