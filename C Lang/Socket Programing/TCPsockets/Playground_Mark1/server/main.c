#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void) {
    const int serving_port = 4444;
    char ip_str[INET_ADDRSTRLEN]; // Buffer to hold the human-readable IP

    // Creating Socket
    const int socketFD = socket(AF_INET, SOCK_STREAM, 0);             // Syntax socket(int domain, int type, int protocol)
    if (socketFD == -1) {
        perror("[-] Error In Creating Socket");
        fprintf(stderr, "Socket Error [%d]: %s\n", errno, strerror(errno));
        close(socketFD);
        exit(-1);
    }

    // Setting Up address Object for socket
    struct sockaddr_in addrObject;
    memset(&addrObject, 0, sizeof(addrObject));
    addrObject.sin_family = AF_INET;
    addrObject.sin_port = htons(serving_port);
    addrObject.sin_addr.s_addr = htonl(INADDR_ANY);

    // Binding Address To The Socket
    const int bindStat = bind(socketFD, (struct sockaddr *)&addrObject, sizeof(addrObject));     // Syntax: int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
    if (bindStat == -1) {
        perror("[-] Error In Binding Address");
        fprintf(stderr, "Binding Error [%d]: %s\n", errno, strerror(errno));
        close(socketFD);
        exit(EXIT_FAILURE);
    }
    else
        printf("Binding Successful On Port %d\n", serving_port);
    
    // Listening For Connections
    const int lStat = listen(socketFD, 10);     // Syntax: int listen(int sockfd, int backlog);
    if (lStat == -1) {
        perror("[-] Error In Listening");
        fprintf(stderr, "Listening Error [%d]: %s\n", errno, strerror(errno));
        close(socketFD);
        exit(EXIT_FAILURE);
    }
    else
        printf("Listening For Connections %s:%d\n", "0.0.0.0",serving_port);

    // Accepting Connections
    struct sockaddr_in client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    int client_fd = accept(socketFD, (struct sockaddr *)&client_addr, &client_addr_len);        // Syntax: int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
    if (client_fd == -1) {
        perror("[-] Error In Accepting Connections");
        fprintf(stderr, "Acceptance Error [%d]: %s\n", errno, strerror(errno));
        close(socketFD);
        exit(EXIT_FAILURE);
    }
    else {
        inet_ntop(AF_INET, &client_addr.sin_addr, ip_str, INET_ADDRSTRLEN);
        printf("Connected To %s:%d\n", ip_str, serving_port);

        // Sending Data
        char *message = "Hello From Server!\n";
        ssize_t bytes_sent = send(client_fd, message, strlen(message), 0);
        if (bytes_sent == -1) {
            perror("[-] Error In Sending Data To Client");
            fprintf(stderr, "Sending Error [%d]: %s\n", errno, strerror(errno));
        }

        // Receiving data
        char buffer[1024];
        ssize_t bytes_received = recv(client_fd, buffer, sizeof(buffer) - 1, 0);
        if (bytes_received == -1) {
            perror("[-] Error In Receiving Data");
            fprintf(stderr, "Receiving Error [%d]: %s\n", errno, strerror(errno));
        } else if (bytes_received == 0) {
            printf("Client %s Disconnected.\n", ip_str);
        } else {
            buffer[bytes_received] = '\0'; // Null-terminate the received data
            printf("%s\n", buffer);
        }

        close(socketFD);
        return 0;
    }
}
