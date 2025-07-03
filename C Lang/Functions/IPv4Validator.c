#include <stdio.h>

int printIP(char * ptr, int valid)
{
   if (valid == 1)
   {
      printf("%s is a valid IPv4 address\n", ptr);
      return 0;
   }
   else
   {
      printf("%s is not a valid IPv4 Address\n", ptr);
      return 1;
   }
}
int isValid(char ptr[])
{
   int oct1, oct2, oct3, oct4; char extra;
   int result = sscanf(ptr, "%d.%d.%d.%d%c", &oct1, &oct2, &oct3, &oct4, &extra);
   //printf("oct1: %d, oct2: %d, oct3: %d, oct4: %d\n", oct1, oct2, oct3, oct4);
   //printf("%d", result);
   if (result == 4)
   {
      if ((oct1 >= 0 && oct1 <= 255) && (oct2 >= 0 && oct2 <= 255) && (oct3 >= 0 && oct3 <= 255) && (oct4 >=0 && oct4 <= 255))
      {
         printIP(ptr, 1);
      }
      else
      {
         printIP(ptr, 0);
      }
   }
   else
      printIP(ptr, 0);
   return 0;
}

int main(void)
{
   char ipv4[16];
   printf("Enter The IPv4 Address: ");
   scanf("%s", ipv4);
   //printf("%s", ipv4);
   isValid(ipv4);
   return 0;
}
