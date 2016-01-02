function add_like(){
//    alert('likes');
    var req = new XMLHttpRequest();
    var results = document.cookie.match ( '(^|;) ?bigImg=([^;]*)(;|$)' );
    if (results) {
        results = unescape ( results[2] );
        results = results.split('/')[1];
    }

    var href = window.location.href + '/counter';
//    alert(href)
    var answer = "img=" + results;

    req.open('POST', href, true);
//    req.setRequestHeader('Content-Type', 'multipart/form-data');

	req.onreadystatechange = function() {
	    if (req.readyState == 4) {
			if(req.status == 200) {
//			    alert((req.responseText.split(':')[1]).split('}')[0]);
			    document.getElementById('like').innerHTML = '&hearts;' + (req.responseText.split(':')[1]).split('}')[0];
			}
		}
	}
	req.send('img' + results);
}
