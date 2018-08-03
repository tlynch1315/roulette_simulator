import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cmx
import matplotlib
from matplotlib.colors import Normalize


def pandasprocessing(axes, value,df, limiter=None):
    if limiter != None:
        df = df.loc[df[limiter[0]] == limiter[1]]
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
        colorarray = np.zeros([0], dtype="int")
        xarray = np.zeros([1])
        yarray = np.zeros([1])
        zarray = np.zeros([1])
        #print np.shape(pixel_array)
        df = df.set_index([xaxis_name, yaxis_name, zaxis_name])

        #print df
        for i1, x in enumerate(xaxis):
            for i2, y in enumerate(yaxis):
                for i3, z in enumerate(zaxis):
                    try:
                        val = df.loc[x,y,z][value]
                        if isinstance(val, pd.Series):
                            colorarray = np.append(colorarray, int(val.mean()))
                            xarray = np.append(xarray, x)
                            yarray = np.append(yarray, y)
                            zarray = np.append(zarray, z)
                        else:
                            colorarray = np.append(colorarray, int(val))
                            xarray = np.append(xarray, x)
                            yarray = np.append(yarray, y)
                            zarray = np.append(zarray, z)
                    except KeyError:
                        pass

        return {"color" : colorarray,
                "xaxis": xarray,
                "yaxis": yarray,
                "zaxis": zarray,
                "x_name": xaxis_name,
                "y_name": yaxis_name,
                "z_name": zaxis_name}
        print "not ready yet"

def produceimage(tommysucks, dim="2D"):
    if dim == "2D":
        class MidPointNormalize(Normalize):
            def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
                self.midpoint = midpoint
                Normalize.__init__(self, vmin, vmax, clip)

            def __call__(self, value, clip=None):
                # I'm ignoring masked values and all kinds of edge cases to make a
                # simple example...
                x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
                return np.ma.masked_array(np.interp(value, x, y))
        norm = MidPointNormalize(midpoint = 0)
        print tommysucks
        plt.imshow(tommysucks['data'],interpolation="none", cmap='seismic', norm=norm,extent=[np.min(tommysucks['xaxis']), np.max(tommysucks['xaxis']), np.min(tommysucks['yaxis']), np.max(tommysucks['yaxis'])], aspect='auto')
        plt.xlabel(tommysucks['x_name'])
        plt.ylabel(tommysucks['y_name'])
        plt.colorbar()
        plt.show()
    elif dim == "3D":
        class MidPointNormalize(Normalize):
            def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
                self.midpoint = midpoint
                Normalize.__init__(self, vmin, vmax, clip)

            def __call__(self, value, clip=None):
                # I'm ignoring masked values and all kinds of edge cases to make a
                # simple example...
                x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
                return np.ma.masked_array(np.interp(value, x, y))
        fig = plt.figure()
        ax3D = fig.add_subplot(111, projection='3d')
        cm = plt.get_cmap('viridis')
        #cNorm = MidPointNormalize(vmin=min(tommysucks['color']), vmax=max(tommysucks['color']), midpoint=250)
        cNorm = matplotlib.colors.Normalize(vmin=min(tommysucks['color']), vmax=max(tommysucks['color']))

        scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
        ax3D.scatter(tommysucks['xaxis'], tommysucks['yaxis'], tommysucks['zaxis'], c=scalarMap.to_rgba(tommysucks['color']), marker='o')
        ax3D.set_xlabel(tommysucks['x_name'])
        ax3D.set_ylabel(tommysucks['y_name'])
        ax3D.set_zlabel(tommysucks['z_name'])
        scalarMap.set_array(tommysucks['color'])
        fig.colorbar(scalarMap)
        plt.show()

if __name__ == "__main__":
    data = pd.read_csv("results.csv")
    #tommysucks = pandasprocessing(("stack", "starting_bet", "win_rate"),"goal", df=data)
    tommysucks = pandasprocessing(("stack", "starting_bet"),"net", df=data)

    produceimage(tommysucks, dim="2D")
