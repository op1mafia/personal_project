
void setup(){
  size(1000, 1000);
}

void draw(){
  background(0);//set background to black
  ellipseMode(CENTER);
  ellipse(mouseX, mouseY, 550, 100);
}

void mousePressed(){
  fill(255,0,0);
}

void keyPressed(){
  fill(0,255,255);
}
