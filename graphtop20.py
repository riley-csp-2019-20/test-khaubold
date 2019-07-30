import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def graph_pair(image1path, image2path, sourceFolder, destFolder, similarityScore):
    #plot one pair of images 

    fig, ax = plt.subplots(1,2)

    #get file path 1
    im1 = os.path.join(sourceFolder, image1path)
    #open image 1 as array?
    ax[0].plot(plt.imread(im1))

    #get file path 2
    im2 = os.path.join(sourceFolder, image2path)
    #open image 2 as array?
    ax[1].plot(plt.imread(im2))


    #figure with two subplots
    #plot image 1
    #plot image 2
    #title with image names
    ax[0].title(image1path)
    ax[1].title(image2path)

    #add similarity score

    #append the plot to a file
    fig.savefig(os.path.join(destFolder, 'test.png'))




    plt.close(fig)


def graph_20(listOfPairs):
    #run graph pair 20 times and save the file



def graph_all(textFile):
    #run graph_20 multiple times, breaking at each \n for a new file





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Match Extracted Features')
    parser.add_argument('-list', '-l', help='List of image pairs and similarity scores.') 
    parser.add_argument('-output', '-o', help='Folder to save the files in.') 
    parser.add_argument('-source', '-s', help='Source folder where images are stored.')

    args = parser.parse_args()
