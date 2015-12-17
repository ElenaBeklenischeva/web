var images_src = ['images/1.jpg',
	'images/2.jpg',
	'images/3.jpg',
	'images/4.jpg',
	'images/5.jpg',
	'images/6.jpg'];
var hrefs = ['#1.jpg',
	'#2.jpg',
	'#3.jpg',
	'#4.jpg',
	'#5.jpg',
	'#6.jpg'];

var images_count = images_src.length;
var curr_image;
var curr_image_position = 0;
var img_b;
var img_f;
var current_id = 'bigImg';

window.onload = function ready(e) {
	//console.log(document.cookie);
	var text = 'Разрешение экрана: <br>' + screen.width + '×' + screen.height;
    var resol = document.getElementById("resolution");
    resol.innerHTML = text;
	var curr_cookie = get_cookie('bigImg');
	if(!curr_cookie)
		curr_cookie = get_cookie('start');
	if (curr_cookie) {
		// console.log(curr_cookie);
		if(Array.prototype.indexOf)
			curr_image_position = images_src.indexOf(curr_cookie);
		else {
			for(var i in images_src) {
				if  (images_src[i] == curr_cookie)
					curr_image_position = i;
			}
		}
		display_inline_box(hrefs[curr_image_position]);
	}
};

function searchIndForIE(src) {
	for(var i in hrefs) {
		if  (hrefs[i] == src)
			return i;
	}
	return -1;
}

function load_next_img(img, src) {
	img = new Image();
	img.src = src;
	img.id = hrefs[curr_image_position];
}

function set_cookie(name, value, path, expires) {
	//console.log('set cookie');
	var cookie_str = name + "=" + value + "; ";
	if (expires)
		cookie_str += "expires=" + expires + "; ";
	if (path)
		cookie_str += "path=" + path + ";";
	else
		cookie_str += "path=/;";
	document.cookie = cookie_str;
}

function delete_cookie ( cookie_name )
{
	// console.log("delete_cookie");
	if(get_cookie(cookie_name)) {
		set_cookie('bigImg', "");
	}
}

function get_cookie ( cookie_name )
{
	// console.log('get_cookie');
	var results = document.cookie.match ( '(^|;) ?' + cookie_name + '=([^;]*)(;|$)' );

	if ( results )
		return ( unescape ( results[2] ) );
	else
		return null;
}

function display_none() {
	var lightBox = document.getElementById('lightBox');
	lightBox.setAttribute('style', 'display: none');

	var bigImg = document.getElementById(current_id);
	bigImg.setAttribute('style', 'display: none');

	var closer = document.getElementById('imageCloser');
	closer.setAttribute("style", "display: none");

	delete_cookie('bigImg');
	//window.history.pushState({href: "#", title: historyC}, null, null);
	//historyC++;
}

function display_inline_box(src) {
	if(Array.prototype.indexOf)
		curr_image_position = hrefs.indexOf(src);
	else
		curr_image_position = searchIndForIE(src);

	var lightBox = document.getElementById('lightBox');
	lightBox.setAttribute("style", "display: block");

	var bigImg = document.getElementById(current_id);
	bigImg.setAttribute('style', 'display: inline-block');
	bigImg.setAttribute('src', images_src[curr_image_position]);
	bigImg.setAttribute('id', src);
	current_id = src;

	var closer = document.getElementById('imageCloser');
	closer.setAttribute("style", "display: block");

	set_cookie('bigImg',images_src[curr_image_position]);
}

document.onclick = function click(e) {
	var id;
	var className;
	var target;
	var parent;
	if (!e) {
		e =  window.event;
		target = e.srcElement;

	} else {
		target = e.target;
	}
	parent = target.parentElement;
	className = target.parentElement.className;
	id = parent.id;

	if(target.id == 'imageCloser' || target.id == 'lightBox' || target.id == 'big') {
		display_none();

	} else
	if (className == 'aImg') {
		var curr_image_src = parent.getAttribute('href');
		//load_next_img(img_f, curr_image_src);

		display_inline_box(curr_image_src);
		if (curr_image_position == (images_src.length - 1))
			load_next_img(img_f, images_src[0]);
		else
			load_next_img(img_f, images_src[Math.abs((curr_image_position + 1) %  images_count)]);
		if (curr_image_position == 0) {
			load_next_img(img_b, images_src[images_src.length - 1]);
		}
		else
			load_next_img(img_b, images_src[Math.abs((curr_image_position - 1) %  images_count)]);

		return false;
	}
};

document.onkeydown = function press(e) {
	e = e || window.event;

	if (e.keyCode == 27 ) {
		display_none();
	} else
	if (e.keyCode == 112) {
		if (e.preventDefault) {
			e.preventDefault();
		} else {
			e.returnValue = false;
		}
		alert("Справка:\nЧтобы открыть картинку, кликните на нее.\nЧтобы закрыть картинку, нажмите ESC или возле картинки на изображение 'X'.\nПри открытой картинке перемещайтесь стрелками '->','<-', чтобы открывать другие картинки.");
	} else
	if (e.keyCode == 39 || e.keyCode == 37) {
		delete_cookie ('bigImg');

		var bigImg = document.getElementById(current_id);
		var curr_id;
		if (e.keyCode == 39) {
			curr_image_position++;
			if(img_f) {
				curr_image = img_f.src;
				curr_id = img_f.id;
			} else {
				curr_image = images_src[Math.abs(curr_image_position %  images_count)];
				curr_id = hrefs[curr_image_position];
			}
		}
		else{
			curr_image_position--;
			if (curr_image_position < 0)
				curr_image_position += images_count;
			if(img_b) {
				curr_id  = img_b.id;
				curr_image = img_b.src;
			} else {
				curr_id = hrefs[curr_image_position];
				curr_image = images_src[Math.abs(curr_image_position %  images_count)];
			}
		}
		bigImg.setAttribute("src", curr_image);
		bigImg.setAttribute('id', curr_id);
		current_id = curr_id;
		set_cookie('bigImg', curr_image);
		//if (e.keyCode == 39) {
			load_next_img(img_f, images_src[Math.abs((curr_image_position + 1) %  images_count)]);
		//} else {
		if (curr_image_position == 0) {
			load_next_img(img_b, images_src[images_src.length - 1]);
		}
		else
			load_next_img(img_b, images_src[Math.abs((curr_image_position - 1) %  images_count)]);
		//}
	}
};

document.onhashchange = function hash_chg(){
	alert('что-то произошло');
};


function start() {
	var curr_img = document.getElementById(current_id);
	var img = curr_img.getAttribute('src');
	var date = new Date();
	date.setFullYear(2016);
	date.setMonth(1);
	date.setDate(31);
	set_cookie('start', img, '', date);
}
