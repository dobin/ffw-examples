#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>
#include <crypt.h>
#include <sys/types.h>
#include <sys/socket.h>


/* Do nothing with first message */
void handleData0(char *data, int len) {
    printf("Auth success\n");
}

/* Second message is stack based buffer overflow */
void handleData1(char *data, int len) {
    char buff[8];
    memcpy(buff, data, len);
    printf("%s\n", buff); // so it is not optimized away
}

/* Third message is heap overflow */
void handleData2(char *data, int len) {
    char *buff = malloc(8);
    memcpy(buff, data, len);
    printf("%s\n", buff); // so it is not optimized away
    free(buff);
}


void doprocessing (int sock) {
	char data[1024];
	int n = 0;
    int len = 0;

    while(1) {
    	bzero(data, sizeof(data));
    	len = read(sock, data, 1024);

        if(len == 0) {
            return;
        }

        printf("Received data with len: %i on state: %i\n", len, n);
        switch(n) {
            case 0:
                handleData0(data, len);
                write(sock, "ok", 2);
                break;
            case 1:
                handleData1(data, len);
                write(sock, "ok", 2);
                break;
            case 2:
                handleData2(data, len);
                write(sock, "ok", 2);
                return; // finito
                break;
            default:
                return;
        }

        n++;
    }
}


int main( int argc, char *argv[] ) {
    int sockfd, newsockfd, portno, clilen;
    char buffer[256];
    struct sockaddr_in serv_addr, cli_addr;
    int n, pid;

    if(argc == 2) {
        portno = atoi(argv[1]);
    } else {
        portno = 5001;
    }

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
      perror("ERROR opening socket");
      exit(1);
    }

    int reuse = 1;
    if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEPORT, (const char*)&reuse, sizeof(reuse)) < 0)
        perror("setsockopt(SO_REUSEPORT) failed");

    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);

    printf("Listening on port: %i\n", portno);

    /* Now bind the host address using bind() call.*/
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
        perror("ERROR on binding");
        exit(1);
    }

    listen(sockfd,5);
    clilen = sizeof(cli_addr);

    while (1) {
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
        if (newsockfd < 0) {
             perror("ERROR on accept");
             exit(1);
        }
        printf("New client connected\n");

        doprocessing(newsockfd);
        shutdown(newsockfd, 2);
        close(newsockfd);
    }
}
