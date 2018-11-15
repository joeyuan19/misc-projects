 //servo control
 unsigned char servo = 6;
 unsigned char count = 0;
 unsigned char i = 0;
 unsigned char servoTime = 0;
 unsigned char servoValue = 0;
 unsigned char flag = 0;
 unsigned int secondT = 0;
 
 unsigned int k = 0;
 
 //pen
 const unsigned int down = 50;
 const unsigned int up = 100;
 
 //motor
 int L1 = 9;
 int L2 = 7;
 
 int R1 = 10;
 int R2 = 8;
 
 //speed and time
 int dir = 0;
 int speeds = 0;
 unsigned long time = 0;
 
 long serialValue = 0;
 int length = 0;

 unsigned char cmd[400];
 
void setup()
{  
  UBRRL=103;   //16M baud 9600，8bit UART
  UCSRB=0x18; //enable

  pinMode(servo,OUTPUT);
  digitalWrite(servo,LOW);
  //pin for motor
  pinMode(L1,OUTPUT);
  pinMode(L2,OUTPUT);
  pinMode(R1,OUTPUT);
  pinMode(R2,OUTPUT);
  
  timer2();
  TIMSK &= ~(2 << 6);
  digitalWrite(servo,LOW);
  
  time = 300;
  penWrite();
  penRise();
}

void loop()
{
   while(!(UCSRA&(1<<RXC)));
   if(UDR == 170)
   {
     while(!(UCSRA&(1<<RXC)));
     if(UDR == 85)
    {
      while(!(UCSRA&(1<<RXC)));
      length = UDR;
	  length = length << 2;
      
      for (k = 0;k<length;++k)
      {
        while(!(UCSRA&(1<<RXC)));
        cmd[k] = UDR;
        while(!(UCSRA&(1<<RXC)));
        cmd[++k] = UDR;
        while(!(UCSRA&(1<<RXC)));
        cmd[++k] = UDR;
        while(!(UCSRA&(1<<RXC)));
        cmd[++k] = UDR;
       }
      
       while(!(UCSRA&(1<<RXC)));
       if(UDR != 0xe0)
         return;
       while(!(UCSRA&(1<<RXC)));
       if(UDR != 0x07)
         return;
        
        for (k = 0;k<length;++k)
       {
         dir = (cmd[k] & 0xf0) >> 4;
         speeds = (cmd[k] & 0xf) * 17;
         time = 0;
         time = time | cmd[++k];
         time = time << 8 | cmd[++k];
         time = time << 8 | cmd[++k];
         
         switch (dir)
         {
         case 8: 
           stoprun();
           break;
         case 0:
           gforward();
           break;
         case 1:
           gback();
           break;
         case 2:
           turnLeft();
           break;
         case 3:
           turnRight();
           break;
         case 4:
           gLF();
           break;
         case 5:
           gRF();
           break;
         case 6:
           gLB();
           break;
         case 7:
           gRB();
           break;
         case 9:
           penWrite();
           break;
         case 10:
           penRise();
           break;
         default: stoprun();
        }
       }
   cmd[0] = UDR;
    }
  }
}

//timer2 for servo control
void timer2()
{
  noInterrupts();
  TCCR2 = 0x0f;       //CTC,1024
  OCR2 = 155;
  TIMSK |= (2 << 6);
  interrupts();
}

//each interrupt 25hz
ISR(TIMER2_COMP_vect)
{
  
//two intrupt as a circle
   if(secondT == 0)
   {
    digitalWrite(servo,HIGH);
    secondT++;
    flag = 0;
   }
   else
   {
    secondT = 0;
   }
  
   //finished in 10ms
   for(count = 0;count<127;count++)
   {
     if(flag == 1)
     {
      return;    
     }
     
     //for(i = 0;i != 120;i++);
     delayMicroseconds(76);
     if(servoTime == servoValue)
     {
      digitalWrite(servo,LOW);
      flag = 1;
      servoTime = 0;
      //secondT++;
      return;
     }
     else
     {
       servoTime++;
     }
   }
}


//stop
void stoprun()
{
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
  delay(time);
}


void gforward()
{
  //leftmotor
  analogWrite(L1,speeds);
  digitalWrite(L2,LOW);
  //right motor
  analogWrite(R1,speeds);
  digitalWrite(R2,LOW);
  delay(time);
  
  digitalWrite(L1,LOW);
  digitalWrite(R1,LOW);
}

//goback
void gback()
{
  //leftmotor
  analogWrite(L1,speeds);
  digitalWrite(L2,HIGH);
  
  //right motor
  analogWrite(R1,speeds);
  digitalWrite(R2,HIGH);
  delay(time);
  
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
}

void turnLeft()
{
  analogWrite(L1,speeds);
  digitalWrite(L2,HIGH);
  
  analogWrite(R1,speeds);
  digitalWrite(R2,LOW);
  delay(time);
  
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
}

void turnRight()
{
  analogWrite(L1,speeds);
  digitalWrite(L2,LOW);
  
  analogWrite(R1,speeds);
  digitalWrite(R2,HIGH);
  delay(time);
  
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
}

void gLF()
{
  analogWrite(L1,speeds/2);
  digitalWrite(L2,LOW);

  analogWrite(R1,speeds);
  digitalWrite(R2,LOW);
  delay(time);
  
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
}

void gRF()
{
  analogWrite(L1,speeds);
  digitalWrite(L2,LOW);

  analogWrite(R1,speeds/2);
  digitalWrite(R2,LOW);
  delay(time);
  
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
}

void gLB()
{
  analogWrite(L1,speeds/2);
  digitalWrite(L2,HIGH);
  
  analogWrite(R1,speeds);
  digitalWrite(R2,HIGH);
  delay(time);
 
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
}

void gRB()
{
  analogWrite(L1,speeds);
  digitalWrite(L2,HIGH);
  
  analogWrite(R1,speeds/2);
  digitalWrite(R2,HIGH);
  delay(time);
  
  digitalWrite(L1,LOW);
  digitalWrite(L2,LOW);
  
  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
}

void penWrite()
{
TIMSK |= (2 << 6);
servoValue = 14;
delay(150);
delay(time);
}

void penRise()
{
 TIMSK |= (2 << 6);
 servoValue = 20;
 delay(150);
 delay(time);
}
