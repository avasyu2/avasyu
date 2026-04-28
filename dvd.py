const dvd = document.getElementById('dvd');
let x = 0, y = 0;
let xSpeed = 2, ySpeed = 2; // Movement speed

function animate() {
  const screenWidth = window.innerWidth;
  const screenHeight = window.innerHeight;
  const logoWidth = dvd.offsetWidth;
  const logoHeight = dvd.offsetHeight;

  // Update position
  x += xSpeed;
  y += ySpeed;

  // Collision detection: Left/Right
  if (x + logoWidth >= screenWidth || x <= 0) {
    xSpeed *= -1;
    changeColor();
  }

  // Collision detection: Top/Bottom
  if (y + logoHeight >= screenHeight || y <= 0) {
    ySpeed *= -1;
    changeColor();
  }

  dvd.style.left = x + 'px';
  dvd.style.top = y + 'px';

  requestAnimationFrame(animate);
}

function changeColor() {
  const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
  dvd.style.backgroundColor = randomColor;
}

animate();
