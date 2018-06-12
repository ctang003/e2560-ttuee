#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "bcm2835.h"

void setpin(); //set pin mode
int check_mode(); //determine voltage or current mode
void Get_battery_info();//catch battery voltage and current
void Number_Change(int* battery_info, double *info_ptr);//change the time into two number 
void seven_segment(int seven_number, int display_number);//depending on the time display the seven segment
void zero(int choose);	//number zero of seven segment 
void one(int choose);		//number one of seven segment
void two(int choose);		//number two of seven segment
void three(int choose);	//number three of seven segment
void four(int choose);	//number four of seven segment
void five(int choose);	//number five of seven segment
void six(int choose);		//number six of seven segment
void seven(int choose);	//number seven of seven segment
void eight(int choose);	//number eight of seven segment
void nine(int choose);	//number nine of seven segment
void delay_each();		//the delay time between each seven segment 			

int PIN[4] = {17, 18, 27, 22};	//the pin of seven segment from D0 to D3
int seven_pin[8] = {25, 11, 8, 7, 14, 1, 5 ,6};//the pin of seven segment from a to p
int DB_pin[8] = {12, 13, 19, 16, 26, 20, 21, 4}; //digtial output of adc
int mode_pin[2] = {3, 15}; //voltage mode or current mode
int WR_PIN = 0;
int INTR_PIN = 2 ;

int battery_info[8]; //the location put battery information 
int segment7_order[4];
int *bat_info_ptr;
double *infoptr;	//battery information pointer
double temp;

int main(int argc, char **argv){
	
	int number;
	int i;
	
	bat_info_ptr = malloc(sizeof(int));
	infoptr = malloc(sizeof(double));
	
	bat_info_ptr = &battery_info[0];	

	printf("begin\n");	

	if(!bcm2835_init()){ 
		printf("initial fail\n");	
		return -1;
	}
	setpin();
	printf("set pin complete\n");
	while(1){
	
		//itial ic pin 
		bcm2835_gpio_write(INTR_PIN,HIGH);
		printf("(bcm2835_gpio_lev(INTR_PIN):%d\n", bcm2835_gpio_lev(INTR_PIN));
		Get_battery_info();
		printf("check out\n");
		Number_Change(bat_info_ptr, infoptr);
		for(number = 0; number < 4; number++){
			seven_segment(number,segment7_order[number]);	
		delay(5);		
		}
	}
	return 0;
}

//set pin mode
void setpin(){
	int i;
	for(i = 0; i < 4; i++){
		bcm2835_gpio_fsel(PIN[i], BCM2835_GPIO_FSEL_OUTP);	
	}
	
	for(i = 0; i < 8; i++){
		bcm2835_gpio_fsel(seven_pin[i], BCM2835_GPIO_FSEL_OUTP);
		bcm2835_gpio_fsel(DB_pin[i], BCM2835_GPIO_FSEL_INPT);
	}

	for(i = 0; i < 2; i++){
		bcm2835_gpio_fsel(mode_pin[i], BCM2835_GPIO_FSEL_INPT);
	}
	
	bcm2835_gpio_fsel(WR_PIN, BCM2835_GPIO_FSEL_OUTP);
	bcm2835_gpio_fsel(INTR_PIN, BCM2835_GPIO_FSEL_INPT);

	return;
}

//catch battery voltage and current
void Get_battery_info(){

	int checkref = 0; //check the data is ready or not
 	int i; 				//loop counter
	
	bcm2835_gpio_write(WR_PIN,LOW);
	bcm2835_gpio_write(WR_PIN, HIGH);		
	while(checkref != 1){
		printf("checkref:%d\n", checkref);
		if((bcm2835_gpio_lev(INTR_PIN) == LOW)){
			printf("enter checked\n");
			for(i = 0; i < 8; i++){
				if(bcm2835_gpio_lev(DB_pin[i]) == HIGH){
					battery_info[i] = 1;
				}
				else{
					battery_info[i] = 0;
				}
				//printf("battery_info[%d]:%d\n", i, battery_info[i]);
			}
		checkref = 1;
		}
		else{
			printf("data is not ready for reading");
		}
	}
	return;		
}//end_Get_voltage_current

