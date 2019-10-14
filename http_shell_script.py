# !usr/bin/python
import sys
import os


def print_success_request():
    print()
    print("##############################################")
    print("############ SUCCESS SEND REQUEST ############")
    print("##############################################")


def print_request_message(url):
    print()
    print("############## REQUEST MESSAGE ###############")
    print(url)
    print("##############################################")


print("##############################################")
print("############# HTTP SHELL SCRIPT ##############")
print("##############################################")
print()

METHOD = sys.argv[1]

if METHOD == 'GET':
    print(" ##########    ############      ###########")
    print("###            ##                    ##     ")
    print("##             ##                    ##     ")
    print("##     ####    ############          ##     ")
    print("##       ##    ##                    ##     ")
    print("###      ##    ##                    ##     ")
    print(" ##########    ############          ##     ")

    URL = "http GET http://127.0.0.1:8000/post/"

    print_request_message(URL)
    print_success_request()
    result = os.popen(URL).read()

    print()
    print(result)


else:
    start, end = int(sys.argv[2]), int(sys.argv[3]) + 1

    print("##########     ########      #######    ########")
    print("##       ##   ##      ##    ###            ##   ")
    print("##       ##   ##      ##    ###            ##   ")
    print("##      ###   ##      ##     ######        ##   ")
    print("##########    ##      ##         ###       ##   ")
    print("##            ##      ##         ###       ##   ")
    print("##            ##      ##          ##       ##   ")
    print("##             ########      #######       ##   ")

    for i in range(start, end):
        PREFIX = "http --form POST http://127.0.0.1:8000/post/ "
        DATA = 'title="Post Test Title{}" body="Post Test Body{}"'
        URL = PREFIX + DATA.format(i, i)

        print_request_message(URL)
        print_success_request()
        result = os.popen(URL).read()

        print()
        print(result)


print()
print("#############################################")
print("################ END SCRIPT  ################")
print("#############################################")
