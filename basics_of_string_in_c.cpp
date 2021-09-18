#include <iostream>
#include<cstring>

using namespace std;

int main() {
  // char* inp = "hello world";
   
   char a[100] ="hello";
        
   char b[100];
   
   for(int i = 0;i<strlen(a);i++){
       
       b[i]=a[i];
   }
   
   b[1]='q';
   cout<<b<<endl;
   cout<<a;     
        // char* y;
        // y=&a[0];
        
        // *(y+1)='g';
        
        // cout<<a;
        // cout<<y;

   
 
}


//strncpy(a,b,sizeof(b));
//strlen
//strcat(a,b) a = a+b