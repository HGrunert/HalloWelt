addr = "http://lollerz.google.org"
isWebaddr = addr.endswith((".com",".de",".net",".org"))
isSecure = addr.startswith("https")
if(isWebaddr):
    if(isSecure):
        print("Connecting.")
    else:
        print("Warning! Not a secure connection!")
        if(input("Do you want to connect anyway?")=="y"):
            print("Reluctantly connecting.")