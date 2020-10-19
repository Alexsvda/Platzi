#include "stdlib.h"
#include "stdio.h"
#include "string.h"

struct client
{
    char Name    [50];
    char Id      [10];
    float Credit     ;
    char Adress [100];
};
int main(int argc, char const *argv[])
{
    struct client client1 = {0};
    strcpy (client1.Name, "Camilo Valencia");
    strcpy (client1.Id, "000000001");
    client1.Credit=10000000;
    strcpy (client1.Adress, "Calle 1 , carreara 1 , stgo");
    printf ("The client name is : %s", client1.Name);
    printf ("The client ID is : %s", client1.Id);
    printf ("The client Credit is : %d", client1.Credit);
    printf ("The client Adress is : %s", client1.Adress);

    return 0;
}


