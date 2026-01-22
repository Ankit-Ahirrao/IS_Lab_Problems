#include<iostream>
// #include<bits/stdc++.h>
using namespace std;

string encrypt(string text, int s){
    string result = "";
    for(int i=0;i<text.length();i++){
        if(isupper(text[i])){
            result += char(int(text[i]+s-65)%26 + 65);

        }
        else{
            result += char(int(text[i]+s-97)%26 + 97);
        }
    }
    return result;
}

int main(){
    string text = "ANKIT";
    int s = 4;
    cout<<"Original Text : "<<text<<endl;
    cout<<"Shift : "<<s<<endl;
    cout<<"Cipher: "<<encrypt(text, s)<<endl;
}