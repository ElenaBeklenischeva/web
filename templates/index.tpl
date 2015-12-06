%setdefault('all', '0')
%setdefault('today', '0')
%setdefault('last_visit', '')
%setdefault('browser', 'отсутствует')
<!DOCTYPE html>
<html>
<head>
	%include templates/styles title='Первая страница'
	<link rel="stylesheet" type="text/css" href="styles/index_style.css">
	<script>
        window.onload = function add_resolution(){
            var text = 'Разрешение экрана: <br>' + screen.width + '×' + screen.height;
            var resol = document.getElementById("resolution");
            resol.innerHTML = text;
        };
    </script>
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
	<div class="counter" id='counts'>
        <p class="text_counter">Всего посещений: {{all}}</p>
        <p class="text_counter">Сегодня: {{today}}</p>
        <p class="text_counter">Ваше последнее посещение: <br>{{last_visit}}</p>
        <p class="text_counter" id="resolution"></p>
        <p class="text_counter">Информация о браузере: {{browser}}</p>

    </div>
	%include templates/bottom
</body>
</html>
