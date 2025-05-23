
#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *left;
    struct node *right;
};
typedef struct node *NODE;

NODE create_node(int item)
{
    NODE temp;
    temp=(NODE)malloc(sizeof(struct node));
    temp->data=item;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
}

NODE Insertbst(NODE root,int item)
{
    NODE temp;
    temp=create_node(item);
    if(root==NULL)
        return temp;
    else
    {
       if(item < root->data)
            root->left=Insertbst(root->left,item);
        else
            root->right=Insertbst(root->right,item);
    }
    return root;

}

void preorder(NODE root)
{
    if(root!=NULL)
    {
        printf("%d\t",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void inorder(NODE root)
{
    if(root!=NULL)
    {
        inorder(root->left);
        printf("%d\t",root->data);
        inorder(root->right);
    }
}

void postorder(NODE root)
{
    if(root!=NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d\t",root->data);
    }
}


int main()
{
    NODE root = NULL;
    int ch,item;
    for(;;)
    {
        printf("\n 1. Insert");
        printf("\n 2. Preorder");
        printf("\n 3. Inorder");
        printf("\n 4. Postorder");
        printf("\n 5. Exit");
        printf("\n Read ur choice:");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:printf("\n Read element to be inserted :");
                scanf("%d",&item);
                root=Insertbst(root,item);
                break;
            case 2:printf("\n The Preorder traversal is\n");
                 preorder(root);
                 break;
            case 3:printf("\n The Inorder traversal is\n");
                 inorder(root);
                 break;
            case 4:printf("\n The Postorder traversal is\n");
                 postorder(root);
                 break;
            default :exit(0);
        }
    }
    return 0;
}
