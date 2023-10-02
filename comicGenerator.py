import requests
import pandas as pd
import random
import texter
from PIL import Image

def getDate(date):
    day = int(date[6:])
    month = int(date[4:6]) - 1
    year = date[:4]
    i = day % 10
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')
    if (day > 10 and day < 20):
        suffix = "th"
    else:
        match i:
            case 1:
                suffix = "st"
            case 2:
                suffix = "nd"
            case 3:
                suffix = "rd"
            case _:
                suffix = "th"

        
    return months[month] + ' ' + str(day) + suffix + ', ' + year

def main():
    #'~/Documents/CalvinAndHobbes/CHid.csv'
    #'CHid.csv'
    df = pd.read_csv(r'~/Documents/CalvinAndHobbes/CHid.csv')
    #df = pd.read_csv(r'CHid.csv')

    i = random.randint(0, 3696)
    id = str(df.iloc[i].item())

    url = 'https://picayune.uclick.com/comics/ch/19' + id[2:4] + '/ch' + id[2:] + '.gif'
    img = requests.get(url)

    with open('comic.gif','wb') as f:
        f.write(img.content)

    
    #Converts gif to png so it displays in iMessage
    gif='comic.gif'
    img = Image.open(gif)
    img.save('comic.png','png', optimize=True, quality=70)

    #Sends texts to all willing (or unwilling) participants
    #For verizon, @vzwpix.com

    #texter.sendText('[PHONE_NUMBER]@[CARRIER_ADDRESS]', 'comic.png', getDate(id))


if __name__ == '__main__':    
    main()
    
