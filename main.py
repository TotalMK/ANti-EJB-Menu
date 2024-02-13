## EJB BLOCKER BY TOTALMK http://www.youtube.com/totalmk ##

## EJB BLOCKER Raspberry Pi Pico I/O:

#                         USB END
#                      [¯¯¯[¯¯]¯¯¯]
#           LED BAR 0 -[GP00  VBUS]-
#           LED BAR 1 -[GP01  VSYS]-
#         -------------[GRND  GRND]------------
#           LED BAR 2 -[GP02  3.3E]-
#           LED BAR 3 -[GP03  3.3O]-
#           LED BAR 4 -[GP04   ADC]-
#           LED BAR 5 -[GP05  GP28]-(EJB Stop Signal) & BLUE LED +
#         -------------[GRND  GRND]------------         BLUE LED - 
#           LED BAR 6 -[GP06  GP27]-
#           LED BAR 7 -[GP07  GP26]-
#           LED BAR 8 -[GP08   RUN]-
#           LED BAR 9 -[GP09  GP22]-
#         -------------[GRND  GRND]------------
#                     -[GP10  GP21]-
#                     -[GP11  GP20]-
#                     -[GP12  GP19]-
#                     -[GP13  GP18]-
# RED LED - -----------[GRND  GRND]------------
# RED LED +           -[GP14  GP17]-
#         (P2 BL) GP15-[GP15  GP16]-
#                      [__/\/\/\__]
#                         | | |_SWIO
#                         | |_-GND-
#                         |_SWCLK

##----------EJB KODES----------##
##[BL :P1|P2|P1|P2|P1|P2|P1|P2]##
##[MK1:05|10|02|01|02|03|04|  ]##
##[MK2:05|10|02|08|02|        ]##
##[MK3:05|10|03|01|02|02|03|04]##

#Import Classes#
import utime, machine, gc
from machine import Pin, Timer
from time import sleep_ms, sleep

def reset(source):
    global baroff
    global counter_p2bl
    print('')
    counter_p2bl = DEFAULT_COUNTER_VALUE
    print('RESETING PLAYER 2 BL COUNTER=' + str(counter_p2bl))
    baroff()
    reset_timer.deinit()

def baroff():
    ledbar0.value(0)
    ledbar1.value(0)
    ledbar2.value(0)
    ledbar3.value(0)
    ledbar4.value(0)
    ledbar5.value(0)
    ledbar6.value(0)
    ledbar7.value(0)
    ledbar8.value(0)
    ledbar9.value(0)
    
#Counter Config#
DEFAULT_COUNTER_VALUE = 0
COUNTER_CHANGE = 1

#P2 BL Counter
counter_p2bl = DEFAULT_COUNTER_VALUE
print('PLAYER 2 BL COUNTER IS CURRENTY: {}.'.format(counter_p2bl))

#GPIO Button And Switch Config#
p2_bl_button = Pin(15, Pin.IN, Pin.PULL_UP)

#GPIO Devices Config#
ejbkodestop = Pin(18, Pin.OUT, Pin.PULL_UP) #P2 BL
ejbkodestop.value(1)

#EJB Kode Intensity /10
ledbar0 = Pin(0, Pin.OUT)
ledbar1 = Pin(1, Pin.OUT)
ledbar2 = Pin(2, Pin.OUT)
ledbar3 = Pin(3, Pin.OUT)
ledbar4 = Pin(4, Pin.OUT)
ledbar5 = Pin(5, Pin.OUT)
ledbar6 = Pin(6, Pin.OUT)
ledbar7 = Pin(7, Pin.OUT)
ledbar8 = Pin(8, Pin.OUT)
ledbar9 = Pin(9, Pin.OUT)

ledbar0.value(0)
ledbar1.value(0)
ledbar2.value(0)
ledbar3.value(0)
ledbar4.value(0)
ledbar5.value(0)
ledbar6.value(0)
ledbar7.value(0)
ledbar8.value(0)
ledbar9.value(0)

#Stop EJB LED
stopejb = Pin(13, Pin.OUT)
stopejb.value(0)

while True:

    #Empty Cache
    gc.collect()
    
    if  p2_bl_button.value()==0 and counter_p2bl <=10:
        print('P2 BL PUSHED')
        counter_p2bl = counter_p2bl + COUNTER_CHANGE
        print('> PLAYER 2 BL COUNTER IS CURRENTY: {}.'.format(counter_p2bl))
        print('')
        sleep(0.1)
        
    #Reset LEDs when Kode hits 10
    if  counter_p2bl >=10:
        baroff()
        
    #Start an ecapsulation timer when Kode hits '2' 3 seconds pass and counter is reset
    if counter_p2bl == 1:
        reset_timer = Timer(period=3000, mode=Timer.PERIODIC, callback=reset)
    
    #Display Kode Intensity LEDs
    if counter_p2bl == 1: #1/10 LEDS ON
        ledbar0.value(1)
    if counter_p2bl == 2: #2/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
    if counter_p2bl == 3: #3/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
    if counter_p2bl == 4: #4/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
        ledbar3.value(1)
    if counter_p2bl == 5: #5/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
        ledbar3.value(1)
        ledbar4.value(1)
    if counter_p2bl == 6: #6/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
        ledbar3.value(1)
        ledbar4.value(1)
        ledbar5.value(1)
    if counter_p2bl == 7: #7/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
        ledbar3.value(1)
        ledbar4.value(1)
        ledbar5.value(1)
        ledbar6.value(1)
    if counter_p2bl == 8: #8/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
        ledbar3.value(1)
        ledbar4.value(1)
        ledbar5.value(1)
        ledbar6.value(1)
        ledbar7.value(1)
    if counter_p2bl == 9: #9/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
        ledbar3.value(1)
        ledbar4.value(1)
        ledbar5.value(1)
        ledbar6.value(1)
        ledbar7.value(1)
        ledbar8.value(1)

# EJB Kode Kancel when P2 BL Kode hits '10'

    if counter_p2bl == 10: #10/10 LEDS ON
        ledbar0.value(1)
        ledbar1.value(1)
        ledbar2.value(1)
        ledbar3.value(1)
        ledbar4.value(1)
        ledbar5.value(1)
        ledbar6.value(1)
        ledbar7.value(1)
        ledbar8.value(1)
        ledbar9.value(1)  
        print('P2 BL X 10 EJB KODE FRAGMENT DETECTED')
        print('SABOTAGING EJB KODE!')
        ejbkodestop.value(0)
        sleep_ms(50)
        ejbkodestop.value(1)
        sleep_ms(50)
        ejbkodestop.value(0)
        sleep_ms(50)
        ejbkodestop.value(1)
        print('DONE!')
        print('NO FREE PLAY FOR YOU!!')
        print('HIGH SCORES PROTECTED!!')
        print('')
        counter_p2bl = DEFAULT_COUNTER_VALUE
        stopejb.value(1)
        sleep(0.5)
        stopejb.value(0)
        baroff()

## END EJB BLOCKER ##
