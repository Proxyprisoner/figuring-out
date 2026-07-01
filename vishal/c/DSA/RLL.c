#include<stdlib.h>
#include<stdio.h>
struct node{
    int data;
    struct node *next;
};
void *reverse(struct node *head){
    struct node *prev=NULL,*current=head,*next=NULL;
    while(current!=NULL){
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    head=prev;
}
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