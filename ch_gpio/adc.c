#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <unistd.h>

int readadc(int ch)
{
    int errno;
    unsigned char data[3];
    unsigned int adcout;
    wiringPiSPISetup(0, 500000);

    data[0] = 1; 
    data[1] = (8 + ch) << 4; 
    data[2] = 0; 

    errno = wiringPiSPIDataRW(0, data, 3);

    adcout = ((data[1] & 0x03) << 8) + data[2];

    return adcout;
}

int main(int argc, char *argv[])
{
    int ch;
    wiringPiSetupPhys();
    while(1){
        for(ch = 0; ch <= 1; ch++){
            int rst = readadc(ch);
            printf("ch %d is %d\n", ch, rst);
        }
        sleep(1);
    }

    return 0;
}


