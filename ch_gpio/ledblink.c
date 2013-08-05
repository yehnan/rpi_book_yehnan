#include <stdio.h>
#include <wiringPi.h>

int main()
{
    wiringPiSetupPhys();
    pinMode(12, OUTPUT);

    while(1){
        digitalWrite(12, HIGH);
        delay(1000);
        digitalWrite(12, LOW);
        delay(1000);
    }

    return 0;
}


