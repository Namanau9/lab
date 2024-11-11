#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

char st[MAX];    // Stack for operators
int top = -1;    // Stack pointer

void push(char st[], char val);
char pop(char st[]);
void InixtoPostix(char source[], char target[]);
int getPriority(char op);

int main() {
    char inix[100], postix[100];

    printf("\nEnter any infix expression: ");
    fgets(inix, sizeof(inix), stdin);  // safer than gets()

    // Remove the newline character if present
    inix[strcspn(inix, "\n")] = 0;

    strcpy(postix, "");
    InixtoPostix(inix, postix);

    printf("\nThe corresponding postfix expression is: ");
    puts(postix);
    return 0;
}

void InixtoPostix(char source[], char target[]) {
    int i = 0, j = 0;
    char temp;
    
    while (source[i] != '\0') {
        if (source[i] == '(') {
            push(st, source[i]);
        } else if (source[i] == ')') {
            while (top != -1 && st[top] != '(') {
                target[j++] = pop(st);
            }
            if (top == -1) {
                printf("\nIncorrect Expression: Unmatched parentheses\n");
                exit(1);
            }
            pop(st);  // Pop the '('
        } else if (isalnum(source[i])) {  // Operand (either digit or alphabet)
            target[j++] = source[i];
        } else if (strchr("+-*/%^", source[i])) {  // Operator
            while (top != -1 && st[top] != '(' && 
                   getPriority(st[top]) >= getPriority(source[i])) {
                target[j++] = pop(st);
            }
            push(st, source[i]);
        } else {
            printf("\nIncorrect Element in Expression\n");
            exit(1);
        }
        i++;
    }

    // Pop all the remaining operators in the stack
    while (top != -1) {
        if (st[top] == '(') {
            printf("\nIncorrect Expression: Unmatched parentheses\n");
            exit(1);
        }
        target[j++] = pop(st);
    }

    target[j] = '\0';  // Null-terminate the result string
}

int getPriority(char op) {
    if (op == '^') {
        return 2;  // Power has the highest precedence
    } else if (op == '*' || op == '/' || op == '%') {
        return 1;  // Multiplication, Division, Remainder
    } else if (op == '+' || op == '-') {
        return 0;  // Addition and Subtraction
    }
    return -1;  // Invalid operator
}

void push(char st[], char val) {
    if (top == MAX - 1) {
        printf("\nStack Overflow\n");
    } else {
        top++;
        st[top] = val;
    }
}

char pop(char st[]) {
    char val = ' ';
    if (top == -1) {
        printf("\nStack Underflow\n");
    } else {
        val = st[top];
        top--;
    }
    return val;
}
