import requests
import pandas as pd
import random
import texter
from PIL import Image

def main():
    #'~/Documents/CalvinAndHobbes/CHid.csv'
    #'CHid.csv'
    df = pd.read_csv(r'~/Documents/CalvinAndHobbes/CHid.csv')

    i = random.randint(0, 3696)
    id = str(df.iloc[i].item())

    url = 'https://picayune.uclick.com/comics/ch/19' + id[2:4] + '/ch' + id[2:] + '.gif'
    img = requests.get(url)

    with open("comic.gif",'wb') as f:
        f.write(img.content)

    
    #Converts gif to png so it displays in iMessage
    gif='comic.gif'
    img = Image.open(gif)
    img.save("comic.png",'png', optimize=True, quality=70)

    #Sends texts to all willing (or unwilling) participants
    texter.sendText('6128605585@vzwpix.com', 'comic.png')
    #texter.sendText('6122809032@vzwpix.com', 'comic.png')


if __name__ == '__main__':    
    main()
    
