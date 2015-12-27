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
