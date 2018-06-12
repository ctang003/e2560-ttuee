#include <wiringPi.h>
#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include <ctype.h>
#include <string.h>
static int digits   [8] = {  26, 27,28,29,5,6,10,11 } ;
static int segments [7] = {  25,24,23,22,21,14,13} ;
static int btset[9]     = {  3,2,0,7,9,8,15,16,1};
static int segmentDigits [10][7] =

// a  b  c  d  e  f  g     Segments
// 6  5  4  3  2  1  0,	// wiringPi pin No.
{
   {1, 1, 1, 1, 1, 1, 0},	// 0
   {0, 1, 1, 0, 0, 0, 0},	// 1
   {1, 1, 0, 1, 1, 0, 1},	// 2
   {1, 1, 1, 1, 0, 0, 1},	// 3
   {0, 1, 1, 0, 0, 1, 1},	// 4
   {1, 0, 1, 1, 0, 1, 1},	// 5
   {1, 0, 1, 1, 1, 1, 1},	// 6
   {1, 1, 1, 0, 0, 0, 0},	// 7
   {1, 1, 1, 1, 1, 1, 1},	// 8
   {1, 1, 1, 1, 0, 1, 1}	// 9

};
char chr [8] ;

void ptff1 (void)

{

int g1=0;
int g2=0;
int w =0;
for(g2=0;g2<8;g2++)
{

w=chr[g2]-48;
if(w==-16)
w=0;
digitalWrite (digits[g2], 0);
for (g1 = 0 ; g1 < 7 ; ++g1)
{digitalWrite (segments [g1],segmentDigits [w][g1] );}
delay(1);
digitalWrite (digits[g2], 1);

}


}




void setup(void)
{
  int i, c ;

  wiringPiSetup () ;

// 7 segments

  for (i = 0 ; i < 7 ; ++i)
    { pinMode (segments [i], OUTPUT) ;digitalWrite (segments [i], 0) ;
       }

// 6 digits

  for (i = 0 ; i < 8 ; ++i)
    {  pinMode (digits [i],   OUTPUT) ;digitalWrite (digits [i], 1) ;   }
 

 for (i = 0 ; i < 9 ; ++i)
    {  pinMode (btset [i],   INPUT) ;   }

}









int main(void)
{	
	int ap = 0;
	int vo = 0;
	int i  = 0;
	
	setup    () ;
	printf("hello\n");
	for(i=0;i<100;i++)
	{
	for (i=0;i<9;i++)
	{
	if(digitalRead(btset[i]))
	ap = i;
	}
	int gg = 0;
	vo = (ap*48)*10000;
        gg = 48*ap+vo;

	sprintf(chr,"%8d",gg);
	ptff1();

	}

	  	
	
	
}


























