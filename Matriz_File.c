#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define FILAS_MATRIZ_A 3
#define COLUMNAS_MATRIZ_A 3
#define FILAS_MATRIZ_B 3
#define COLUMNAS_MATRIZ_B 3
#define FILAS_MATRIZ_C 3
#define COLUMNAS_MATRIZ_C 3


int main(int argc, char **argv) {
    //printf("Parametro: %s ",argv[1]);
    int fail;
    float pi = 3.1416
    char linea[1024];
    FILE *fich;
    float matrizA[FILAS_MATRIZ_A][COLUMNAS_MATRIZ_A];
    float matrizB[COLUMNAS_MATRIZ_B][COLUMNAS_MATRIZ_B];
    float matrizC[COLUMNAS_MATRIZ_C][COLUMNAS_MATRIZ_C];
    /*Seccion para leer el archivo y pasar los datos a un matriz de 3x3*/
    fich = fopen(argv[1], "r");
    //fich = fopen("test.txt", "r");
    //fich = fopen("test_pos.txt", "r");
    //fich = fopen("test_neg.txt", "r");
    //fich = fopen("test_float.txt", "r");
    //fich = fopen("test_char.txt", "r");
    int f = 0;
    int c = 0;
    while(fgets(linea, 1024, (FILE*) fich)) {
        int n = strlen(linea);
        if (linea[n-1] != '\n') {
        printf ("Sin fin de linea \n");
        }
        else{
        char * token = strtok(linea, ";");
          while( token != NULL ) {
            float data = atoi(token);
            matrizA[f][c] = data;
            matrizB[f][c] = data;
            token = strtok(NULL, ";");
          c++;
          }
          c=0;
          
        }
    f++;
    }
    f=0;
    fclose(fich);
    /*Fin de lectira del archivo*/

    /*Multiplicacion de la matriz por si misma  matrizA * matrizB*/
    for (int a = 0; a < COLUMNAS_MATRIZ_B; a++) {
        // Dentro recorremos las filas de la primera (A)
        for (int i = 0; i < FILAS_MATRIZ_A; i++) {
            float suma = 0;
            // Y cada columna de la primera (A)
            for (int j = 0; j < COLUMNAS_MATRIZ_A; j++) {
                // Multiplicamos y sumamos resultado
                suma += matrizA[i][j] * matrizB[j][a];
            }
            // Lo acomodamos dentro del matrizC
            matrizC[i][a] = suma;
        }
    }

    printf("********Matriz 3x3 Origen***************");
    for(int x=0;x<FILAS_MATRIZ_A;x++){
        for(int y=0;y<COLUMNAS_MATRIZ_A;y++){
           printf(" %f  ",matrizA[x][y]);
        }
        
    }
    
    printf("********Matriz 3x3 Multiplicada*********");
    for(int x=0;x<FILAS_MATRIZ_C;x++){
        for(int y=0;y<COLUMNAS_MATRIZ_C;y++){
           printf(" %f  ",matrizC[x][y]);
        }
        
    }
    printf("********Matriz 3x3 Num_Positivo*********");


return 0;
}
