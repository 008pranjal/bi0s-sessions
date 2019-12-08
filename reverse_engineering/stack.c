#include<stdio.h>
int size,top=-1,stack[100],size;
void push();
void pop();
void display();	

int main(){
    int op; 
	
	printf("Enter the size of Stack: ");
	scanf("%d",&size);

	printf("push()\t pop()\t print()\t exit()");

      do
    {      
        printf("\nEnter the Choice:");
        scanf("%d",&op);
        switch(op)
        {
            case 1:
            {
                push();
                break;
            }
            case 2:
            {
                pop();
                break;
            }
            case 3:
            {
                display();
                break;
            }
            case 4:
            {
                printf("\nExiting");
                break;
            }
            default:
            {
                printf ("\nINVALID!!!");
            }
                 
        }
    }
    while(op!=4);
return 0;
}

void push()
{   int x;
    if(top>=size-1)
    {
        printf("\nStack overflow!!!");
         
    }
    else
    {
        printf("Value: ");
        scanf("%d",&x);
        
        top++;
        printf("%d",top);
        stack[top]=x;
    }
}
void pop()
{
    if(top == -1)
    {
        printf("Stack underflow!!!");
    }
    else
    {
        top--;
    }
}
void display()
{
    if(top>=0)
    {
        
        for(int i=top; i>=0; i--)
            printf("<--- %d",stack[i]);
        
    }
    else
    {
        printf("\nempty");
    }
    
}	


