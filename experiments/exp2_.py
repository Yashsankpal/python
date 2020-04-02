def date(s):
    if s.find("AM")>=0:
        s=s.replace("AM","")
    elif s.find("PM")>=0:
        s=s.replace("PM","")
    s=s.split(":")
    if s[0] == "12":
        s[0]="00"
    else:
        s[0]=str(int(s[0])+12)

    s=":".join(s)    
    print(s)


date("07:09:45PM")