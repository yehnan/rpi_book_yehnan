#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>

int main()
{
    int i;
    wiringPiSetupPhys();
    softPwmCreate(12, 0, 100);

    while(1){
        for(i = 0; i <= 100; i+=5){
            softPwmWrite(12, i);
            delay(100);
        }
        for(i = 100; i >= 0; i-=5){
            softPwmWrite(12, i);
            delay(100);
        }
    }

    return 0;
}


