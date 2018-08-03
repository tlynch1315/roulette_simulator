import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def pandas2image(axes, value, df):
    if len(axes) == 2:
        xaxis_name = axes[0]
        yaxis_name = axes[1]
        xaxis = df[xaxis_name].unique()
        yaxis = df[yaxis_name].unique()

        pixel_array = np.zeros([len(xaxis), len(yaxis)])
        #print np.shape(pixel_array)
        df = df.set_index([xaxis_name, yaxis_name])
        #print df
        for i1, x in enumerate(xaxis):
            for i2, y in enumerate(yaxis):
                try:
                    val = df.loc[x,y][value]
                    pixel_array[i1][i2] = val



                except KeyError:
                    val = np.nan
                    pixel_array[i1][i2] = val

        return pixel_array, xaxis, yaxis
    elif len(axes) == 3:
        print "not ready yet"


if __name__ == "__main__":
    data = pd.read_csv("results.csv")
    tommysucks = pandas2image(("stack", "starting_bet"),"net", data)
    plt.imshow(tommysucks[0], cmap='hot')
    #plt.axis([tommysucks[1][0], tommysucks[1][-1], tommysucks[2][0], tommysucks[2][-1]])
    plt.show()
    #print data["net"].values
