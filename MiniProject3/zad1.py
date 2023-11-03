def range_days(text):
    days = text.split("-")
    if len(days) != 2:
        return days
    every = ["pn", 'wt', 'sr', 'czw', 'pt', 'sob', 'nd']
    return every[every.index(days[0]):every.index(days[1])+1]


def dates(months, days, *morning):
    counter = 0
    for i in range(len(months)):
        temp = range_days(days[i])
        for j in temp:
            try:
                mor = morning[0][counter]
            except:
                mor = 'r'
            finally:
                print(months[i] + " " + j + " " + mor)
            counter+=1


dates(["styczen", 'luty', 'kwiecien'],["pn-sr",'czw','sob-nd'],["r",'w','w'])
