


void setup(){
 
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop(){
  int message = get_serial_command_from_pi();
  
  //if (message == 97)
  if(message >= 1)
  {
    Serial.println(message);    
  }
  if (message == 98)
  {
    Serial.println(message, DEC);    
  }
  if (message == 99)
  {
    Serial.println(message, DEC);    
  }  
}

void blink_led(int time){
  digitalWrite(13, HIGH);
   delay(time);
  digitalWrite(13, LOW);
  delay(time);
}


int get_serial_command_from_pi(){
  int byteMessage = 0;
  if(Serial.available()>0){
    byteMessage = Serial.read();
    }
  return byteMessage;
}

