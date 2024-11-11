#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define SIZE 20

struct stack {
    int top;
    char data[SIZE];
};

typedef struct stack STACK;

// Push function to add element to the stack
void push(STACK *s, char item) {
    if (s->top == SIZE - 1) {
        printf("\nStack Overflow! Cannot push '%c'\n", item);
        exit(1); // Exit if the stack is full
    }
    s->data[++(s->top)] = item;
}

// Pop function to remove element from the stack
char pop(STACK *s) {
    if (s->top == -1) {
        printf("\nStack Underflow!\n");
        exit(1); // Exit if the stack is empty
    }
    return s->data[(s->top)--];
}

// Function to return the precedence of operators
int preced(char symbol) {
    switch (symbol) {
        case '^': return 5; // Highest precedence for power
        case '*': case '/': return 3; // Multiplication and Division
        case '+': case '-': return 1; // Addition and Subtraction
        default: return -1; // Invalid symbol
    }
}

// Function to convert infix to postfix expression
void infixtopostfix(STACK *s, char infix[SIZE]) {
    int i, j = 0;
    char postfix[SIZE], temp, symbol;

    // Process each character in the infix expression
    for (i = 0; infix[i] != '\0'; i++) {
        symbol = infix[i];

        // If the symbol is an operand, add it to the postfix expression
        if (isalnum(symbol)) {
            postfix[j++] = symbol;
        } else {
            switch (symbol) {
                case '(':  // Left parenthesis, push onto stack
                    push(s, symbol);
                    break;

                case ')':  // Right parenthesis, pop until left parenthesis is found
                    temp = pop(s);
                    while (temp != '(') {
                        postfix[j++] = temp;
                        temp = pop(s);
                    }
                    break;

                // Operators
                case '+': case '-': case '*': case '/': case '^':
                    // Handle precedence and pop higher precedence operators
                    while (s->top != -1 && preced(s->data[s->top]) >= preced(symbol) && s->data[s->top] != '(') {
                        postfix[j++] = pop(s);
                    }
                    push(s, symbol);
                    break;

                default:
                    printf("\nInvalid character encountered: '%c'\n", symbol);
                    exit(1); // Exit for invalid character
            }
        }
    }

    // Pop any remaining operators from the stack
    while (s->top != -1) {
        char remaining = pop(s);
        if (remaining == '(') {
            printf("\nMismatched parentheses!\n");
            exit(1); // Exit for unmatched parentheses
        }
        postfix[j++] = remaining;
    }

    postfix[j] = '\0'; // Null-terminate the postfix string

    printf("\nThe postfix expression is: %s\n", postfix);
}

int main() {
    STACK s;
    s.top = -1; // Initialize stack
    char infix[SIZE];

    // Read infix expression from user input
    printf("\nEnter an infix expression: ");
    fgets(infix, sizeof(infix), stdin);
    infix[strcspn(infix, "\n")] = 0; // Remove the newline character if present

    infixtopostfix(&s, infix);

    return 0;
}
