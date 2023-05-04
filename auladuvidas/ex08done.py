# Transforma segundos em anos, dias, horas, minutos e segundos e retorna uma string com o resultado
# Exemplo: 3662 -> "1 hour, 1 minute and 2 seconds"
# Exemplo: 15731080 -> "182 days, 1 hour, 44 minutes and 40 seconds"

def format_duration(seconds):
    if seconds == 0:
        return "now"
    y= seconds // (60*60*24*365)
    yr= seconds % (60*60*24*365)
    d= yr // (60*60*24)
    dr= yr % (60*60*24)
    h= dr // (60*60)
    hr= dr % (60*60)
    m= hr // (60)
    mr= hr % (60)
    s= mr % (60)
    final= []
    if y!=0:
        final.append(str(y)+(" year")+("s" if y > 1 else ""))
    if d!=0:
        final.append(str(d)+(" day")+("s" if d > 1 else ""))
    if h!=0:
        final.append(str(h)+(" hour")+("s" if h > 1 else ""))
    if m!=0:
        final.append(str(m)+(" minute")+("s" if m > 1 else ""))
    if s!=0:
        final.append(str(s)+(" second")+("s" if s > 1 else ""))
    return ", ".join(final[:-1]) + (" and " if len(final) > 1 else "") + final[-1]


def main():
    assert(format_duration(1) == "1 second")
    assert(format_duration(62) == "1 minute and 2 seconds")
    assert(format_duration(120) == "2 minutes")
    assert(format_duration(3600) == "1 hour")
    assert(format_duration(3662) == "1 hour, 1 minute and 2 seconds")
    assert(format_duration(15731080) == "182 days, 1 hour, 44 minutes and 40 seconds")
    assert(format_duration(132030240) == "4 years, 68 days, 3 hours and 4 minutes")
    assert(format_duration(205851834) == "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
    assert(format_duration(253374061) == "8 years, 12 days, 13 hours, 41 minutes and 1 second")
    assert(format_duration(242062374) == "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
    assert(format_duration(101956166) == "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
    assert(format_duration(33243586) == "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")
    assert(format_duration(0) == "now")
    print("All tests passed!")

if __name__ == "__main__":
    main()