function upper(){
    var button = document.getElementById('comment_b');
    var div = document.getElementById("comment_button");
    var attrDiv = button.getAttribute('value');
    console.log('upper');
    if (attrDiv == '0') {
        div.setAttribute('style', 'display:block');
        div.setAttribute('style', 'right:0');
        button.setAttribute('value', '1');
        button.setAttribute('style', 'right:340px');
    } else {
        div.setAttribute('style', 'display:hidden');
        div.setAttribute('style', 'right:-335px');
        button.setAttribute('value', '0');
        button.setAttribute('style', 'right:5');
    }
}

