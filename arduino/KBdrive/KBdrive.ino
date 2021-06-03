//A delay of 1000 Microseconds is Full Reverse
//A delay of 1000 to 1460 Microseconds is Proportional Reverse
//A delay of 1460 to 1540 Microseconds is neutral
//A delay of 1540 to 2000 Microseconds is Proportional Forward
//A delay of 2000 Microseconds is Full Forward
const int rightSide = 3;
const int leftSide = 5;
//const int liftMotor = 6;

void setup()
{

  pinMode(rightSide, OUTPUT);
  pinMode(leftSide, OUTPUT);
//pinMode(liftMotor, OUTPUT);
  Serial.begin(57600);
  
}
void loop()
{

    String read1 = Serial.readString();

    if (read1 == "U") {

      digitalWrite(rightSide, HIGH);
      delayMicroseconds(1000);
      digitalWrite(rightSide, LOW);
      delayMicroseconds(1000);

      digitalWrite(leftSide, HIGH);
      delayMicroseconds(1000);
      digitalWrite(leftSide, LOW);
      delayMicroseconds(1000);



    }

    if (read1 == "D") {

      digitalWrite(rightSide, HIGH);
      delayMicroseconds(2000);
      digitalWrite(rightSide, LOW);
      delayMicroseconds(2000);

      digitalWrite(leftSide, HIGH);
      delayMicroseconds(2000);
      digitalWrite(leftSide, LOW);
      delayMicroseconds(2000);



    }

    if (read1 == "R") {

      digitalWrite(rightSide, HIGH);
      delayMicroseconds(2000);
      digitalWrite(rightSide, LOW);
      delayMicroseconds(2000);

      digitalWrite(leftSide, HIGH);
      delayMicroseconds(1000);
      digitalWrite(leftSide, LOW);
      delayMicroseconds(1000);


    }

    if (read1 == "L") {

      digitalWrite(rightSide, HIGH);
      delayMicroseconds(1000);
      digitalWrite(rightSide, LOW);
      delayMicroseconds(1000);

      digitalWrite(leftSide, HIGH);
      delayMicroseconds(2000);
      digitalWrite(leftSide, LOW);
      delayMicroseconds(2000);


    }
  
}
