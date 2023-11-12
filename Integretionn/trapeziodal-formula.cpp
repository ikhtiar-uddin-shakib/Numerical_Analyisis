// Trapoizoidal Formula : h((y0+yn)/2)+ y1 + y2 + ........ + y(n-1))

// upper limit = 1
// lower limit = 0
// integretion = 1/(1+x*x) dx

#include<iostream>
using namespace std;

double fx (double x){
    return 1/(1+x*x);
}
int main(){
    double lower,upper,step,inte,h,y0, y1,i,x;
    cin>>lower>>upper>>step;
    h = (upper - lower)/step;
    y0 = fx(lower);
    y1 = fx(upper);
    inte = (y0 + y1) /2;

    for(i = 1; i<= step-1; i++){
        x = lower + i*h;
        inte = inte + fx(x);
    }
    inte = inte * h;
    cout<<inte;
}