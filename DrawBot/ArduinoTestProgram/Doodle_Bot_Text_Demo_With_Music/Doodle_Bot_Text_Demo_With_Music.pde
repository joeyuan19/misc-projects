
#include "Constants.h"
#include "IOpins.h"
#include "Notes.h"

int volts;                                         // battery voltage
int pause=-1;                                      // a value of -1 means the battery voltage is ok, 0 and 1 are used to flash LED on D13 when the battery is flat
byte pen;
byte turn;

int lspeed;                                        // left  speed -255 to +255 (negative values are reverse)
int rspeed;                                        // right speed -255 to +255 (negative values are reverse)
int dspeed=80;                                     // draw  speed  +50 to +200

volatile int rcount;
volatile int lcount;

void setup()
{
  attachInterrupt(0,Rcount,CHANGE);
  attachInterrupt(1,Lcount,CHANGE);
  
  Serial.begin(57600);                             // initialize serial interface - 9600 baud   
  pinMode(Ldirpin,OUTPUT);                         // set left  direction pin as an output pin
  pinMode(Rdirpin,OUTPUT);                         // set right direction pin as an output pin
  pinMode(Srvopin,OUTPUT);                         // set servo  control  pin as an output pin
  
  digitalWrite(2,1);                               // enable pullup resistor on D2
  digitalWrite(3,1);                               // enable pullup resistor on D3
  
  Up();                                            // start the program with the pen raised
  
  //--------------------------------------------------------------------------- play tune on powerup / reset --------------------------

  pinMode(7,OUTPUT);                                                         // left  motor direction           
  pinMode(8,OUTPUT);                                                         // right motor direction
  pinMode(9,OUTPUT);                                                         // left  motor PWM
  pinMode(10,OUTPUT);                                                        // right motor PWM
  pinMode(13,OUTPUT);
  
  
  digitalWrite(13,1);                                                        // turn on D13 LED as indicator that program is running

  int tempo=700;                                                             // changes the tempo (speed) that the music plays at
  int notes=29;                                                              // number of notes to be played

  int melody[]={                                                             // define your melody here
    NOTE_C6,NOTE_C6,NOTE_C6,NOTE_D6,NOTE_E6,0,
    NOTE_E6,NOTE_D6,NOTE_E6,NOTE_F6,NOTE_G6,0,
    NOTE_C7,NOTE_C7,NOTE_C7,NOTE_G6,NOTE_G6,NOTE_G6,NOTE_E6,NOTE_E6,NOTE_E6,NOTE_C6,NOTE_C6,NOTE_C6,
    NOTE_G6,NOTE_F6,NOTE_E6,NOTE_D6,NOTE_C6
  };

  byte noteDurations[]={                                                     // define the duration of each note here
    2,2,2,4,2,4,
    2,4,2,4,2,4,
    4,4,4,4,4,4,4,4,4,4,4,4,
    2,4,2,4,2
  };
  for (byte Note = 0; Note < notes; Note++)                                  // Play melody
  {
    long pulselength = 1000000/melody[Note];
    long noteDuration = tempo/noteDurations[Note];
    long pulses=noteDuration*tempo/pulselength;
    if (pulselength>100000)
    {
      delay(noteDuration);
    }
    else
    {
      for(int p=0;p<pulses;p++)
      {                                                                      // drive motors forward
        digitalWrite(7,0);                                                   // left  motor DIR pin
        digitalWrite(8,0);                                                   // right motor DIR pin
        digitalWrite(9,1);                                                   // set left  PWM to 100%
        digitalWrite(10,1);                                                  // set right PWM to 100%
        delayMicroseconds(pulselength/2-20);                                 // frequency of note divide by 2
        
                                                                             // drive motors backward
        digitalWrite(7,HIGH);                                                // left  motor PWM pin                                                
        digitalWrite(8,HIGH);                                                // right motor PWM pin
        delayMicroseconds(pulselength/2-20);                                 // frequency of note divide by 2
      }
      
      digitalWrite(9,0);                                                     // turn off left  motor for pause between notes
      digitalWrite(10,0);                                                    // turn off right motor for pause between notes
      int pauseBetweenNotes = noteDuration * 0.30;                           // short pause between notes
      delay(pauseBetweenNotes);
    }
  }
  digitalWrite(13,0);                                                        // music finished, turn off D13 LED
  delay(1000);
}

void loop()
{ 
  volts=analogRead(Battery)/10;
  
  if(volts<lowbat || pause!=-1)                    // once voltage falls below lowbat value
  {
    lspeed=0;                                      // stop left  motor
    rspeed=0;                                      // stop right motor
    Motors();                                      // update motor control pins
    if (pause<0) Up();                             // make sure pen is raised when battery first falls below lowbat value
    pause++;                                       // increment pause
    if(pause>1) pause=0;                           // toggle pause between 0 and 1 once battery is flat
    digitalWrite(13,pause);                        // flash LED on D13
    delay(200);                                    // set flashing LED speed
    return;                                        // reset loop
  }
                                                   // current is proportional to voltage and power = voltage x current
                                                   // As the battery voltage drops dspeed increases to maintain a constant speed
  
  dspeed=26214/volts*10/volts;                     // draw speed power correction factor=100% when battery=5V (analog reading = 512)
  dspeed=dspeed*8/10;                              // adjust speed to reduce overshoot
   
  I();Space();L();Heart();V();E();Space();M();U();S();I();C();Space();END();
  //I();Space();A();M();Space();A();Space();R();O();B();O();T();Space();END();
  //A();B();C();D();E();F();G();H();I();J();K();L();M();N();O();P();Q();R();S();T();U();V();W();X();Y();Z();END();
  //N0();N1();N2();N3();N4();N5();N6();N7();N8();N9();END();
}


  





