#include<stdio.h>
int main(){
    char str1[100],str2[20][200];
    printf("Enter the string: ");
    fgets(str1,100,stdin);
    int i=0,j=0,k=0;
    while(str1[i]!='\0' ){
        if(str1[i]==' ' && str1[i]!='\n'){
            str2[j][k]='\0';
            j++;
            k=0;
        }
        else{
            str2[j][k]=str1[i];
            k++;
        }
        i++;
    }
    str2[j][k]='\0'; // Null-terminate the last string

    for(int m=0;m<=j;m++){
        printf("%s\n",str2[m]);
    }   
return 0;
}