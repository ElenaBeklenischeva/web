window.onload = function add_resolution(){
    var text = 'Разрешение экрана: <br>' + screen.width + '×' + screen.height;
    var resol = document.getElementById("resolution");
    resol.innerHTML = text;
};