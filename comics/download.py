import requests
import pandas as pd
import random
from PIL import Image
import os



def main():
    #'~/Documents/CalvinAndHobbes/CHid.csv'
    #'CHid.csv'
    #df = pd.read_csv(r'~/Documents/CalvinAndHobbes/CHid.csv')
    df = pd.read_csv(r'CHid.csv')

    for i in range(0, 3697):
        #finished 2865
        #i = random.randint(0, 3696)
        
        id = str(df.iloc[i].item())
        date = id[2:4] + '/ch' + id[2:]

        print(f'Currently downloading #{i} out of 3696. ID: {id}')

        if os.path.exists(f'comics/gifs/{id}.gif'):
            print('continuing\n\n\n\n...,')
            continue

        

        url = 'https://picayune.uclick.com/comics/ch/19' + id[2:4] + '/ch' + id[2:] + '.gif'
        img = requests.get(url)

        

        with open(f'comics/gifs/{id}.gif','xb') as f:
            f.write(img.content)
            

        
        #Converts gif to png instead (creates a second file)
        gif=f'comics/gifs/{id}.gif'
        img = Image.open(gif)
        img.save(f'comics/pngs/{id}.png','png', optimize=True, quality=100)




if __name__ == '__main__':    
    main()
    