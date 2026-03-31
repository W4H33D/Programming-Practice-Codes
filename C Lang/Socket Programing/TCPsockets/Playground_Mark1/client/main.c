#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char * argv[]) {

    if (argc != 3) {
        fprintf(stderr, "Usage: %s <IP Address> <Port Number>\n", argv[0]);
        return 1; // Exit with error
    }
    char * ipAddr = argv[1];
    int portNo = atoi(argv[2]);
    if (portNo <= 0 || portNo > 65535) {
        fprintf(stderr, "[-] Error: Invalid port number %d\n", portNo);
        return 1;
    }

    // Creating Socket File Descriptor
    int socketFD = socket(AF_INET, SOCK_STREAM, 0);
    if (socketFD == -1) {
        perror("[-] Error In Creating Socket");
        fprintf(stderr, "Socket Error [%d]: %s\n", errno, strerror(errno));
        close(socketFD);
        exit(-1);
    }

    // Setting Up address Object for socket
    struct sockaddr_in addrObject;
    addrObject.sin_family = AF_INET;
    addrObject.sin_port = htons(portNo);
    addrObject.sin_addr.s_addr = inet_addr(ipAddr);

    // Sending Connection To The Socket
    int conStat = connect(socketFD, (struct sockaddr*) &addrObject, sizeof(addrObject) );
    if (conStat == -1) {
        perror("[-] Error In Connecting To The Socket");
        fprintf(stderr, "Connection Error [%d]: %s\n", errno, strerror(errno));
        close(socketFD);
        exit(-1);
    }
    else
        printf("Connection Established To %s\n", ipAddr);

    // Sending Data To The Server
    char * reqBuff = "Hello From Client\n";
    int sendStat = send(socketFD, reqBuff, strlen(reqBuff), 0);
    if (sendStat == -1) {
        perror("[-] Error In Sending Data To Socket");
        fprintf(stderr, "Sending Error [%d]: %s\n", errno, strerror(errno));
        close(socketFD);
        exit(-1);
    }

    // Receiving Data From The Server
    char recvBuff[3024];
    int recvStat = recv(socketFD, recvBuff, sizeof(recvBuff) - 1, 0);
    if (recvStat == -1) {
        perror("[-] Error In Receiving Data");
    } else if (recvStat == 0) {
        printf("Server Closed The Connection.\n");
    } else {
        // Manually null-terminate the string so printf knows where it ends
        recvBuff[recvStat] = '\0';
        printf("%s", recvBuff);
    }

    close(socketFD);
    return 0;
}
