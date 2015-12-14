%setdefault('all', '0')
%setdefault('today', '0')
%setdefault('last_visit', '')
%setdefault('messages', '')
<!DOCTYPE html>
<html>
<head>
	%include templates/styles title='Галерея'
	<link rel="stylesheet" type="text/css" href="styles/galery_style.css">
	<script  type="text/javascript" href="js/ie.js"></script>
	<script type="text/javascript" src='js/gallery.js'></script>
	<script  type="text/javascript" src="js/gallery_buttons.js"></script>
	<script>
        window.onload = function add_resolution(){
            var text = 'Разрешение экрана: <br>' + screen.width + '×' + screen.height;
            var resol = document.getElementById("resolution");
            resol.innerHTML = text;
        };
    </script>
</head>
<body onhelp="return false" name="body">
	%include templates/head
	<div class='col-xs-offset-1 col-xs-10 col-md-offset-2 col-md-8 col-lg-offset-3 col-lg-6 background'>
		<div id='previewsContainer'>
			<div class="load">
			<a href="#1.jpg" class='aImg' onclick="return false">
				<img class='images' data-larger="images/1.jpg" id='1' src="images/1s.jpg" alt='photo'>
			</a>
			</div>
			<div class="load">
			<a href='#2.jpg' class='aImg' onclick="return false">
				<img class='images' data-larger="images/2.jpg" id='2' src="images/2s.jpg" alt='photo'>
			</a>
			</div>
			<div class="load">
			<a href='#3.jpg' class='aImg' onclick="return false">
				<img class='images' data-larger="images/3.jpg" id='3' src="images/3s.jpg" alt='photo'>
			</a>
			</div>
			<div class="load">
			<a href='#4.jpg' class='aImg' onclick="return false">
				<img class='images' data-larger="images/4.jpg" id='4' src="images/4s.jpg" alt='photo'>
			</a>
			</div>
			<div class="load">
			<a href='#5.jpg' class='aImg' onclick="return false">
				<img class='images' data-larger="images/5.jpg" id='5' src="images/5s.jpg" alt='photo'>
			</a>
			</div>
			<div class="load">
			<a href='#6.jpg' class='aImg' onclick="return false">
				<img class='images' data-larger="images/6.jpg" id='6' src="images/6s.jpg" alt=''>
			</a>
			</div>
		</div>
	</div>
    %include templates/counter all=all, today=today, last_visit=last_visit, browser=browser
    %include templates/comment_tpl messages=messages
	%include templates/bottom
	<div id='lightBox'>
		<div class="load" id="big">
		<a href='#' id='imageCloser' onclick='return false'>X</a>
		<img id="bigImg" class="bigImg" alt='bigImg' />
		<p>
			<button class="button_cookie" id="started" onclick="start()">Старт</button>
			<!--<button class="button_cookie" id="background_img" onclick="back()">Фон</button>-->
		</p>
		</div>
	</div>
</body>
</html>