//determine voltage or current mode
int check_mode(){
	if(bcm2835_gpio_lev(mode_pin[0]) == HIGH){
		return 0;	//voltage mode
	}
	else if(bcm2835_gpio_lev(mode_pin[1]) == HIGH){
		return 1;	//current mode
	}
	else{
		printf("read pin mode error\n");
	}
}//end check_mode() 

//change the time into two number
void Number_Change(int* battery_info, double *infoptr){	
	int i;
	temp = 0;
		for(i = 0; i < 8; i++){
			printf("battery_info[%d]:%d\n", i, battery_info[i]);
			temp += battery_info[i]* pow(2,i);
			*infoptr  = temp;
			printf("infoptr:%f\n", *infoptr);
		} 

		printf("final infoptr:%f\n", *infoptr);
		
		*infoptr = *infoptr /256 *20;
		
		//printf("final infoptr:%f\n", *infoptr);
		
		*infoptr *=100000;
		
		segment7_order[0] = (int)*infoptr %1000000 /100000;
		segment7_order[1] = (int)*infoptr %100000 /10000;
		segment7_order[2] = (int)*infoptr %10000 /1000;
		segment7_order[3] = (int)*infoptr %1000 /100;			
		
		for( i = 0; i < 4; i++){
			printf("segment7_order[%d]: %d\n", i, segment7_order[i]);
		}
		printf("test:%d\n", (int) *infoptr);	
}


//depending on the time display the seven segment
void seven_segment(int seven_number,int display_number){
	int j;
	for(j = 0; j < 4; j++){
		if(j != seven_number){
			bcm2835_gpio_write(PIN[j],LOW);
			delay_each();
		}
	}
	switch(display_number){
		case 0:
			zero(seven_number);
			break;
		case 1:
			one(seven_number);
			break;
		case 2:
			two(seven_number);
			break;
		case 3:
			three(seven_number);
			break;
		case 4:
			four(seven_number);
			break;
		case 5:
			five(seven_number);
			break;
		case 6:
			six(seven_number);
			break;
		case 7:
			seven(seven_number);
			break;
		case 8:
			eight(seven_number);
			break;
		case 9:
			nine(seven_number);
			break;
		default:
			break;
	}
	bcm2835_gpio_write(PIN[seven_number],HIGH);
	delay_each();
}
	
//number zero of seven segment
void zero(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j ==7 || j == 6){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
						delay_each();
		}
	}		
}

// number one of seven segment
void one(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j ==1 || j==2){
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}

//number two of seven segment
void two(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j ==2 || j==5 ||j == 7){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}

//number three of seven segment 
void three(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j ==4 || j==5 || j==7){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}

//number four of seven segment 
void four(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j == 0 || j == 3 || j== 4 || j ==7){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}

//number five of seven segment 
void five(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j == 1 || j == 4 || j ==7){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}

//number six of seven segment 
void six(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j == 1 || j ==7){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}


//number seven of seven segment 
void seven(int choose){	
	int j;
	for(j = 0; j < 8; j++){
		if(j ==0 || j==1 || j ==2){
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
	}	
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}

//number eight of seven segment 
void eight(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if( j ==7){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}	
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}	
}

//number nine of seven segment 
void nine(int choose){
	int j;
	for(j = 0; j < 8; j++){
		if(j ==4 || j ==7){
			bcm2835_gpio_write(seven_pin[j],HIGH);
			delay_each();
		}
		else{
			bcm2835_gpio_write(seven_pin[j],LOW);
			delay_each();
		}
	}
	if(choose == 0){
		bcm2835_gpio_write(seven_pin[7],LOW);
	}
}


//the delay time between each seven segment 
void delay_each(){
	delay(0.1);
}