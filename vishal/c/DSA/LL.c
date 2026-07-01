#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};  
int main(){
    struct node *head=NULL,*temp=NULL,*newnode=NULL;
    for(int i=0;i<5;i++){
        newnode=(struct node*)malloc(sizeof(struct node));
        printf("Enter the data: ");
        scanf("%d",&newnode->data);
        newnode->next=NULL;
        if(head==NULL){
            head=temp=newnode;
        }
        else{
            temp->next=newnode;
            temp=newnode;
        }
    }
    temp=head;
    printf("The linked list is: ");
    while(temp!=NULL){
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n");
    return 0;
}