%setdefault('all', '0')
%setdefault('today', '0')
%setdefault('last_visit', '')
%setdefault('messages', '')

<!DOCTYPE html>
<html>
<head>
	%include templates/styles title="Контакты"
	<link rel="stylesheet" type="text/css" href="styles/contacts_style.css">

</head>
<body>
	%include templates/head
	<div class='col-xs-offset-1 col-xs-10 col-md-offset-2 col-md-8 col-lg-offset-3 col-lg-6 background'>
		<div class="left_img">
			<img class="image" src="images/photo.jpg" alt="Кот">
		</div>
		<p id="header">Контакты:</p>
		<ul id="padding" class='text'>
			<li>
				<a href="mailto:beklenischeva.elena@gmail.com">
					Email
				</a>
			</li>
			<li><a href="https://vk.com/id93083691">Вконтакте</a></li>
			<li><a href="http://urfu.ru/ru/">УрФУ</a></li>
			<li><a href="http://imkn.urfu.ru/">Матмех</a></li>
		</ul>
	</div>
	%include templates/counter all=all, today=today, last_visit=last_visit, browser=browser
	%include templates/comment_tpl messages=messages
	%include templates/bottom
</body>
</html>