



void setup() {
  size(640, 360);
  background(50);
}

void draw() {

println("DRAW BEGINS !");
  
  
  for (int X = 30; X < width - 30; X = X + 30 )
  for (int Y = 30; Y< height - 30; Y = Y + 30 ) {
    ellipse (X,Y,30, 30);
  }
}
