float ballX;
float ballY;

float diameter;
float ballCoLor;

void setup() {
  size(640, 360);
   background(50);
  ballX = 50;
  ballY = 50;
  ballCoLor= 255;
}

void draw(){
  ballX = random(width);
  ballY = random(height);
  diameter = random(10, 45);
  ballCoLor= random(0, 255);

  fill(ballCoLor);
  ellipse(ballX, ballY, diameter, diameter);

  println("ball Position X: " + ballX);
}
