#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //image[2][3].rgbtRed = 0;
    //image[2][3].rgbtGreen = 0;
    //image[2][3].rgbtBlue = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = round((double)(image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / (double)3);
            image[i][j].rgbtGreen = image[i][j].rgbtRed;
            image[i][j].rgbtBlue = image[i][j].rgbtRed;
        };
    };
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j <= (width - 1) / 2; j++)
        {
            tmp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = tmp;
        };
    };
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE imageCopy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            imageCopy[i][j] = image[i][j];
        };
    };
    int Red, Green, Blue, NUMBER;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            Red = 0;
            Green = 0;
            Blue = 0;
            NUMBER = 0;
            //We go through all the neighbors, checking whether they are included in the array.
            if (i - 1 >= 0 && i - 1 < height && j - 1 >= 0 && j - 1 < width)
            {
                Red += imageCopy[i - 1][j - 1].rgbtRed;
                Green += imageCopy[i - 1][j - 1].rgbtGreen;
                Blue += imageCopy[i - 1][j - 1].rgbtBlue;
                NUMBER++;
            };
            if (i - 1 >= 0 && i - 1 < height && j >= 0 && j < width)
            {
                Red += imageCopy[i - 1][j].rgbtRed;
                Green += imageCopy[i - 1][j].rgbtGreen;
                Blue += imageCopy[i - 1][j].rgbtBlue;
                NUMBER++;
            };
            if (i - 1 >= 0 && i - 1 < height && j + 1 >= 0 && j + 1 < width)
            {
                Red += imageCopy[i - 1][j + 1].rgbtRed;
                Green += imageCopy[i - 1][j + 1].rgbtGreen;
                Blue += imageCopy[i - 1][j + 1].rgbtBlue;
                NUMBER++;
            };
            if (i >= 0 && i < height && j + 1 >= 0 && j + 1 < width)
            {
                Red += imageCopy[i][j + 1].rgbtRed;
                Green += imageCopy[i][j + 1].rgbtGreen;
                Blue += imageCopy[i][j + 1].rgbtBlue;
                NUMBER++;
            };
            if (i >= 0 && i < height && j - 1 >= 0 && j - 1 < width)
            {
                Red += imageCopy[i][j - 1].rgbtRed;
                Green += imageCopy[i][j - 1].rgbtGreen;
                Blue += imageCopy[i][j - 1].rgbtBlue;
                NUMBER++;
            };
            if (i + 1 >= 0 && i + 1 < height && j - 1 >= 0 && j - 1 < width)
            {
                Red += imageCopy[i + 1][j - 1].rgbtRed;
                Green += imageCopy[i + 1][j - 1].rgbtGreen;
                Blue += imageCopy[i + 1][j - 1].rgbtBlue;
                NUMBER++;
            };
            if (i + 1 >= 0 && i + 1 < height && j >= 0 && j < width)
            {
                Red += imageCopy[i + 1][j].rgbtRed;
                Green += imageCopy[i + 1][j].rgbtGreen;
                Blue += imageCopy[i + 1][j].rgbtBlue;
                NUMBER++;
            };
            if (i + 1 >= 0 && i + 1 < height && j + 1 >= 0 && j + 1 < width)
            {
                Red += imageCopy[i + 1][j + 1].rgbtRed;
                Green += imageCopy[i + 1][j + 1].rgbtGreen;
                Blue += imageCopy[i + 1][j + 1].rgbtBlue;
                NUMBER++;
            };
            Red += imageCopy[i][j].rgbtRed;
            Green += imageCopy[i][j].rgbtGreen;
            Blue += imageCopy[i][j].rgbtBlue;
            NUMBER++;
            image[i][j].rgbtRed = round((double) Red / (double) NUMBER);
            image[i][j].rgbtGreen = round((double) Green / (double) NUMBER);
            image[i][j].rgbtBlue = round((double) Blue / (double) NUMBER);
        };
    };
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE imageCopy[height + 2][width + 2];
    //Making a copy of image array with place for "black frame" at the edges.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            imageCopy[i + 1][j + 1] = image[i][j];
        };
    };
    //Filling edges with black pixels (horizontally).
    for (int j = 0; j < width + 2; j++)
    {
        imageCopy[0][j].rgbtRed = 0;
        imageCopy[0][j].rgbtGreen = 0;
        imageCopy[0][j].rgbtBlue = 0;
        imageCopy[height + 1][j].rgbtRed = 0;
        imageCopy[height + 1][j].rgbtGreen = 0;
        imageCopy[height + 1][j].rgbtBlue = 0;
    };
    //Filling edges with black pixels (vertically).
    for (int i = 1; i < height + 1; i++)
    {
        imageCopy[i][0].rgbtRed = 0;
        imageCopy[i][0].rgbtGreen = 0;
        imageCopy[i][0].rgbtBlue = 0;
        imageCopy[i][width + 1].rgbtRed = 0;
        imageCopy[i][width + 1].rgbtGreen = 0;
        imageCopy[i][width + 1].rgbtBlue = 0;
    };
    int Gx, Gy, G;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //In our model pixel image[i][j] corresponds to pixel imageCopy[i+1][j+1] due to black edges, which was added to the copy.
            /*"Neibourhood matrix" for pixel [i+1][j+1] looks like
            [i]  [j]     [i]  [j+1]     [i]  [j+2]
            [i+1][j]     [i+1][j+1]     [i+1][j+2]
            [i+2][j]     [i+2][j+1]     [i+2][j+2]
            */
            //Computing G for red part.
            Gx = 0;
            Gy = 0;
            G = 0;
            Gx += - 1 * imageCopy[i][j].rgbtRed;
            Gx += - 2 * imageCopy[i + 1][j].rgbtRed;
            Gx += - 1 * imageCopy[i + 2][j].rgbtRed;
            Gx += 1 * imageCopy[i][j + 2].rgbtRed;
            Gx += 2 * imageCopy[i + 1][j + 2].rgbtRed;
            Gx += 1 * imageCopy[i + 2][j + 2].rgbtRed;

            Gy += - 1 * imageCopy[i][j].rgbtRed;
            Gy += - 2 * imageCopy[i][j + 1].rgbtRed;
            Gy += 1 * imageCopy[i + 2][j].rgbtRed;
            Gy += - 1 * imageCopy[i][j + 2].rgbtRed;
            Gy += 2 * imageCopy[i + 2][j + 1].rgbtRed;
            Gy += 1 * imageCopy[i + 2][j + 2].rgbtRed;

            G = (int) round(sqrt(Gx * Gx + Gy * Gy));
            if (G > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = G;
            };

            //Computing G for green part.
            Gx = 0;
            Gy = 0;
            G = 0;
            Gx += - 1 * imageCopy[i][j].rgbtGreen;
            Gx += - 2 * imageCopy[i + 1][j].rgbtGreen;
            Gx += - 1 * imageCopy[i + 2][j].rgbtGreen;
            Gx += 1 * imageCopy[i][j + 2].rgbtGreen;
            Gx += 2 * imageCopy[i + 1][j + 2].rgbtGreen;
            Gx += 1 * imageCopy[i + 2][j + 2].rgbtGreen;

            Gy += - 1 * imageCopy[i][j].rgbtGreen;
            Gy += - 2 * imageCopy[i][j + 1].rgbtGreen;
            Gy += 1 * imageCopy[i + 2][j].rgbtGreen;
            Gy += - 1 * imageCopy[i][j + 2].rgbtGreen;
            Gy += 2 * imageCopy[i + 2][j + 1].rgbtGreen;
            Gy += 1 * imageCopy[i + 2][j + 2].rgbtGreen;

            G = (int) round(sqrt(Gx * Gx + Gy * Gy));
            if (G > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = G;
            };

            //Computing G for blue part.
            Gx = 0;
            Gy = 0;
            G = 0;
            Gx += - 1 * imageCopy[i][j].rgbtBlue;
            Gx += - 2 * imageCopy[i + 1][j].rgbtBlue;
            Gx += - 1 * imageCopy[i + 2][j].rgbtBlue;
            Gx += 1 * imageCopy[i][j + 2].rgbtBlue;
            Gx += 2 * imageCopy[i + 1][j + 2].rgbtBlue;
            Gx += 1 * imageCopy[i + 2][j + 2].rgbtBlue;

            Gy += - 1 * imageCopy[i][j].rgbtBlue;
            Gy += - 2 * imageCopy[i][j + 1].rgbtBlue;
            Gy += 1 * imageCopy[i + 2][j].rgbtBlue;
            Gy += - 1 * imageCopy[i][j + 2].rgbtBlue;
            Gy += 2 * imageCopy[i + 2][j + 1].rgbtBlue;
            Gy += 1 * imageCopy[i + 2][j + 2].rgbtBlue;

            G = (int) round(sqrt(Gx * Gx + Gy * Gy));
            if (G > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = G;
            };
        };
    };
    return;
}
