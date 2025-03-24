#include <stdio.h>
#include <string.h>

void encrypt(char text[], int shift) {
    for (int i = 0; text[i] != '\0'; ++i) {
        char c = text[i];
        if (c >= 'a' && c <= 'z') {
            text[i] = (c - 'a' + shift) % 26 + 'a';
        } else if (c >= 'A' && c <= 'Z') {
            text[i] = (c - 'A' + shift) % 26 + 'A';
        }
    }
}

int main() {
    char text[100];
    int shift;
    printf("Enter text: ");
    fgets(text, 100, stdin);
    printf("Enter shift: ");
    scanf("%d", &shift);

    encrypt(text, shift);
    printf("Encrypted text: %s", text);
    return 0;
}
