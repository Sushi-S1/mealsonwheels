const int spike1 = 3;
const int spike2 = 5;
const int spike3 = 6;
const int spike4 = 9;
const int spike5 = 10;


void setup() {
  Serial.begin(57600);


}

void loop() {
  while (!Serial.available()) {
  }
  while (Serial.available()) {

    char readser2 = Serial.read();

    if (readser2 == "UP") {

      digitalWrite(spike1, HIGH);
    }

    else if (readser2 == "DOWN") {

      digitalWrite(spike2, HIGH);
    }

    else if (readser2 == "RIGHT") {

      digitalWrite(spike3, HIGH);
    }

    else if (readser2 == "LEFT") {

      digitalWrite(spike4, HIGH);
    }

    else if (readser2 == "T") {

      digitalWrite(spike5, HIGH);
    }
  }

}
