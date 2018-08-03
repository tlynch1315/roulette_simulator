import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def pandas2image(axes, value,df, limiters=None):

    if limiters != None:
        df = df.loc[df[limiters[0]] == limiters[1]]
    else:
        pass

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
                    try:
                        pixel_array[i1][i2] = val
                    except ValueError:
                        pixel_array[i1][i2] = val.mean()
                except KeyError:
                    val = np.nan
                    pixel_array[i1][i2] = val

        return {"data" : pixel_array,
                "xaxis": xaxis,
                "yaxis": yaxis,
                "x_name": xaxis_name,
                "y_name": yaxis_name}
    elif len(axes) == 3:
        xaxis_name = axes[0]
        yaxis_name = axes[1]
        zaxis_name = axes[2]
        xaxis = df[xaxis_name].unique()
        yaxis = df[yaxis_name].unique()
        zaxis = df[zaxis_name].unique()
        pixel_array = np.zeros([len(xaxis), len(yaxis), len(zaxis)])

        #print np.shape(pixel_array)
        df = df.set_index([xaxis_name, yaxis_name, zaxis_name])
        #print df
        for i1, x in enumerate(xaxis):
            for i2, y in enumerate(yaxis):
                for i3, z in enumerate(zaxis):
                    try:
                        val = df.loc[x,y,z][value]
                        try:
                            pixel_array[i1][i2] = val
                        except ValueError:
                            pixel_array[i1][i2] = val.mean()
                    except KeyError:
                        val = np.nan
                        pixel_array[i1][i2] = val

        return {"data" : pixel_array,
                "xaxis": xaxis,
                "yaxis": yaxis,
                "zaxis": zaxis,
                "x_name": xaxis_name,
                "y_name": yaxis_name,
                "z_name": zaxis_name}
        print "not ready yet"


if __name__ == "__main__":
    data = pd.read_csv("results.csv")
    tommysucks = pandas2image(("stack", "starting_bet"),"net",limiters=("num_simulations", 100), df=data)
    plt.imshow(tommysucks['data'],interpolation="none", extent=[np.min(tommysucks['xaxis']), np.max(tommysucks['xaxis']), np.min(tommysucks['yaxis']), np.max(tommysucks['yaxis'])], aspect='auto')
    plt.xlabel(tommysucks['x_name'])
    plt.ylabel(tommysucks['y_name'])

    plt.colorbar()
    #plt.axis([tommysucks[1][0], tommysucks[1][-1], tommysucks[2][0], tommysucks[2][-1]])

    plt.show()
    #print data["net"].values
