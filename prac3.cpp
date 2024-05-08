#include <iostream>
using namespace std;

class TREE_CLASS
{
private:
    struct bin
    {
        char data[50];
        struct bin *left;
        struct bin *right;
    };

public:
    bin *New, *root;
    TREE_CLASS();
    void create();
    void insert(bin *, bin *);
    void rec_inorder(bin *);
    void printLevelOrder(bin *root);
    void printLevel(bin *root, int level);
    int height(bin *node);
};

TREE_CLASS::TREE_CLASS()
{
    root = NULL;
}

void TREE_CLASS::create()
{
    char ans = 'y';
    do
    {
        New = new bin;
        cout << "\n Enter The Book/Chapter/Section: ";
        cin >> New->data;
        New->left = NULL;
        New->right = NULL;
        if (root == NULL)
            root = New;
        else
            insert(root, New);
        cout << "\n Do You want To Enter More Chapter/Section?(y/n): ";
        cin >> ans;
    } while (ans == 'y' || ans == 'Y');
}

void TREE_CLASS::insert(bin *root, bin *New)
{
    char ch;
    cout << "\n Where to insert left(l)/right(r) of " << root->data << " : ";
    cin >> ch;
    if ((ch == 'r') || (ch == 'R'))
    {
        if (root->right == NULL)
        {
            root->right = New;
        }
        else
            insert(root->right, New);
    }
    else
    {
        if (root->left == NULL)
        {
            root->left = New;
        }
        else
            insert(root->left, New);
    }
}

void TREE_CLASS::rec_inorder(bin *root)
{
    if (root != NULL)
    {
        rec_inorder(root->left);
        cout << " " << root->data;
        rec_inorder(root->right);
    }
}

void TREE_CLASS::printLevelOrder(bin *root)
{
    int h = height(root);
    int i;
    for (i = 1; i <= h; i++)
    {
        cout << "\n";
        printLevel(root, i);
    }
}

void TREE_CLASS::printLevel(bin *root, int level)
{
    if (root == NULL)
        return;
    if (level == 1)
        cout << " " << root->data;
    else if (level > 1)
    {
        printLevel(root->left, level - 1);
        printLevel(root->right, level - 1);
    }
}

int TREE_CLASS::height(bin *node)
{
    if (node == NULL)
        return 0;
    else
    {
        int lheight = height(node->left);
        int rheight = height(node->right);
        if (lheight > rheight)
            return (lheight + 1);
        else
            return (rheight + 1);
    }
}

int main()
{
    int choice;
    TREE_CLASS obj;
    do
    {
        cout << "\n\t\tMain Menu";
        cout << "\n 1.Create";
        cout << "\n 2.Display";
        cout << "\n 3.Exit";
        cout << "\n\t Enter Your Choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            obj.create();
            break;
        case 2:
            if (obj.root == NULL)
                cout << "Tree Is not Created!";
            else
                obj.printLevelOrder(obj.root);
            break;
        }
    } while (choice <= 2);
    return 0;
}



                Main Menu
 1.Create
 2.Display
 3.Exit
//          Enter Your Choice: 1

//  Enter The Book/Chapter/Section: book

//  Do You want To Enter More Chapter/Section?(y/n): y

//  Enter The Book/Chapter/Section: chapter1

//  Where to insert left(l)/right(r) of book : l

//  Do You want To Enter More Chapter/Section?(y/n): y

//  Enter The Book/Chapter/Section: chapter2

//  Where to insert left(l)/right(r) of book : r

//  Do You want To Enter More Chapter/Section?(y/n): y

//  Enter The Book/Chapter/Section: section1.1

//  Where to insert left(l)/right(r) of book : l

//  Where to insert left(l)/right(r) of chapter1 : l

//  Do You want To Enter More Chapter/Section?(y/n): y

//  Enter The Book/Chapter/Section: section1.2

//  Where to insert left(l)/right(r) of book : l

//  Where to insert left(l)/right(r) of chapter1 : r

//  Do You want To Enter More Chapter/Section?(y/n): y

//  Enter The Book/Chapter/Section: section2.1

//  Where to insert left(l)/right(r) of book : r

//  Where to insert left(l)/right(r) of chapter2 : l

//  Do You want To Enter More Chapter/Section?(y/n): y

//  Enter The Book/Chapter/Section: section2.2

//  Where to insert left(l)/right(r) of book : r

//  Where to insert left(l)/right(r) of chapter2 : r

//  Do You want To Enter More Chapter/Section?(y/n): n

//                 Main Menu
//  1.Create
//  2.Display
//  3.Exit
//          Enter Your Choice: 2

//  book
//  chapter1 chapter2
//  section1.1 section1.2 section2.1 section2.2
//                 Main Menu
//  1.Create
//  2.Display
//  3.Exit
//          Enter Your Choice: 3
