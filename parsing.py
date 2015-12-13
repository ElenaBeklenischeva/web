from html.parser import HTMLParser

open_tags = ['b', 'i', 'img']
attributes = ['src']
close_tags = ['b', 'i']
curr_tags = []


def screening(text):
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag in open_tags and attrs in attributes:
            curr_tags.append(tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


def clear_space(data):
    data = data.replace("  ", " ")
    data = data.replace(" >", ">")
    return data


def parsing_text(data):
    s_b = '<b>'
    e_b = '</b>;'
    s_i = '<i>'
    e_i = '</i>'
    img_s1 = '<img src="'
    img_e1 = '">;'
    img_s2 = "<img src='"
    img_e2 = "'>"
    start = [s_b, s_i]
    length = len(data)
    stack = []
    tags = []
    i = 0
    j = []
    # data = screening(data)
    data = clear_space(data)
    while i < length:
        i = data.index("<")
        if i >= 0:
            if data[i:i + 3] in start:
                stack.append((data[i:i + 3], i))
                i += 3
            elif i + 10 <= length and (data[i:i + 10] == img_s1 or
                                               data[i:i + 10] == img_s2):

                close_index_1 = data[i + 1:].index('">')
                close_index_2 = data[i + 1:].index("'>")
                open_index = data[i + 1:].index("<")
                bracket1 = data[i + 11:].index('"')
                bracket2 = data[i + 11:].index("'")
                if data[i:i + 10] == img_s1 and (
                                close_index_1 < open_index or open_index < 0) and close_index_1 == bracket1:
                    # {{!data[i:close_index_1 + 3]}}
                    i = close_index_1 + 3
                elif data[i:i + 10] == img_s2 and (
                                close_index_2 < open_index or open_index < 0) and close_index_2 == bracket2:
                    # {{!data[i:close_index_1 + 3]}}
                    i = close_index_2 + 3
                else:
                    i += 1
            elif i + 4 <= length and len(stack) > 0 and i - stack[-1][1] + 4 > 0:
                if stack[-1][0] == s_b:
                    if data[i:i + 4] != e_b:
                        data = data[:stack[-1][1]] + screening(data[stack[-1][1]: stack[-1][1] + 3]) + data[
                                                                                                       stack[-1][
                                                                                                           1] + 3:]
                    else:
                        pass
                        # {{!data[stack[-1][1]:i+4}}
                    stack.pop()
                elif stack[-1][0] == s_i:
                    if data[i:i + 4] != e_i:
                        data = data[:stack[-1][1]] + screening(data[stack[-1][1]: stack[-1][1] + 3]) + data[
                                                                                                       stack[-1][
                                                                                                           1] + 3:]
                    else:
                        pass
                        # {{!data[stack[-1][1]:i+4}}
                    stack.pop()
                i += 1
            else:
                data = screening(data[i:i+1])
                i += 1
        else:
            # {{data[i:]}}
            break

# parser = MyHTMLParser()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')


def get_index(data, substr):
    close_index_2 = data.count(substr)
    if close_index_2 > 0:
        return data.index(substr)
    else:
        return -1