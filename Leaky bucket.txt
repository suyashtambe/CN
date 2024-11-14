#include <stdio.h>

int main() {
    int incoming, outgoing, buck_size, n, store = 0;

    printf("Enter bucket size, outgoing rate, and number of inputs: ");
    scanf("%d %d %d", &buck_size, &outgoing, &n);

    while (n > 0) {
        printf("Enter the incoming packet size: ");
        scanf("%d", &incoming);
        printf("Incoming packet size %d\n", incoming);

        if (incoming <= (buck_size - store)) {
            store += incoming;
            printf("Bucket buffer size %d out of %d\n", store, buck_size);
        } else {
            printf("Dropped %d packets\n", incoming - (buck_size - store));
            printf("Bucket buffer size %d out of %d\n", store, buck_size);
            store = buck_size;  // The bucket is full, no more packets can be added.
        }

        store = store - outgoing;
        if (store < 0) {
            store = 0;  // Ensure the bucket doesn't go negative.
        }

        printf("After outgoing %d packets left out of %d in buffer\n", store, buck_size);
        n--;
    }

    return 0;
}