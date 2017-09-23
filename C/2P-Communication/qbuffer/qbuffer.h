#define DIRTY 1 //ready to write new data
#define TAKEN 0
#define NOT_READY -1
#define BUFFER_SIZE 1024

typedef struct {
	char name[37];
	char sbuf_nxt[37];
	int state;
	unsigned checksum;
	pthread_mutex_t mutex;
	char shared_data[BUFFER_SIZE];	
}q_buf;


q_buf *create_buffer_q(int max_num);
int make_circular(q_buf *node, char *hname);
int atomic_write_buffer(q_buf *node, char *string);
int atomic_read_buffer(q_buf *node, char *string);
