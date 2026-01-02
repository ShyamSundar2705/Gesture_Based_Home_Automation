int valsRec[1];
String inputString = "";

void setup() {
  pinMode(23, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() > 0) {
    char inChar = Serial.read();

    if (inChar == '$') {
      inputString = "";
    } 
    else if (isDigit(inChar)) {
      inputString += inChar;
    } 
    else if (inChar == '\n' || inChar == '\r') {
      if (inputString.length() > 0) {
        valsRec[0] = inputString.toInt();
        analogWrite(23, valsRec[0]);
        inputString = "";
      }
    }
  }
}
