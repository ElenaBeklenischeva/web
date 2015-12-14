%setdefault('all', '0')
%setdefault('today', '0')
%setdefault('last_visit', '')
%setdefault('browser', 'отсутствует')
<!DOCTYPE html>
<html>
<head>
	%include templates/styles title='Практика'
	<link rel="stylesheet" type="text/css" href="styles/hw_style.css">
	<script src="js/hw.js"></script>
</head>
<body>
	% include templates/head
	<div class='col-xs-offset-1 col-xs-10 col-md-offset-2 col-md-8 col-lg-offset-3 col-lg-6 background'>
		<p>Домашняя работа №1:</p>
		<ul class='col-sm-offset-1'>
			<li class="paddingList">
				<a href="hw/1/hw1.html"> Карта</a>
			</li>
		</ul>
		<p>Домашняя работа №2:</p>
		<ul class='col-sm-offset-1'>
			<li class="paddingList">
				<a href="hw/2/e1.html"> Шапка e1.ru </a>
			</li>
			<li class="paddingList">
				<a href="hw/2/levelUp/hw2.html"> Таблица </a>
			</li>
		</ul>
		<p>Домашняя работа №3:</p>
		<ul class='col-sm-offset-1'>
			<li class="paddingList">
				<a href="hw/3/class3.html"> Паспарту </a>
			</li>
			<li class="paddingList">
				<a href="hw/3/levelUp/watches.html"> Часы SVG</a>
			</li>
		</ul>
		<p>Домашняя работа №4:</p>
		<ul class='col-sm-offset-1'>
			<li class="paddingList">
				<a href="hw/4/sqr.html"> Квадраты </a>
			</li>
			<li class="paddingList">
				<a href="hw/4/levelUp/clock.html"> Часы CANVAS</a>
			</li>
		</ul>
		<p>Домашняя работа №5:</p>
		<ul class='col-sm-offset-1'>
			<li class="paddingList">
				<a href="hw/5/for_one.html"> Квадраты </a>
			</li>
		</ul>
	</div>
	%include templates/counter all=all, today=today, last_visit=last_visit, browser=browser
	%include templates/bottom
	%include templates/comment_tpl messages=messages
</body>
</html>