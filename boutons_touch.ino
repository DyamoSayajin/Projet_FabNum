char rep1 = 'i';
char rep2 = 'j';
const int touch_trigger = 32;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (touchRead(13)<touch_trigger){
    rep1 = 'a';
  }
  if (touchRead(27)<touch_trigger){
    rep1 = 'b';
  }
  if (touchRead(32)<touch_trigger){
    rep1 = 'c';
  }

  if (touchRead(4)<touch_trigger){
    rep2 = 'x';
  }
  if (touchRead(2)<touch_trigger){
    rep2 = 'y';
  }
  if (touchRead(15)<touch_trigger){
    rep2 = 'z';
  }
  
  Serial.write(rep1);
  Serial.write(rep2);
}