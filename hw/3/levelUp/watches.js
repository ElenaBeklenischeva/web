function establishTime(){
  date = new Date();
  seconds = date.getSeconds();
  minutes = date.getMinutes();

  hours = date.getHours();

  if (hours >=12) { hours -= 12 ; }
 
  s = document.getElementById('second');
  s.style.transform = 'rotate(' + seconds * 6 + 'deg)';

  m = document.getElementById("minute");
  m.style.transform = 'rotate(' + minutes * 6 + 'deg)';
  // alert(minutes * 6);
 
  h = document.getElementById('hour');
  h.style.transform = 'rotate(' + (hours * 30 + minutes / 2) + 'deg)';
}