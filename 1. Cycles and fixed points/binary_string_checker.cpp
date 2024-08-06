#include <iostream>
#include <fstream>
#include <random>
#include <time.h>
#include <bitset>

int aaaCount(int n, unsigned long x){
    int count = 0;
    int a = 0;
    for(int j=0;j<n;j++){
        if(x%2 == 0)
            a++;
        else
            a = 0;
            
        x=x/2;
        if(a>=3) count++;
    }
    return count;
}

bool aaaExists(int n, unsigned long x){
    int a = 0;
    for(int j=0;j<n;j++){
        if(x%2 == 0)
            a++;
        else
            a = 0;
            
        x=x/2;
        if(a>=3) return true;
    }
    return false;
}

bool abbExists(int n, unsigned long x){
    int a = 0;
    int b = 0;
    for(int j=0;j<n;j++){
        if(x%2 == 0){
            a = 1;
            b = 0;
        }else{
            if(a == 1 && b == 1)
                return true;
            if(b == 2)
                a = 0;
            b++;
        }
        x=x/2;
    }
    return false;
}

unsigned long randomBits(int n){
    int a = rand();
    int b = rand();
    unsigned long bits = 
    ((unsigned long)rand()<<31) + 
    ((unsigned long)rand())>>(62-n); 
    return bits;
}

void all_aaa(){
    std::ofstream fout("data/all_aaa.txt");
    for(int n=0;n<50;n++){
        unsigned long count = 0;
        unsigned long i = 0;
        while(i < ((unsigned long)1<<n)){
            count += aaaExists(n,i);
            i++;
        }
        std::cout<<n<<": "<<count<<std::endl;
        fout<<count<<std::endl;
    }
}
void all_abb(){
    std::ofstream fout("data/all_abb.txt");
    for(int n=0;n<50;n++){
        unsigned long count = 0;
        unsigned long i = 0;
        while(i < ((unsigned long)1<<n)){
            count += abbExists(n,i);
            i++;
        }
        std::cout<<n<<": "<<count<<std::endl;
        fout<<count<<std::endl;
    }
}
void count_aaa(){
    std::ofstream fout("data/all_aaa_cout.txt");
    for(int n=0;n<50;n++){
        unsigned long count = 0;
        unsigned long i = 0;
        while(i < ((unsigned long)1<<n)){
            count += aaaCount(n,i);
            i++;
        }
        double average = (double)count / (i+1);
        std::cout<<n<<": "<<average<<std::endl;
        fout<<average<<std::endl;
    }
}
void random_aaa(){
    std::ofstream fout("data/rand_aaa.txt");
    int maxk = 100000;
    for(int n=0;n<=50;n++){
        unsigned long long count = 0;
        for(int k=0;k<maxk;k++){
            count += aaaExists(n,randomBits(n));
        }
        std::cout<<n<<": "<<(count<<n)/maxk <<std::endl;
        fout<<(count<<n)/maxk<<std::endl;
    }

}
void random_abb(){
    std::ofstream fout("data/rand_abb.txt");
    int maxk = 100000;
    for(int n=0;n<=50;n++){
        unsigned long long count = 0;
        for(int k=0;k<maxk;k++){
            count += abbExists(n,randomBits(n));
        }
        std::cout<<n<<": "<<(count<<n)/maxk <<std::endl;
        fout<<(count<<n)/maxk<<std::endl;
    }
}
void random_aaa_count(){
    std::ofstream fout("data/rand_aaa_count.txt");
    int maxk = 100000;
    for(int n=0;n<=50;n++){
        int count = 0;
        for(int k=0;k<maxk;k++){
            count += aaaCount(n,randomBits(n));
        }
        double average = (double)count / maxk;
        std::cout<<n<<": "<<average<<std::endl;
        fout<<average<<std::endl;
    }
}

int main(){
    srand(time(NULL));
    // all_aaa();
    // all_abb();
    // count_aaa();
    random_aaa();
    random_abb();
    // random_aaa_count();

}