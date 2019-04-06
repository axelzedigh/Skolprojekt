#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROWS 9
#define COLS 8
#define TECKEN 'X'
#define ANTAL 5

_Bool c = 0;
char forvantat[20];

void finnRad(char **field, int antal, char tecken);
void finnKol(char **field, int antal, char tecken);
void finnDia(char **field, int antal, char tecken);

int main(int argc, char* argv[]) {
	///////////////////////////////////////////////////////
    // Öppna fil
    FILE * fil = fopen("testdata.txt", "r");
    int strSize, readSize;
    char *buffer;
    // Ta reda på storleken och återgå sen till start
    fseek(fil, 0, SEEK_END);
    strSize = ftell(fil);
    rewind(fil);
    // Skapa dynamiskt minne för filens innehåll
    buffer = calloc(sizeof(char), strSize+1);
    // Läs in filens innehåll och spara antaler inlästa tecken 
    //i "readSize"
    readSize = fread(buffer, sizeof(char), strSize, fil);
    
    fclose(fil);
    ///////////////////////////////////////////////////////
    // Skriv ut lite tjafs
    printf("\n");
    printf("Läser in matris från filen 'testdata.txt'\n");
    printf("\n");
    printf("%s\n", buffer);
    printf("\n");
	printf("Testar om det finns %d i rad av %c.\n", ANTAL, TECKEN);
	printf("Förväntat resultat: ");
	fgets(forvantat, sizeof(forvantat), stdin);
	printf("\n");
	printf("Börjar testen\n");
	printf("\n");

    rewind(fil);
	///////////////////////////////////////////////////////
	//Skapa matris
    int tal = 0;
	char ** matris =  malloc( sizeof(char *) * ROWS);
	for (int i = 0; i < ROWS; i++) {
		matris[i] =  malloc( sizeof( char  ) * COLS);
        for (int j = 0; j < COLS; ) {
			if ((strcmp(&buffer[tal], " ")) || (strcmp(&buffer[tal],"\n")) || (strcmp(&buffer[tal],"#"))) {
        		matris[i][j] = buffer[tal];
            	j++;
            	tal++;
        	}
        	++tal;
    	}
    }
    fclose(fil);
    ///////////////////////////////////////////////////////
    //Utför tester
    finnRad(matris, ANTAL, TECKEN);
    finnKol(matris, ANTAL, TECKEN);
    finnDia(matris, ANTAL, TECKEN);
    printf("\n");
    //////////////////////////////////////////////////////
    //Skriv ut resultat
    if (c == 1){
    	printf("Reslutat: Positivt");
    	printf("\n");
    }
    else {
    	printf("Resultat: Negativt");
    	printf("\n");
    }
    ///////////////////////////////////////////////////////
    // Städa lite
    free(matris);
    free(buffer);
    printf("\n");
    return 0;
}
void finnRad(char **field, int antal, char tecken) {
	//Finn antal tecken i vågrät:
    int count = 0;
	for (int i = 0; i < ROWS; i++) {
		count = 0;
		for (int j = 0; j < COLS; j++) {
			if ((char)field[i][j] == (char)tecken) {
				count = count +1;
			}
			else {
				count = 0;
			}
			if (count == (int)antal) {
				printf("\t%d i rad vågrät i rad %d\n", antal, i+1);
				c = 1;
				return;
			}
		}
    }
    printf("\tInga %d i rad vågrät\n", antal);
    return;
}
void finnKol(char **field, int antal, char tecken) {
	//Finn antal tecken i lodrät:
    int count = 0;
    for (int i = 0; i < COLS; i++) {
    	count = 0;
    	for (int j = 0; j < ROWS; j++) {
    		if ((char)field[j][i] == (char)tecken) {
				count++;
    		}
			else {
				count = 0;
			}
			if (count == (int)antal) {
				printf("\t%d i rad lodrät i kolumn %d\n", antal, i+1);
				c = 1;
				return;
			}
    	}
    }
    printf("\tInga %d i rad lodrät\n", antal);
    return;
}
void finnDia(char **field, int antal, char tecken) {
	int count = 0;
	int x;
	int y;
	// Sydväst-diagonaler
	for (int i = 0; i < ROWS; i++) {
    	count = 0;
    	for (int j = 0; j < COLS; j++) {
    		x = i;
    		y = j;
    		count = 0;
    		while ((x >= 0) && (x < ROWS) && (y >= 0) && (y<COLS)) {
    			if ((char)field[x][y] == (char)tecken) {
					count++;
    			}
				else {
					count = 0;
				}
				if (count == (int)antal) {
					printf("\t%d i rad i diagonal\n", antal);
					c = 1;
					return;
				}
				++x;
				--y;
			}
    	}
    }
    // Sydöst-diagonaler
    for (int i = 0; i < ROWS; i++) {
    	count = 0;
    	for (int j = COLS-1; 0 <= j; j--) {
    		x = i;
    		y = j;
    		count = 0;
    		while ((x >= 0) && (x < ROWS) && (y >= 0) && (y<COLS)) {
    			if ((char)field[x][y] == (char)tecken) {
					count++;
    			}
				else {
					count = 0;
				}
				if (count == (int)antal) {
					printf("\t%d i rad i diagonal\n", antal);
					c = 1;
					return;
				}
				++x;
				++y;
			}
    	}
    }
    printf("\tInga %d i rad diagonal\n", antal);
    return;
}
