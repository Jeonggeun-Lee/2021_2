#include <stdio.h>
#include <sys/socket.h> //socket
#include <netinet/in.h> //IPPROTO_TCP, sockaddr_in
#include <stdlib.h> //implicit declaration of function 'exit'
#include <string.h> //memset()
#include <sys/types.h>
#include <dirent.h>

#define MAX 256
#define PORT 8999
#define PENDING 10
#define CLIENT_SIZE 5
#define TEMP_SIZE 1000

int sock_flag, conn_flag, length;
struct sockaddr_in server_addr, client_addr;
FILE* fp;
char buf[MAX];
char user[128];
int msg_t;
int data_len;
int msg_end;
char data[MAX];
char temp[TEMP_SIZE];

int DATA_SEND_RECV(int);
void serve();
void msg_analize(char buf[], char user[], int* msg_t, int* data_len, int* msg_end, char str[]);
void msg_make(int user_len, char user[], int msg_t, int data_len, int msg_end , char data[], char buf[]);
int main(int argc, char* arv[])
{
	

	if((sock_flag = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0){
		printf("Socket 생성 실패...\n");
		exit(0);
	}
	else
		printf("Socket 생성 성공...\n");

	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	server_addr.sin_port = htons(PORT);

	if((bind(sock_flag, (struct sockaddr*)&server_addr, sizeof(server_addr))) != 0){
		printf("소켓 바인딩 실패...\n");
		exit(0);
	}
	else
		printf("소켓 바인딩 성공...\n");

	if((listen(sock_flag, CLIENT_SIZE)) != 0){
		printf("연결 대기 실패...\n");
		exit(0);
	}

	length = sizeof(client_addr);
	if((conn_flag = accept(sock_flag, (struct sockaddr*)&client_addr, &length)) < 0){
		printf("서버-클라이언트 연결 실패\n");
		exit(0);
	}
	else
		printf("서버-클라이언트 연결 성공\n");

  	serve(conn_flag);
	
	close(sock_flag);
	
	return 0;
}

void serve()
{
	while(1){
		
		memset(buf, 0x00, MAX);
		read(conn_flag, buf, sizeof(buf));
		
		msg_analize(buf, user, &msg_t, &data_len, &msg_end, data);
		printf("user: %s\n", user);
		printf("msg_t: %x\n", msg_t);
		printf("data_len: %d\n", data_len);
		printf("msg_end: %x\n", msg_end);
		printf("str: %s\n", data);

		memset(buf, 0x00, MAX);
		if(msg_t == 0x10)
			msg_make(strlen(user), user, 0x11, data_len, 0x00 , data, buf);
		else if(msg_t == 0x50){
			memset(buf, 0x00, MAX);
			memset(data, 0x00, MAX);
			int end_val = 0x00;
			memcpy(data, &end_val, sizeof(int));
			msg_make(strlen(user), user, 0x51, sizeof(int), 0x00 , data, buf);
		}
		else if(msg_t == 0x20){
			fp = fopen(data,"wb");
			memset(buf, 0x00, MAX);
			memset(data, 0x00, MAX);
			int permission_val = 0x00;
			memcpy(data, &permission_val, sizeof(int));
			msg_make(strlen(user), user, 0x21, sizeof(int), 0x00, data, buf);
		}
		else if(msg_t == 0x22){
			fwrite(data, data_len, 1, fp);
			if(msg_end == 0x01) continue;
			else if(msg_end == 0x00){
				memset(buf, 0x00, MAX);
				memset(data, 0x00, MAX);
				int end_val = 0x00;
				memcpy(data, &end_val, sizeof(int));
				msg_make(strlen(user), user, 0x23, sizeof(int), 0x00, data, buf);
				fclose(fp);
			}
		}
		else if(msg_t == 0x40){
			DIR* dir;
			struct dirent* ent;
			dir = opendir("./");
			if(dir != NULL){
				while( (ent=readdir(dir))!=NULL ){
					
					strcat(temp, ent->d_name);
					strcat(temp, "\n");
				}
			}
			else{
				puts("cannot read directory");
				exit(1);
			}
			
			int len = strlen(temp);
			int num_tran;
			int last_bytes;
			num_tran = len/remained_space();
			last_bytes = len%remained_space();
			
			int i;
			for(i=0; i<num_tran; i++){
				memset(buf, 0x00, sizeof(buf));
				memset(data,0x00, sizeof(data));
				strncat(data, temp+i*remained_space(), remained_space());
				msg_make(strlen(user), user, 0x41, remained_space(), 0x01, data, buf);
				write(conn_flag, buf, sizeof(buf));
			}
			
			memset(buf, 0x00, sizeof(buf));
			memset(data,0x00, sizeof(data));
			
			strncat(data, temp+i*remained_space(), last_bytes);

			msg_make(strlen(user), user, 0x41, last_bytes, 0x00, data, buf);
			write(conn_flag, buf, sizeof(buf));
			continue;
		}
		else if(msg_t == 0x30){
			char file_name[MAX];
			strncpy(file_name, data, data_len);
			file_name[data_len] = '\0';
			printf("file_name: %s\n", file_name);

			memset(buf, 0x00, MAX);
			memset(data, 0x00, MAX);
			int permission_val = 0x00;
			memcpy(data, &permission_val, sizeof(int));
			msg_make(strlen(user), user, 0x31, sizeof(int), 0x00 , data, buf);
			write(conn_flag, buf, sizeof(buf));

			FILE* fp = fopen(file_name, "rb");
			if(fp==NULL){
				puts("src file open failed");
				exit(1);
			}
			int size;
			int num_trans;
			int last_bytes;
			fseek(fp, 0, SEEK_END);
			size = ftell(fp);
			printf("size: %d\n",size);
			fseek(fp, 0, SEEK_SET);
			num_trans = size/remained_space();
			last_bytes = size%remained_space();
			for(int i=0; i<num_trans; i++){
				memset(buf, 0x00, sizeof(buf));
				memset(data,0x00, sizeof(data));
				fread(data, remained_space(),1, fp);
				msg_make(strlen(user), user, 0x32, remained_space(), 0x01, data, buf);
				write(conn_flag, buf, sizeof(buf));
			}
			memset(buf, 0x00, sizeof(buf));
			memset(data,0x00, sizeof(data));
			fread(data, last_bytes,1, fp);
			msg_make(strlen(user), user, 0x32, last_bytes, 0x00, data, buf);
			write(conn_flag, buf, sizeof(buf));
			fclose(fp);
			continue;
		}
		write(conn_flag, buf, sizeof(buf));
		if(msg_t == 0x50) break;
	}
}

void msg_analize(char buf[], char user[], int* msg_t, int* data_len, int* msg_end, char str[]){
	char* ptr = strtok(buf,"|");
	strcpy(user, ptr);
	ptr = strtok(NULL, "|");
	memcpy(msg_t, ptr, sizeof(int));
	//ptr = strtok(NULL, "|");
	ptr = ptr+sizeof(int)+sizeof(char);
	memcpy(data_len, ptr, sizeof(int));
	//ptr = strtok(NULL, "|");
	ptr = ptr+sizeof(int)+sizeof(char);
	memcpy(msg_end, ptr, sizeof(int));
	//ptr = strtok(NULL, "|");
	ptr = ptr+sizeof(int)+sizeof(char);
	memset(str, 0x00, (*data_len)+1);
	memcpy(str, ptr, *data_len);
}

void msg_make(int user_len, char user[], int msg_t, int data_len, int msg_end , char data[], char buf[]){
	int offset = 0;
	char sep = '|';
	memcpy(buf, user, user_len);
	offset += user_len;
	memcpy(buf+offset, &sep, sizeof(char));
	offset += sizeof(char);
	memcpy(buf+offset, &msg_t, sizeof(int));
	offset += sizeof(int);
	memcpy(buf+offset, &sep, sizeof(char));
	offset += sizeof(char);
	memcpy(buf+offset, &data_len, sizeof(int));
	offset += sizeof(int);
	memcpy(buf+offset, &sep, sizeof(char));
	offset += sizeof(char);
	memcpy(buf+offset, &msg_end, sizeof(int));
	offset += sizeof(int);
	memcpy(buf+offset, &sep, sizeof(char));
	offset += sizeof(char);
	memcpy(buf+offset, data, data_len);
}

int remained_space(){
	return MAX - strlen(user) -1 -sizeof(int) -1 -sizeof(int) -1 -sizeof(int) -1;
}

int len_cal(){
	int rem_space = remained_space();
	if(rem_space<strlen(data)-1) return rem_space;
	else return strlen(data)-1;
}