#include<iostream>
#include<stdio.h>
#include<windows.h>
// using namespace std;
HWND workerw = NULL;
inline BOOL CALLBACK EnumWindowsProc(HWND handle, LPARAM lparam){
    HWND defview = FindWindowEx(handle, 0, "SHELLDLL_DefView", NULL);
    if(defview != NULL){
        workerw = FindWindowEx(0, handle, "WorkerW", 0);
    }
    return true;
}
int main(){
    // printf("hello,你好");
    // std::cout << "你好" << std::endl;
    HWND windowHandle = FindWindow("Progman", NULL);
    // std::cout << windowHandle << std::endl;
    EnumWindowsProc(windowHandle, 0);
     return 0;
}