%setdefault('all', '0')
%setdefault('today', '0')
%setdefault('last_visit', '')
%setdefault('messages', '')
%setdefault('browser', 'отсутствует')
<!DOCTYPE html>
<html>
<head>
	%include templates/styles title='Первая страница'
	<link rel="stylesheet" type="text/css" href="styles/index_style.css">
</head>
<body>
    % include templates/head
	<div class='col-xs-offset-1 col-xs-10 col-md-offset-2 col-md-8 col-lg-offset-3 col-lg-6 background'>
		<div class="left_img">
			<img class="image" src="images/photo.jpg" alt="Photo">
		</div>
		<ul class="text list">
			<li class="top">Доброго времени суток!</li>
			<li>Меня зовут Бекленищева Елена</li>
			<li>И это мой первый сайт</li>
		</ul>
	</div>
	%include templates/counter text=text, browser=browser
	%include templates/comment_tpl messages=messages, addr="/"
 	%include templates/bottom
</body>
</html>
