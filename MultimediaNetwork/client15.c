#include <stdio.h>
#include <sys/socket.h> //socket
#include <netinet/in.h> //IPPROTO_TCP, socketaddr_in
#include <arpa/inet.h> // inet_addr
#include <stdlib.h> //implicit declaration of function 'exit'
#include <string.h> //memset()
#include <pthread.h>
#include <unistd.h>
#include <time.h>

#define MAX 256
#define SERVER_PORT 45000
#define PENDING 10
#define TEMP_SIZE 1000
#define Max_Transfer_Unit 200

int sock_flag, conn_flag;
struct sockaddr_in server_addr;

char buf[MAX];
char user[MAX];
char msg_t[MAX];
char data_len[MAX];
char msg_end[MAX];
char data[MAX];
char file_name[MAX];

char r_buf[MAX];
char r_user[MAX];
char r_msg_t[MAX];
char r_data_len[MAX];
char r_msg_end[MAX];
char r_data[MAX];
char r_temp[TEMP_SIZE];

int choice;
pthread_t pthread[2];
pthread_mutex_t mutex_lock;

int thr_id;
int result;
FILE* dfp;

void buf_reader(char r_buf[], int size);
int msg_make(char user[], char msg_t[], char data_len[], char msg_end[] , char data[], char buf[]);
void msg_analize(char buf[], char user[], char msg_t[], char data_len[], char msg_end[], char data[]);
void* msg_sender(void* param);
void* msg_receiver(void* param);

void display();
void chat();
void file_upload();
void file_list();
void file_download();

