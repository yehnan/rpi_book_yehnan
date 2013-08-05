#include <stdio.h>
#include <wiringPi.h>

int main()
{
    int ledStatus = LOW;
    unsigned int t = 0;

    wiringPiSetupPhys();
    pinMode(12, OUTPUT);
    pinMode(11, INPUT);
    digitalWrite(12, ledStatus);

    while(1){
        int switchStatus = digitalRead(11);
        if(switchStatus == HIGH){
            unsigned int temp = millis();
            if(temp - t > 300){
                t = temp;
                ledStatus = ledStatus == HIGH ? LOW : HIGH;
                digitalWrite(12, ledStatus);
            }
        }
    }

    return 0;
}


