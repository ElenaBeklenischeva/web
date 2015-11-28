//function set_cookie(name, value, path, expires) {
//    console.log('set cookie');
//    var cookie_str = name + "=" + value + "; ";
//    if (expires)
//        cookie_str += "expires=" + expires + "; ";
//    if (path)
//        cookie_str += "path=" + path + ";";
//    else
//        cookie_str += "path=/;";
//    document.cookie = cookie_str;
//}
//
//function start(id) {
//    var curr_img = document.getElementById(id);
//    var img = curr_img.getAttribute('src');
//    var date = new Date();
//    date.setFullYear(2016);
//    date.setMonth(1);
//    date.setDate(31);
//    set_cookie('start', img, '', date);
//}

//function back() {
//    var curr_img = document.getElementById('bigImg');
//    var img = curr_img.getAttribute('src');
//    var date = new Date();
//    date.setFullYear(2016);
//    date.setMonth(01);
//    date.setDate(31);
//    set_cookie('back', img, '', date);
//    var back = document.getElementsByName('body');
//    back.style.background = "url('" + img +")";
//    console.log(img);
//}