int main(int argc, char* argv[])
{
	memset(user, 0x00, MAX);
	strcpy(user, argv[1]);
	if((sock_flag = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0){
		printf("Socket 생성 실패...\n");
		exit(0);
	}
	else
		printf("Socket 생성 성공...\n");

	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	server_addr.sin_port = htons(SERVER_PORT);

	thr_id = pthread_create(&pthread[0], NULL, msg_sender, (void *)argv[1]);
	if(thr_id < 0){
		perror("pthread create error");
		exit(0);
	}
	thr_id = pthread_create(&pthread[1], NULL, msg_receiver, (void *)argv[1]);
	if(thr_id < 0){
		perror("pthread create error");
		exit(0);
	}

	pthread_join(pthread[0], (void*)&result);
	pthread_join(pthread[1], (void*)&result);

	close(sock_flag);
	return 0;
}

void display(){
	puts("***프로그램 순서***");
	puts("채팅: 채팅 메시지 입력->quit 입력->채팅 종료->");
	puts("파일 업로드: 업로드 파일명 입력->업로드->");
	puts("파일 리스트: 파일 리스트 출력->");
	puts("파일 다운로드: 다운로드 파일명 입력->다운로드->");
	puts("프로그램 종료");
}

int msg_make(char user[], char msg_t[], char data_len[], char msg_end[] , char data[], char buf[]){
	char* sep = "|";
	memset(buf, 0x00, MAX);
	strcat(buf, user);	//initially defined
	strcat(buf, sep);	//1 byte
	strcat(buf, msg_t);	//4 byte
	strcat(buf, sep);	//1 byte
	strcat(buf, data_len);//variable
	strcat(buf, sep);	//1 byte
	strcat(buf, msg_end);//4 byte
	strcat(buf, sep);	//1 byte
	int data_len_int = atoi(data_len);
	int offset = strlen(user) + 1 + strlen(msg_t) + 1 + strlen(data_len) + 1 + strlen(msg_end) + 1;
	if(MAX - offset < data_len_int) return 1;
	memcpy(buf+offset, data, data_len_int);
	puts("message make:");
	buf_reader(buf, MAX);
	return 0;
}

void buf_reader(char r_buf[], int size){
	for(int i=0; i<size; i++){
		printf("%c", r_buf[i]);
	}
	puts("");
}

void msg_analize(char r_buf[], char r_user[], char r_msg_t[], char r_data_len[], char r_msg_end[], char r_data[]){
	puts("received:");
	buf_reader(r_buf, MAX);
	
	memset(r_user, 0x00, MAX);
	memset(r_msg_t, 0x00, MAX);
	memset(r_data_len, 0x00, MAX);
	memset(r_msg_end, 0x00, MAX);
	memset(r_data, 0x00, MAX);

  	char* ptr = strtok(r_buf, "|");
  	strcpy(r_user, ptr);
	ptr = strtok(NULL, "|");
	strcpy(r_msg_t, ptr);
	ptr = strtok(NULL, "|");
	strcpy(r_data_len, ptr);
	ptr = strtok(NULL, "|");
	strcpy(r_msg_end, ptr);
	ptr = strtok(NULL, "|");
	int r_data_len_int = atoi(r_data_len);
	memset(r_data, 0x00, MAX);
	memcpy(r_data, ptr, r_data_len_int);
	
	/*
	printf("r_user: %s\n",r_user);
	printf("r_msg_t: %s\n",r_msg_t);
	printf("r_data_len: %s\n",r_data_len);
	printf("r_msg_end: %s\n",r_msg_end);
	printf("r_data: %s\n",r_data);
	*/
}

void* msg_sender(void* param){
	if( (connect(sock_flag, (struct sockaddr*)&server_addr, sizeof(server_addr))) < 0 ){
		printf("서버-클라이언트 연결 실패\n");
		exit(0);
  	}
  	else
		printf("서버-클라이언트 연결 성공\n");
	
	display();
	chat();
	file_upload();
	sleep(5);
	file_list();
	file_download();
	
}

void* msg_receiver(void* param){
	while(1){
		
		memset(r_buf, 0x00, MAX);
		read(sock_flag, r_buf, MAX);
		
		msg_analize(r_buf, r_user, r_msg_t, r_data_len, r_msg_end, r_data);
		
		
		if(strcmp(r_msg_t, "0x51") == 0){
			if(strcmp(r_data, "0x00")==0){
				puts("program end");
				exit(0);
			}
			
		}
		else if(strcmp(r_msg_t, "0x41") == 0){
			strcat(r_temp, r_data);
			if(strcmp(r_msg_end, "0x00") == 0){
				puts("file list:");
				puts(r_temp);
			}
		}
		else if(strcmp(r_msg_t, "0x31") == 0){
			if(strcmp(r_data, "0x00") == 0){
				puts("download allowed");
					
				dfp = fopen(data, "w");
				if(dfp==NULL) {
					puts("no file to write on");
					exit(1);
				}
			}
			else if(strcmp(r_data, "0x01") == 0){
				puts("download denied");
			}
		}
		else if(strncmp(r_msg_t, "0x32", 4) == 0){
			
			fwrite(r_data, atoi(r_data_len), 1, dfp);


			if(strncmp(r_msg_end, "0x00", 4) ==0 ){
				puts("file closed");
				fclose(dfp);
				msg_make(user, "0x33", "4", "0x00", "0x00", buf);
				write(sock_flag, buf, MAX);
				sleep(2);
				msg_make(user, "0x50", "4", "0x00", "EXIT", buf);
				write(sock_flag, buf, MAX);
			}
		}
		
		sleep(1);
	}
}

void chat(){
  	while(1){
		memset(data, 0x00, MAX);
		fgets(data, MAX, stdin);
    	if(strncmp(data, "quit", 4)==0){
      			break;
    	}
		char len[MAX];
		sprintf(len, "%ld", strlen(data));
		if(msg_make(user, "0x10", len, "0x00", data, buf)==1){
			puts("message overflow");
			return;
		}
		write(sock_flag, buf, MAX);
  	}	
}

void file_upload(){
	memset(data, 0x00, MAX);
	fgets(data, MAX, stdin);
	int size = strlen(data);
	data[size-1] = '\0';
	strcpy(file_name,data);

	char len[MAX];
	sprintf(len, "%ld", strlen(data));
	if( msg_make(user, "0x20", len, "0x00", data, buf) == 1){
		puts("message overflow");
		return;
	}
	write(sock_flag, buf, MAX);
	
	while(1){
		puts("wait");
		
		if(strncmp(r_msg_t, "0x21",4)==0){
			
			break;
		}
		
	}

	if(strncmp(r_msg_t, "0x21",4)==0){
		if(strncmp(r_data, "0x00",4)==0){
			puts("upload allowed, upload start");
			printf("file_name: %s\n", file_name);
			FILE* fp = fopen(file_name, "r");
			
			if(fp==NULL){
				puts("src file open failed");
				exit(1);
			}
			
			int size;
			int num_trans;
			int last_bytes;
			int remained_space;
			remained_space = MAX - ( strlen(user) + 1 + 4 + 1 + 3 + 1 + 4 + 1)-1;
			fseek(fp, 0, SEEK_END);
			size = ftell(fp);
			printf("size: %d\n",size);
			fseek(fp, 0, SEEK_SET);

			num_trans = size/remained_space;
			last_bytes = size%remained_space;
			printf("last bytes: %d\n", last_bytes);

			char rs[MAX];
			for(int i=0; i<num_trans; i++){
				memset(data,0x00, MAX);
				fread(data, remained_space, 1, fp);	
				sprintf(rs, "%d", remained_space);
				if(i == num_trans-1 && last_bytes == 0){
					msg_make(user, "0x22", rs, "0x00", data, buf);
				}
				else{
					msg_make(user, "0x22", rs, "0x01", data, buf);
				}
				write(sock_flag, buf, sizeof(buf));
			}

			if(last_bytes != 0){
				memset(data,0x00, sizeof(data));
				fread(data, last_bytes, 1, fp);

				memset(rs, 0x00, MAX);
				sprintf(rs, "%d", last_bytes);
				msg_make(user, "0x22", rs, "0x00", data, buf);
				write(sock_flag, buf, MAX);
			}
			
			fclose(fp);
			puts("transmission completed");
		}
		else if( strncmp(r_data, "0x01",4) == 0){
			puts("upload denied");
		}
	}
}

void file_list(){
	msg_make(user, "0x40", "4", "0x00", "0x00", buf);
	write(sock_flag, buf, sizeof(buf));
}

void file_download(){
	memset(data, 0x00, MAX);
	fgets(data, MAX, stdin);
	int size = strlen(data);
	data[size-1] = '\0';

	char len[MAX];
	sprintf(len, "%ld", strlen(data));
	msg_make(user, "0x30", len, "0x00", data, buf);
	write(sock_flag, buf, MAX);
}

