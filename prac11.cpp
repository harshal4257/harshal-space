#include <iostream>
#include <fstream>
#include <cstring>
#include<string>

using namespace std;

class tel {
public:
    int rollNo, roll1;
    char name[10];
    char div;
    char address[20];

    void accept() {
        cout << "\n\tEnter Roll Number : ";
        cin >> rollNo;
        cout << "\n\tEnter the Name : ";
        cin >> name;
        cout << "\n\tEnter the Division : ";
        cin >> div;
        cout << "\n\tEnter the Address : ";
        cin >> address;
    }

    void accept2() {
        cout << "\n\tEnter the Roll No. to modify : ";
        cin >> rollNo;
    }

    void accept3() {
        cout << "\n\tEnter the name to modify : ";
        cin >> name;
    }

    int getRollNo() {
        return rollNo;
    }

    void show() {
        cout << "\n\t" << rollNo << "\t\t" << name << "\t\t" << div << "\t\t" << address;
    }
};

int main() {
    int ch;
    tel t1;

    fstream g, f;

    do {
        cout << "\n\t------MENU-------";
        cout << "\n1.Insert and overwrite\n2.Show\n3.Search & Edit(number)\n4.Delete a Student Record\n5.Exit\n\tEnter the Choice\t:";
        cin >> ch;
        cin.ignore(); // Clear the input buffer

        switch (ch) {
            case 1:
                f.open("StuRecord.txt", ios::out);
                x:
                t1.accept();
                f.write((char *)&t1, (sizeof(t1)));
                cout << "\nDo you want to enter more records?\n1.Yes\n2.No\n";
                char ans;
                cin >> ans;
                if (ans == 'y'||ans=='Y')
                    goto x;
                else {
                    f.close();
                    break;
                }

            case 2:
                f.open("StuRecord.txt", ios::in);
                while (f.read((char *)&t1, (sizeof(t1)))) {
                    t1.show();
                }
                f.close();
                break;

            case 3:
                int rec;
                cout << "\nEnter the roll number you want to find : ";
                cin >> rec;
                f.open("StuRecord.txt", ios::in | ios::out);
                while (f.read((char *)&t1, (sizeof(t1)))) {
                    if (rec == t1.rollNo) {
                        cout << "\nRecord found";
                        int add = f.tellg();
                        f.seekg(0, ios::beg);
                        int start = f.tellg();
                        int n1 = (add - start) / (sizeof(tel));
                        f.seekp((n1 - 1) * sizeof(tel), ios::beg);
                        t1.accept();
                        f.write((char *)&t1, (sizeof(tel)));
                        f.close();
                        break;
                    }
                }
                if (f.eof()) {
                    cout << "\nRecord not found";
                }
                f.close();
                break;

            case 4:
                int roll;
                cout << "Please Enter the Roll No. of Student Whose Info You Want to Delete: ";
                cin >> roll;
                f.open("StuRecord.txt", ios::in);
                g.open("temp.txt", ios::out);
                f.read((char *)&t1, sizeof(tel));
                while (!f.eof()) {
                    if (t1.getRollNo() != roll)
                        g.write((char *)&t1, sizeof(tel));
                    else
                        cout << "The record with the roll no. " << roll << " has been deleted." << endl;
                    f.read((char *)&t1, sizeof(tel));
                }
                f.close();
                g.close();
                remove("StuRecord.txt");
                rename("temp.txt", "StuRecord.txt");
                break;

            case 5:
                cout << "\n\tThank you";
                break;
        }
    } while (ch != 5);

    return 0;
}



//         ------MENU-------
// 1.Insert and overwrite
// 2.Show
// 3.Search & Edit(number)
// 4.Delete a Student Record
// 5.Exit
//         Enter the Choice        :1

//         Enter Roll Number : 1

//         Enter the Name : a

//         Enter the Division : a

//         Enter the Address : bqqw

// Do you want to enter more records?
// 1.Yes
// 2.No
// y

//         Enter Roll Number : 2 

//         Enter the Name : b

//         Enter the Division : b

//         Enter the Address : kbdkdcc

// Do you want to enter more records?
// 1.Yes
// 2.No
// n

//         ------MENU-------
// 1.Insert and overwrite
// 2.Show
// 3.Search & Edit(number)
// 4.Delete a Student Record
// 5.Exit
//         Enter the Choice        :2

//         1               a               a               bqqw
//         2               b               b               kbdkdcc
//         ------MENU-------
// 1.Insert and overwrite
// 2.Show
// 3.Search & Edit(number)
// 4.Delete a Student Record
// 5.Exit
//         Enter the Choice        :3

// Enter the roll number you want to find : 1

// Record found
//         Enter Roll Number : 1

//         Enter the Name : c

//         Enter the Division : b

//         Enter the Address : kjn

//         ------MENU-------
// 1.Insert and overwrite
// 2.Show
// 3.Search & Edit(number)
// 4.Delete a Student Record
// 5.Exit
//         Enter the Choice        :2

//         1               c               b               kjn
//         2               b               b               kbdkdcc
//         ------MENU-------
// 1.Insert and overwrite
// 2.Show
// 3.Search & Edit(number)
// 4.Delete a Student Record
// 5.Exit
//         Enter the Choice        :4
// Please Enter the Roll No. of Student Whose Info You Want to Delete: 1
// The record with the roll no. 1 has been deleted.

//         ------MENU-------
// 1.Insert and overwrite
// 2.Show
// 3.Search & Edit(number)
// 4.Delete a Student Record
// 5.Exit
//         Enter the Choice        :2

//         2               b               b               kbdkdcc
//         ------MENU-------
// 1.Insert and overwrite
// 2.Show
// 3.Search & Edit(number)
// 4.Delete a Student Record
// 5.Exit
//         Enter the Choice        :5
