def timeConversion(s):
    hour=(int(s[0:2]))
    minute=(s[3:5])
    sec=(s[6:8])
    upper=s[8:10].upper()
    if(upper=="PM"):
        if(hour==12):
            return s[0:8]
        pmhour=12+hour
        newtime=str(pmhour)+":"+minute+":"+sec
        return newtime
    else:
        if(hour==12):
            newtimes="00"+":"+minute+":"+sec
            return newtimes
        newtimes=s[0:8]
        return newtimes
s="07:05:45am"
result=timeConversion(s)
print(result)