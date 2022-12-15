#include <stdio.h>
#include <iostream>
#include <assert.h>

#define NM (1LL << 63) /* negative most */
#define PM ~NM         /* positive most */
#define LL(d) *((long long *)&(d))
#define EZ(d) LL(d) &= (PM >> 1), LL(d) |= (1023LL << 52)

int sign(double d) { return (LL(d) >> 63) & 1LL; }
int exponent(double d) { return (LL(d) >> 52) & 0x7ff; }
// `EZ(d) -> LL(d) &= (PM >> 1), (LL(d) >> 52) & 0x7ff;`
// 将`d`的指数部分的$11$位填上$1023$(低$10$位全$1$，最高位为$0$)
// 因为采用的是余$1023$码，所以这条语句的目的是将指数部分变为$0$
double mantissa(double d) { return EZ(d), d; }

#define sign(d) (sign(d) ? -1 : 1)
#define exponent(d) (exponent(d) - 1023)

/* print binary of a double */
void printbd(double d)
{
    /* from left to right */
    printf("%+g =\n", d);
    printf("%4c", 32);
    for (int i = 0; i < 64; ++i)
    {
        if (i == 0 || i == 1 || i == 12)
            putchar('|');
        // 这里只能用右移，因为 (long long -> int) 要截断到低32位
        putchar(((LL(d) >> (63 - i)) & 1LL) + '0');
    }
    printf("|\n");
    printf("%4c", 32);
    printf("%+d * %g * 2^(%d)\n", sign(d), mantissa(d), exponent(d));
}

int main()
{
    assert(sign(+0.5) == +1);
    assert(sign(-0.5) == -1);
    double a = 0.0;
    std::cout<<"input:";
    std::cin>>a;
        printbd(a);
        // printf("%f",a);

    return 0;
}