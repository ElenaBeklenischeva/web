function draw_circle(r, color){
	var example = document.getElementById("clock"),
	ctx = example.getContext('2d');
	ctx.fillStyle=color;
	ctx.strokeStyle="#bdbdbd";
	ctx.beginPath();
	ctx.arc(350, 155, r, 0, 360);
	ctx.fill();
	ctx.stroke();
}

function draw_line(width_line, start_x, start_y){
	var example = document.getElementById("clock"),
	ctx = example.getContext('2d');
	ctx.strokeStyle="#000";
	ctx.lineWidth=width_line;
	ctx.beginPath();
	ctx.moveTo(350, 155);
	ctx.lineTo(start_x, start_y);
	ctx.stroke();
}

function draw_numeric() {
	var example = document.getElementById("clock"),
	ctx = example.getContext('2d');
	ctx.fillStyle = "#000";
    ctx.strokeStyle = "#F00";
    ctx.font = "20pt Arial";
    // ctx.fillText("12", 335, 30);
    // ctx.fillText("3", 480, 159);
    // ctx.fillText("6", 340, 300);
    // ctx.fillText("9", 207, 159);
    for (i = 1; i < 13; i++) {
    	ctx.fillText(i, 335 + Math.cos(i * Math.PI/30 - Math.PI/2),
    		30 + Math.sin(i * Math.PI/30 - Math.PI/2));
    }
    // ctx.stroke();
}

function update(){
	// alert("here");
	draw_circle(150, "#D8D8D8");
	draw_numeric();
	draw_circle(10, "#000");
	date = new Date();
	seconds = date.getSeconds() * Math.PI/30 - Math.PI/2;
	minutes = date.getMinutes() * Math.PI/30 - Math.PI/2;
	// alert(minutes);
	hours = date.getHours() * Math.PI/6 - Math.PI/2;
	draw_line(3, 350 + Math.cos(seconds) * 110, 155 + Math.sin(seconds) * 110);
	draw_line(7, 350 + Math.cos(hours) * 70, 155 + Math.sin(hours) * 70);
	draw_line(5, 350 + Math.cos(minutes) * 90, 155 + Math.sin(minutes) * 90);
}

window.onload = function get_watches(){
	// var example = document.getElementById("clock"),
	// ctx = example.getContext('2d');
	setInterval(update(), 10);
}