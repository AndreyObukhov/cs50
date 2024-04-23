#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    typedef uint8_t BYTE;
    BYTE buffer[512];

    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    };
    FILE *CARD = fopen(argv[1], "r");

    if (CARD == NULL)
    {
        printf("Forensic image cannot be opened for reading\n");
        return 1;
    };

    //Initializes variables for the loop.
    int N = 0;
    char filename[8];
    FILE *img = NULL;

    //Read input file by block of size 512 B.
    while (fread(buffer, sizeof(BYTE), 512, CARD) == 512)
    {
        //Checks if the new jpg is starting.
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            //Closes last opened img if this is not fisrt in a row.
            if (N > 0)
            {
                fclose(img);
            }
            //Makes a name for new jpg.
            sprintf(filename, "%03i.jpg", N);
            img = fopen(filename, "w");
            //Increases overal number of jpgs.
            N++;
        };
        if (img != NULL)
        {
            //Writes to current output file
            fwrite(buffer, sizeof(BYTE), 512, img);
        };
    };
    //Closes remaining files.
    fclose(img);
    fclose(CARD);
    return 0;
}