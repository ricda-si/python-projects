#include <stdio.h>

void    psswd_gen(int qtd, int len)
{
    char psswd_list[] = "abcdefghijklmno";
    int i = 0;

    while (psswd_list[i])
    {
        printf("%c", psswd_list[i]);
        i++;
    }
    printf("\n");

    if (len < 5)
        printf("Too short !");
    else if (qtd < 5)
        printf("Too small !");
    else
        printf("OK !");
}

void    menu()
{
    int psswd_qtd = 0;
    int psswd_len = 0;

    // header
    printf("=========================\n");
    printf("=   Password Generator  =\n");
    printf("=========================\n");

    // options
    while (1)
    {
        printf("Qtd: ");
        scanf("%d", &psswd_qtd);

        printf("Len: ");
        scanf("%d", &psswd_len);
        break;
    }

    // call psswd_gen function
    psswd_gen(psswd_qtd, psswd_len);
}

int main()
{
    menu();
    return (0);
}
