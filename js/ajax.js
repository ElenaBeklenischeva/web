function vote() {
	var statusElem = document.getElementById('submit');
	var message = document.getElementById('comment').value;
	var req = new XMLHttpRequest();
    var href = window.location.href;
    req.open('POST', href, true);
	req.send('answer_form=' + message);

	req.onreadystatechange = function() {
		if (req.readyState == 4 && req.status == 200) {
				document.getElementById('answers_form').innerHTML = req.responseText;
				document.getElementById('comment').value = "";
				return false;
		}
	}
    return false;
}

function onDownload() {
//    alert('onload');
    var req = new XMLHttpRequest();
    var href = window.location.href + '/file';
//    alert(href);
    req.open('GET', href, true);
    req.send();
//    alert('send')
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status == 200) {
//            alert(req.responseText);
//            download(req.responseText, '/likes.xml', 'text/xml');
//            window.location = './likes.xml';
            var ifrm = document.getElementById("frame");
            ifrm.src = './likes.xml';
            return '#';
        }
    }
}